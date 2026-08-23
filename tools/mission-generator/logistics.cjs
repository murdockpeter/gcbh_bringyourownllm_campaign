'use strict';

const { GeneratorError } = require('./errors.cjs');

const COMBAT_ROLES = new Set(['fighter', 'strike', 'surface_combatant', 'coastal_strike', 'air_defense', 'submarine']);

function scaledQuantity(quantity, ammoPercent) {
  if (quantity <= 0 || ammoPercent <= 0) return 0;
  return Math.min(quantity, Math.max(1, Math.floor((quantity * ammoPercent) / 100)));
}

function missionSpeed(unit) {
  const nominal = unit.domain === 'air' ? Math.min(unit.platform.maxSpeedKts || 420, 420)
    : unit.domain === 'ship' || unit.domain === 'sub' ? Math.min(unit.platform.maxSpeedKts || 18, 22)
      : 0;
  return unit.speed_limit_kts > 0 ? Math.min(nominal, unit.speed_limit_kts) : nominal;
}

function planUnit(unit, database, year, override) {
  const sourceLoadout = database.defaultLoadout(unit.platform_class, year);
  const selectedLoadout = override ? database.validateLoadout(unit.platform_class, override) : sourceLoadout.launchers;
  const launchers = selectedLoadout
    .map((launcher) => ({
      launcherId: launcher.launcherId,
      item: launcher.item,
      quantity: scaledQuantity(launcher.quantity, unit.ammo_pct),
    }))
    .filter((launcher) => launcher.quantity > 0);
  if (COMBAT_ROLES.has(unit.role) && unit.ammo_pct > 0 && launchers.length === 0 && !['air_defense', 'coastal_strike'].includes(unit.role)) {
    throw new GeneratorError('LOADOUT_EMPTY', `No database-backed launcher loadout is available for combat unit ${unit.unit_name} (${unit.platform_class})`);
  }
  const sorties = Number(unit.logistics?.sorties_available_next_12h ?? (unit.domain === 'air' ? 1 : 0));
  if (unit.domain === 'air' && sorties <= 0) throw new GeneratorError('SORTIE_UNAVAILABLE', `${unit.unit_name} has no sorties available`);
  const tasks = unit.domain === 'air' ? ['Aircraft1'] : unit.domain === 'ship' ? ['Ship1', 'ShipDefense'] : unit.domain === 'sub' ? ['Submarine1'] : ['Ground1'];
  if (launchers.length && COMBAT_ROLES.has(unit.role)) tasks.push(unit.role === 'air_defense' ? 'PointDefense' : 'AutoAttack');
  if (unit.domain !== 'ground' && unit.role !== 'base') tasks.push('Nav');
  return {
    ...unit,
    speed: missionSpeed(unit),
    fuelFraction: Number((unit.fuel_pct / 100).toFixed(4)),
    launchers,
    magazines: (override ? [] : sourceLoadout.magazines).map((item) => ({
      ...item,
      quantity: scaledQuantity(item.quantity, item.item === 'Fuel' ? unit.fuel_pct : unit.ammo_pct),
    })).filter((item) => item.quantity > 0),
    loadoutSetup: override ? 'scenario-seed override' : sourceLoadout.setupName,
    tasks,
    sorties,
    persistence: {
      structural_integrity_pct: unit.structural_integrity_pct,
      readiness_pct: unit.readiness_pct,
      crew_fatigue_pct: unit.crew_fatigue_pct,
      fuel_pct: unit.fuel_pct,
      ammo_pct: unit.ammo_pct,
      speed_limit_kts: unit.speed_limit_kts,
      repair: unit.repair || {},
    },
  };
}

function packageCost(units) {
  return {
    fuel_points: units.reduce((sum, unit) => sum + Number(unit.logistics?.daily_upkeep_points || 0), 0),
    ordnance_points: units.filter((unit) => COMBAT_ROLES.has(unit.role)).reduce((sum, unit) => sum + Math.ceil(unit.ammo_pct / 20), 0),
    repair_capacity_points: units.filter((unit) => unit.status === 'damaged').reduce((sum, unit) => sum + Math.max(1, Math.ceil((100 - unit.structural_integrity_pct) / 20)), 0),
    air_sorties: units.filter((unit) => unit.domain === 'air').reduce((sum, unit) => sum + unit.sorties, 0),
  };
}

function validatePackageBudget(side, units, theaterLogistics = {}) {
  const cost = packageCost(units);
  const comparisons = [
    ['fuel_points', 'fuel_points'],
    ['ordnance_points', 'ordnance_points'],
    ['repair_capacity_points', 'repair_capacity_points'],
    ['air_sorties', 'air_sortie_capacity_next_24h'],
  ];
  const errors = [];
  for (const [costKey, budgetKey] of comparisons) {
    if (Number.isFinite(theaterLogistics[budgetKey]) && cost[costKey] > theaterLogistics[budgetKey]) {
      errors.push(`${costKey}: requires ${cost[costKey]}, available ${theaterLogistics[budgetKey]}`);
    }
  }
  if (errors.length) throw new GeneratorError('LOGISTICS_BUDGET', `${side.toUpperCase()} mission package exceeds campaign logistics`, errors);
  return { available: theaterLogistics, allocated: cost };
}

function validateAviationSupport(side, units, support = {}, durationHours = 6) {
  const aircraft = units.filter((unit) => unit.domain === 'air');
  if (!aircraft.length) return { mode: 'not_required', aircraft: 0 };
  const bases = units.filter((unit) => unit.role === 'base');
  if (support.mode === 'in_scenario' && !bases.length) {
    throw new GeneratorError('AVIATION_RECOVERY', `${side.toUpperCase()} declares in-scenario recovery but no recovery base or carrier was selected`);
  }
  if (support.mode === 'off_map' && (!support.location || !support.reason)) {
    throw new GeneratorError('AVIATION_RECOVERY', `${side.toUpperCase()} off-map recovery requires location and reason`);
  }
  if (!['in_scenario', 'off_map'].includes(support.mode)) {
    throw new GeneratorError('AVIATION_RECOVERY', `${side.toUpperCase()} aircraft require explicit in_scenario or off_map recovery support`);
  }
  const combatAircraft = aircraft.filter((unit) => ['fighter', 'strike'].includes(unit.role));
  const tankers = units.filter((unit) => unit.role === 'tanker');
  if (durationHours > 6 && combatAircraft.length && !tankers.length && !support.tanker_waiver_reason) {
    throw new GeneratorError('AVIATION_TANKER', `${side.toUpperCase()} combat aviation longer than six hours requires a tanker or tanker_waiver_reason`);
  }
  return { ...support, aircraft: aircraft.length, combat_aircraft: combatAircraft.length, tankers: tankers.length, in_scenario_bases: bases.map((unit) => unit.unit_name) };
}

function applyLogistics(roster, database, dateTime, loadoutOverrides = {}, campaignSides = {}, aviationSupport = {}, durationHours = 6) {
  const year = new Date(dateTime).getUTCFullYear();
  const result = {
    blue: roster.blue.map((unit) => planUnit(unit, database, year, loadoutOverrides[unit.unit_name] || loadoutOverrides[unit.platform_class])),
    red: roster.red.map((unit) => planUnit(unit, database, year, loadoutOverrides[unit.unit_name] || loadoutOverrides[unit.platform_class])),
    rejected: roster.rejected,
  };
  result.logistics = {
    blue: validatePackageBudget('blue', result.blue, campaignSides.blue?.theater_logistics),
    red: validatePackageBudget('red', result.red, campaignSides.red?.theater_logistics),
  };
  result.aviation = {
    blue: validateAviationSupport('blue', result.blue, aviationSupport.blue, durationHours),
    red: validateAviationSupport('red', result.red, aviationSupport.red, durationHours),
  };
  return result;
}

module.exports = {
  COMBAT_ROLES, scaledQuantity, missionSpeed, planUnit, packageCost,
  validatePackageBudget, validateAviationSupport, applyLogistics,
};
