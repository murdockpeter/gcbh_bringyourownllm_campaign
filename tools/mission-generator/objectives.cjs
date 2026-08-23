'use strict';

const { GeneratorError } = require('./errors.cjs');

const APPROVED_GOALS = new Set(['ProtectGoal', 'DestroyGoal', 'CompoundGoal']);

function namesByRoles(units, roles) {
  const roleSet = new Set(roles);
  return units.filter((unit) => roleSet.has(unit.role)).map((unit) => unit.unit_name).sort();
}

function existingNames(units, requested, side, label) {
  const available = new Set(units.map((unit) => unit.unit_name));
  const missing = requested.filter((name) => !available.has(name));
  if (missing.length) throw new GeneratorError('OBJECTIVE_TARGET', `${label} references unavailable ${side} targets`, missing);
  return [...requested].sort();
}

function boundedQuantity(requested, targets, fallbackFraction) {
  if (!targets.length) return 0;
  const fallback = Math.max(1, Math.ceil(targets.length * fallbackFraction));
  const quantity = requested === undefined ? fallback : Number(requested);
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > targets.length) {
    throw new GeneratorError('OBJECTIVE_QUANTITY', `Objective quantity ${quantity} is invalid for ${targets.length} targets`);
  }
  return quantity;
}

function buildObjectives(units, seed, archetype) {
  const configuredProtect = seed.objectives?.protect?.blue || [];
  const protectTargets = configuredProtect.length
    ? existingNames(units.blue, configuredProtect, 'blue', 'Blue protection objective')
    : namesByRoles(units.blue, archetype.protectRoles);
  const configuredDestroy = seed.objectives?.destroy?.blue || [];
  const destroyTargets = configuredDestroy.length
    ? existingNames(units.red, configuredDestroy, 'red', 'Blue destruction objective')
    : namesByRoles(units.red, archetype.destroyRoles);
  if (!protectTargets.length && !destroyTargets.length) {
    throw new GeneratorError('OBJECTIVE_EMPTY', `${archetype.label} cannot construct a feasible objective from the selected roster`);
  }
  const blueChildren = [];
  if (protectTargets.length) blueChildren.push({
    type: 'ProtectGoal', targets: protectTargets,
    quantity: boundedQuantity(seed.objectives?.protect_quantity?.blue, protectTargets, 0.75),
    label: 'preserve campaign-critical assets',
  });
  if (destroyTargets.length) blueChildren.push({
    type: 'DestroyGoal', targets: destroyTargets,
    quantity: boundedQuantity(seed.objectives?.destroy_quantity?.blue, destroyTargets, 0.5),
    label: 'neutralize the designated threat',
  });
  const redTargets = protectTargets.length ? protectTargets : units.blue.filter((unit) => unit.role !== 'base').map((unit) => unit.unit_name).sort();
  if (!redTargets.length) throw new GeneratorError('OBJECTIVE_EMPTY', 'Red cannot construct a feasible opposing objective');
  const red = {
    type: 'DestroyGoal', targets: redTargets,
    quantity: boundedQuantity(seed.objectives?.destroy_quantity?.red, redTargets, 0.4),
    label: 'break the protected force',
  };
  const blue = blueChildren.length === 1 ? blueChildren[0] : { type: 'CompoundGoal', mode: 0, goals: blueChildren, label: archetype.label };
  return { blue, red };
}

function assertApprovedGoals(goal) {
  if (!APPROVED_GOALS.has(goal.type)) throw new GeneratorError('OBJECTIVE_TYPE', `Unsupported goal type: ${goal.type}`);
  for (const child of goal.goals || []) assertApprovedGoals(child);
}

module.exports = { APPROVED_GOALS, namesByRoles, boundedQuantity, buildObjectives, assertApprovedGoals };
