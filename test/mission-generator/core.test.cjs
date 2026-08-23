'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { normalizeState, normalizeSeed } = require('../../tools/mission-generator/inputs.cjs');
const { createRng, hashValue } = require('../../tools/mission-generator/rng.cjs');
const { eligibility, inferRole } = require('../../tools/mission-generator/state.cjs');
const { scaledQuantity, missionSpeed, validatePackageBudget, validateAviationSupport } = require('../../tools/mission-generator/logistics.cjs');
const { ARCHETYPES, getArchetype } = require('../../tools/mission-generator/archetypes.cjs');
const { boundedQuantity, buildObjectives, assertApprovedGoals } = require('../../tools/mission-generator/objectives.cjs');
const { jitterPoint, pointFromBox, placeUnits } = require('../../tools/mission-generator/placement.cjs');
const { scoreUnit, assessBalance } = require('../../tools/mission-generator/balance.cjs');
const { renderScenario } = require('../../tools/mission-generator/renderer.cjs');
const { shiftLocalDateTime, applyVariation } = require('../../tools/mission-generator/variation.cjs');
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
