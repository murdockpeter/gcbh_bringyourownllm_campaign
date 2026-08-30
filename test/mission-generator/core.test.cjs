'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { normalizeState, normalizeSeed } = require('../../tools/mission-generator/inputs.cjs');
const { createRng, hashValue } = require('../../tools/mission-generator/rng.cjs');
const { eligibility, inferRole } = require('../../tools/mission-generator/state.cjs');
const {
  scaledQuantity, missionSpeed, planUnit, loadoutItemMaximums, stockAviationMagazines,
  validatePackageBudget, validateAviationSupport,
} = require('../../tools/mission-generator/logistics.cjs');
const { ARCHETYPES, getArchetype } = require('../../tools/mission-generator/archetypes.cjs');
const { boundedQuantity, buildObjectives, assertApprovedGoals } = require('../../tools/mission-generator/objectives.cjs');
const { jitterPoint, pointFromBox, placeUnits } = require('../../tools/mission-generator/placement.cjs');
const { scoreUnit, assessBalance } = require('../../tools/mission-generator/balance.cjs');
const { renderScenario } = require('../../tools/mission-generator/renderer.cjs');
const { shiftLocalDateTime, applyVariation } = require('../../tools/mission-generator/variation.cjs');
const { validateContinuity } = require('../../tools/mission-generator/continuity.cjs');
const { summarizeLaunchers, loadoutMenus } = require('../../tools/mission-generator/loadout-picker.cjs');
const { baseUnit, baseState, baseSeed, plannedUnit } = require('./fixtures.cjs');

test('normalizes a valid campaign state', () => {
  const state = normalizeState(baseState());
  assert.equal(state.sides.blue.units[0].side, 'blue');
});

test('rejects invalid percentages and duplicate unit identities', () => {
  const state = baseState();
  state.sides.blue.units.push(baseUnit({ readiness_pct: 101, unit_name: 'Blue Escort' }));
  assert.throws(() => normalizeState(state), /validation failed/);
});

test('rejects unknown seed fields and unsupported archetypes', () => {
  assert.throws(() => normalizeSeed(baseSeed({ typo: true })), (error) => error.details.some((detail) => /not supported/.test(detail)));
  assert.throws(() => normalizeSeed(baseSeed({ archetype: 'raid' })), (error) => error.details.some((detail) => /unsupported/.test(detail)));
});

test('seed defaults are deterministic', () => {
  assert.equal(hashValue(normalizeSeed(baseSeed())), hashValue(normalizeSeed(baseSeed())));
});

test('unit directives validate staged hosts and supported presence states', () => {
  const seed = normalizeSeed(baseSeed({
    unit_directives: { blue: { 'Tiger 1': { presence: 'staged', host: 'Carrier', flight_deck_location: 2 } }, red: {} },
  }));
  assert.equal(seed.unit_directives.blue['Tiger 1'].host, 'Carrier');
  assert.throws(() => normalizeSeed(baseSeed({ unit_directives: { blue: { Bad: { presence: 'teleported' } }, red: {} } })), /validation failed/);
});

test('seed accepts named loadout choices and validates custom presets', () => {
  const seed = normalizeSeed(baseSeed({
    loadout_selections: { 'Test Aircraft': 'maritime strike' },
    loadout_presets: { 'Test Aircraft': { 'maritime strike': [{ launcherId: 0, item: 'Test Missile', quantity: 2 }] } },
  }));
  assert.equal(seed.loadout_selections['Test Aircraft'], 'maritime strike');
  assert.throws(() => normalizeSeed(baseSeed({
    loadout_presets: { 'Test Aircraft': { broken: [{ launcherId: -1, item: '', quantity: 0 }] } },
  })), /validation failed/);
});

test('interactive loadout menus combine database setups and scenario presets', () => {
  const state = baseState();
  const seed = baseSeed({
    date_time: '2026-05-23T16:30:00Z',
    loadout_presets: { 'Test Ship': { strike: [{ launcherId: 0, item: 'Bomb', quantity: 2 }] } },
  });
  const database = {
    platform: () => ({ domain: 'air' }),
    availableLoadouts: () => [{ setupName: 'CAP', launchers: [{ item: 'Missile', quantity: 2 }, { item: 'Missile', quantity: 2 }] }],
  };
  const menus = loadoutMenus(state, seed, database);
  assert.deepEqual(menus[0].choices.map((choice) => choice.name), ['strike', 'CAP']);
  assert.equal(summarizeLaunchers(menus[0].choices[1].launchers), '4x Missile');
});

test('seeded RNG repeats draws and records their labels', () => {
  const left = createRng('repeat');
  const right = createRng('repeat');
  assert.deepEqual([left.next('a'), left.next('b')], [right.next('a'), right.next('b')]);
  assert.deepEqual(left.draws.map((draw) => draw.label), ['a', 'b']);
});

test('different RNG seeds vary output', () => {
  assert.notEqual(createRng('left').next(), createRng('right').next());
});

test('timing, weather, and reserve variation are deterministic and recorded', () => {
  const seed = normalizeSeed(baseSeed({
    force_policy: { blue: { max_units: 2 } },
    variation: { time_offset_minutes: [-5, 5], sea_state_range: [2, 4], reserve_slots: { blue: [1, 1] } },
  }));
  const left = applyVariation(seed, createRng('variation'));
  const right = applyVariation(seed, createRng('variation'));
  assert.deepEqual(left, right);
  assert.equal(left.seed.force_policy.blue.max_units, 3);
  assert.ok(left.seed.sea_state >= 2 && left.seed.sea_state <= 4);
  assert.equal(shiftLocalDateTime('2026-05-22T14:00:00+04:00', 15), '2026-05-22T14:15:00.000+04:00');
});

test('eligibility excludes destroyed, incapable, and critically damaged units', () => {
  assert.equal(eligibility(baseUnit()).eligible, true);
  assert.equal(eligibility(baseUnit({ status: 'destroyed' })).eligible, false);
  assert.equal(eligibility(baseUnit({ mission_capable: false })).eligible, false);
  assert.equal(eligibility(baseUnit({ structural_integrity_pct: 29 })).eligible, false);
});

test('role inference covers campaign platform families', () => {
  assert.equal(inferRole(baseUnit({ platform_class: 'Fort Victoria AOR' }), 'ship'), 'logistics');
  assert.equal(inferRole(baseUnit({ platform_class: 'KC-135R' }), 'air'), 'tanker');
  assert.equal(inferRole(baseUnit({ platform_class: 'K-300P Bastion-P' }), 'ground'), 'coastal_strike');
});

test('ammunition scaling is bounded and deterministic', () => {
  assert.equal(scaledQuantity(16, 50), 8);
  assert.equal(scaledQuantity(1, 1), 1);
  assert.equal(scaledQuantity(16, 0), 0);
});

test('campaign speed limits cap mission speed', () => {
  const unit = { domain: 'ship', platform: { maxSpeedKts: 35 }, speed_limit_kts: 12 };
  assert.equal(missionSpeed(unit), 12);
});

test('package budgets and aviation recovery are enforced', () => {
  const unit = plannedUnit({ logistics: { daily_upkeep_points: 5 }, sorties: 2 });
  assert.throws(() => validatePackageBudget('blue', [unit], { fuel_points: 1 }), /exceeds campaign logistics/);
  const aircraft = plannedUnit({ domain: 'air', role: 'fighter' });
  assert.throws(() => validateAviationSupport('blue', [aircraft], {}, 6), /require explicit/);
  assert.equal(validateAviationSupport('blue', [aircraft], {
    mode: 'off_map', location: 'Base', reason: 'Outside tactical area',
  }, 6).mode, 'off_map');
});

test('all seven archetypes are registered', () => {
  assert.equal(Object.keys(ARCHETYPES).length, 7);
  for (const name of Object.keys(ARCHETYPES)) assert.equal(getArchetype(name).id, name);
});

test('objective quantities cannot exceed target count', () => {
  assert.equal(boundedQuantity(undefined, ['a', 'b', 'c'], 0.5), 2);
  assert.throws(() => boundedQuantity(4, ['a', 'b'], 0.5), /invalid/);
});

test('objective composition uses only approved goal types', () => {
  const blue = [plannedUnit({ unit_name: 'Convoy', role: 'logistics' })];
  const red = [plannedUnit({ unit_name: 'Raider', side: 'red', role: 'surface_combatant' })];
  const objectives = buildObjectives({ blue, red }, normalizeSeed(baseSeed()), getArchetype('convoy_escort'));
  assertApprovedGoals(objectives.blue);
  assertApprovedGoals(objectives.red);
});

test('placement jitter and air boxes are deterministic', () => {
  const left = createRng('place');
  const right = createRng('place');
  assert.deepEqual(jitterPoint({ lat: 25, lon: 57 }, 2, left, 'p'), jitterPoint({ lat: 25, lon: 57 }, 2, right, 'p'));
  assert.deepEqual(pointFromBox(baseSeed().placement.air_boxes.blue, left, 'air'), pointFromBox(baseSeed().placement.air_boxes.blue, right, 'air'));
});

test('placement fails instead of inventing a missing ground location', () => {
  const ground = plannedUnit({ unit_name: 'Ground Node', domain: 'ground', role: 'air_defense' });
  assert.throws(() => placeUnits({ blue: [ground], red: [], rejected: [] }, baseSeed(), createRng('x')), /No valid ground position/);
});

test('named loadout selection sets the default while explicit overrides retain priority', () => {
  const database = {
    defaultLoadout: () => ({ setupName: 'default', launchers: [{ launcherId: 0, item: 'Default Missile', quantity: 2 }], magazines: [] }),
    namedLoadout: (_className, _year, name) => ({
      setupName: name,
      launchers: [{ launcherId: 0, item: 'Named Missile', quantity: 4 }],
      magazines: [{ magazineId: 0, item: 'Named Reload', quantity: 8 }],
    }),
    validateLoadout: (_className, launchers) => launchers,
  };
  const aircraft = { ...baseUnit({ platform_class: 'Test Aircraft' }), domain: 'air', role: 'fighter', platform: { maxSpeedKts: 500 } };
  const named = planUnit(aircraft, database, 2026, null, 'fleet defense');
  assert.equal(named.loadoutSetup, 'fleet defense');
  assert.equal(named.launchers[0].item, 'Named Missile');
  assert.equal(named.magazines[0].item, 'Named Reload');
  const overridden = planUnit(aircraft, database, 2026, [{ launcherId: 0, item: 'Override Missile', quantity: 1 }], 'fleet defense');
  assert.equal(overridden.loadoutSetup, 'scenario-seed override');
  assert.equal(overridden.launchers[0].item, 'Override Missile');
});

test('host magazines cover every known loadout for every staged aircraft', () => {
  assert.deepEqual([...loadoutItemMaximums([
    { launchers: [{ item: 'A', quantity: 2 }, { item: 'A', quantity: 1 }] },
    { launchers: [{ item: 'A', quantity: 1 }, { item: 'B', quantity: 4 }] },
  ])], [['A', 3], ['B', 4]]);
  const carrier = plannedUnit({ unit_name: 'Carrier', role: 'base', ammo_pct: 100, magazines: [{ magazineId: 0, item: 'Fuel', quantity: 100 }] });
  const aircraft = ['Tiger 1', 'Tiger 2'].map((unit_name) => plannedUnit({
    unit_name, platform_class: 'Test Aircraft', domain: 'air', role: 'fighter', presence: 'staged', host: 'Carrier',
    loadoutSetup: 'default', launchers: [{ launcherId: 0, item: 'A', quantity: 1 }],
  }));
  const database = {
    availableLoadouts: () => [
      { setupName: 'air-to-air', launchers: [{ item: 'A', quantity: 3 }] },
      { setupName: 'strike', launchers: [{ item: 'B', quantity: 4 }] },
    ],
    validateLoadout: (_className, launchers) => launchers,
  };
  const units = stockAviationMagazines({ blue: [carrier, ...aircraft], red: [], rejected: [] }, database, '2026-01-01T00:00:00Z');
  const stores = Object.fromEntries(units.blue[0].magazines.map((entry) => [entry.item, entry.quantity]));
  assert.deepEqual(stores, { A: 6, B: 8, Fuel: 100 });
  assert.deepEqual(units.blue[0].aviationMagazine.catalog[0].loadouts, ['air-to-air', 'strike']);
});

test('objective composition supports independent named destruction groups', () => {
  const blue = [plannedUnit({ unit_name: 'Convoy', role: 'logistics' })];
  const red = [
    plannedUnit({ unit_name: 'Picket', side: 'red', role: 'surface_combatant' }),
    plannedUnit({ unit_name: 'Battery', side: 'red', role: 'coastal_strike' }),
  ];
  const seed = normalizeSeed(baseSeed({ objectives: {
    protect: { blue: ['Convoy'] }, protect_quantity: { blue: 1 },
    destroy_groups: { blue: [
      { targets: ['Picket'], quantity: 1 },
      { targets: ['Battery'], quantity: 1 },
    ] },
    destroy_quantity: { red: 1 },
  } }));
  const objectives = buildObjectives({ blue, red }, seed, getArchetype('convoy_escort'));
  assert.equal(objectives.blue.goals.length, 3);
  assertApprovedGoals(objectives.blue);
});

test('per-unit placement and staged aircraft directives override generic placement', () => {
  const ship = plannedUnit({ unit_name: 'Escort' });
  const carrier = plannedUnit({ unit_name: 'Carrier', role: 'base' });
  const aircraft = plannedUnit({ unit_name: 'Tiger 1', domain: 'air', role: 'fighter' });
  const seed = baseSeed({
    unit_directives: { blue: { 'Tiger 1': { presence: 'staged', host: 'Carrier', flight_deck_location: 2 } }, red: {} },
    placement: {
      ...baseSeed().placement,
      unit_positions: { blue: { Escort: { lat: 25.6, lon: 57.7 }, Carrier: { lat: 25.4, lon: 58.0 } } },
      unit_routes: { blue: { Escort: [{ lat: 25.8, lon: 57.2 }] } },
    },
  });
  const placed = placeUnits({ blue: [ship, carrier, aircraft], red: [], rejected: [] }, seed, createRng('directives'));
  assert.deepEqual(placed.blue[0].position, { lat: 25.6, lon: 57.7, altitude: 0 });
  assert.equal(placed.blue[2].presence, 'staged');
  assert.equal(placed.blue[2].host, 'Carrier');
});

test('balance scoring accounts for condition and reports extreme ratios', () => {
  const healthy = plannedUnit();
  const weak = plannedUnit({ side: 'red', readiness_pct: 20, structural_integrity_pct: 30, fuelFraction: 0.2, ammo_pct: 10 });
  assert.ok(scoreUnit(healthy) > scoreUnit(weak));
  const result = assessBalance({ blue: [healthy, healthy], red: [weak] }, {
    blue: { type: 'DestroyGoal', targets: ['r'], quantity: 1 },
    red: { type: 'DestroyGoal', targets: ['b'], quantity: 1 },
  });
  assert.ok(result.warnings.length);
});

test('renderer emits current coordinates, persistence controls, and approved goals', () => {
  const blue = plannedUnit({ unit_name: 'Convoy', role: 'logistics' });
  const red = plannedUnit({ unit_name: 'Raider', side: 'red' });
  const model = {
    state: { turn: 2 }, seed: normalizeSeed(baseSeed()), effectiveSeed: 'test', archetype: getArchetype('convoy_escort'),
    units: { blue: [blue], red: [red] },
    objectives: {
      blue: { type: 'ProtectGoal', targets: ['Convoy'], quantity: 1 },
      red: { type: 'DestroyGoal', targets: ['Convoy'], quantity: 1 },
    },
    balance: { ratio: 1 },
  };
  const source = renderScenario(model);
  assert.match(source, /# Scenario version: 0\.2\.1/);
  assert.match(source, /SetFuelFraction\(0\.750000\)/);
  assert.doesNotMatch(source, /TimeGoal/);
});

test('renderer emits staged aircraft after their active host', () => {
  const carrier = plannedUnit({ unit_name: 'Carrier', role: 'base', presence: 'active' });
  const tiger = plannedUnit({ unit_name: 'Tiger 1', domain: 'air', role: 'fighter', presence: 'staged', host: 'Carrier', flightDeckLocation: 2 });
  const red = plannedUnit({ unit_name: 'Raider', side: 'red', presence: 'active' });
  const model = {
    state: { turn: 2 }, seed: normalizeSeed(baseSeed()), effectiveSeed: 'test', archetype: getArchetype('convoy_escort'),
    units: { blue: [tiger, carrier], red: [red] },
    objectives: { blue: { type: 'ProtectGoal', targets: ['Carrier'], quantity: 1 }, red: { type: 'DestroyGoal', targets: ['Carrier'], quantity: 1 } },
    balance: { ratio: 1 },
  };
  const source = renderScenario(model);
  assert.match(source, /AddUnitToFlightDeck\("Carrier", "Test Ship", "Tiger 1", 2\)/);
  assert.ok(source.indexOf('unit.unitName = "Carrier"') < source.indexOf('AddUnitToFlightDeck'));
});

test('continuity assertions enforce presence, losses, tasking, ammunition, and unique surface routes', () => {
  const blue = plannedUnit({ unit_name: 'Lancer 1', domain: 'air', role: 'strike', presence: 'active', tasks: ['Aircraft1', 'Nav'] });
  const red = plannedUnit({ unit_name: 'Khanjar', side: 'red', presence: 'active', route: [{ lat: 26.4, lon: 56.4 }], launchers: [{ launcherId: 2, item: '76mm', quantity: 1 }] });
  const units = { blue: [blue], red: [red], rejected: [{ side: 'blue', unit_name: 'Wildcat 2', reasons: ['destroyed'] }] };
  assert.equal(validateContinuity(units, {
    required_counts: { blue: 1, red: 1 },
    required_selected: { red: ['Khanjar'] }, required_rejected: { blue: ['Wildcat 2'] },
    required_presence: { blue: { 'Lancer 1': 'active' } }, forbidden_tasks: { 'Lancer 1': ['AutoAttack'] },
    required_loadout_totals: { Khanjar: { '76mm': 1 } }, unique_surface_waypoints: true,
  }).passed, true);
  assert.throws(() => validateContinuity(units, { required_counts: { red: 2 } }), /assertions failed/);
});
