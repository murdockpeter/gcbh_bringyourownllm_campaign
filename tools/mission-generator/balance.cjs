'use strict';

const ROLE_WEIGHT = Object.freeze({
  logistics: 1, base: 2, tanker: 2, reconnaissance: 3, maritime_patrol: 4,
  fighter: 7, strike: 8, surface_combatant: 9, coastal_strike: 8,
  air_defense: 7, submarine: 9, ground: 3, support: 2,
});

function scoreUnit(unit) {
  const base = ROLE_WEIGHT[unit.role] || 2;
  const condition = (unit.structural_integrity_pct / 100) * (unit.readiness_pct / 100);
  const sustainment = 0.4 + 0.3 * unit.fuelFraction + 0.3 * (unit.ammo_pct / 100);
  const fatigue = 1 - Math.min(0.5, unit.crew_fatigue_pct / 200);
  return Number((base * condition * sustainment * fatigue).toFixed(3));
}

function scoreSide(units, objective) {
  const force = units.reduce((sum, unit) => sum + scoreUnit(unit), 0);
  const protectedBurden = objective.type === 'ProtectGoal' ? objective.targets.length
    : (objective.goals || []).filter((goal) => goal.type === 'ProtectGoal').reduce((sum, goal) => sum + goal.targets.length, 0);
  const objectiveBurden = 1 + protectedBurden * 0.04;
  return { force: Number(force.toFixed(3)), objectiveBurden: Number(objectiveBurden.toFixed(3)), effective: Number((force / objectiveBurden).toFixed(3)) };
}

function assessBalance(units, objectives) {
  const blue = scoreSide(units.blue, objectives.blue);
  const red = scoreSide(units.red, objectives.red);
  const ratio = red.effective === 0 ? 99 : Number((blue.effective / red.effective).toFixed(3));
  const warnings = [];
  if (ratio > 2) warnings.push('BLUE effective strength is more than twice RED effective strength.');
  if (ratio < 0.5) warnings.push('RED effective strength is more than twice BLUE effective strength.');
  return { blue, red, ratio, warnings, model: 'role-condition-sustainment-v1' };
}

module.exports = { ROLE_WEIGHT, scoreUnit, scoreSide, assessBalance };
