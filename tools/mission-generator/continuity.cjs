'use strict';

const { GeneratorError } = require('./errors.cjs');

function validateContinuity(units, assertions = {}) {
  const errors = [];
  const selected = { blue: new Map(units.blue.map((unit) => [unit.unit_name, unit])), red: new Map(units.red.map((unit) => [unit.unit_name, unit])) };
  const rejected = new Set((units.rejected || []).map((unit) => `${unit.side}:${unit.unit_name}`));
  for (const side of ['blue', 'red']) {
    const expectedCount = assertions.required_counts?.[side];
    if (expectedCount !== undefined && selected[side].size !== expectedCount) errors.push(`${side} selected count is ${selected[side].size}; expected ${expectedCount}`);
    for (const name of assertions.required_selected?.[side] || []) if (!selected[side].has(name)) errors.push(`${side}/${name} is required but was not selected`);
    for (const name of assertions.required_rejected?.[side] || []) if (!rejected.has(`${side}:${name}`)) errors.push(`${side}/${name} is required to remain rejected`);
    for (const [name, presence] of Object.entries(assertions.required_presence?.[side] || {})) {
      const unit = selected[side].get(name);
      if (!unit) errors.push(`${side}/${name} has a presence assertion but was not selected`);
      else if (unit.presence !== presence) errors.push(`${side}/${name} presence is ${unit.presence}; expected ${presence}`);
    }
  }
  for (const [name, forbidden] of Object.entries(assertions.forbidden_tasks || {})) {
    const unit = [...selected.blue.values(), ...selected.red.values()].find((candidate) => candidate.unit_name === name);
    if (!unit) errors.push(`${name} has a task assertion but was not selected`);
    else for (const task of forbidden) if (unit.tasks.includes(task)) errors.push(`${name} contains forbidden task ${task}`);
  }
  for (const [name, expectedItems] of Object.entries(assertions.required_loadout_totals || {})) {
    const unit = [...selected.blue.values(), ...selected.red.values()].find((candidate) => candidate.unit_name === name);
    if (!unit) {
      errors.push(`${name} has a loadout assertion but was not selected`);
      continue;
    }
    for (const [item, expected] of Object.entries(expectedItems)) {
      const actual = unit.launchers.filter((launcher) => launcher.item === item).reduce((sum, launcher) => sum + launcher.quantity, 0);
      if (actual !== expected) errors.push(`${name} carries ${actual} ${item}; expected ${expected}`);
    }
  }
  if (assertions.unique_surface_waypoints) {
    for (const side of ['blue', 'red']) {
      const seen = new Map();
      for (const unit of selected[side].values()) {
        if (!['ship', 'sub'].includes(unit.domain)) continue;
        for (const point of unit.route) {
          const key = `${point.lat.toFixed(6)},${point.lon.toFixed(6)}`;
          const previous = seen.get(key);
          if (previous && previous !== unit.unit_name) errors.push(`${side} surface waypoint ${key} is shared by ${previous} and ${unit.unit_name}`);
          else seen.set(key, unit.unit_name);
        }
      }
    }
  }
  if (errors.length) throw new GeneratorError('CONTINUITY_ASSERTION', 'Campaign continuity assertions failed', errors);
  return { passed: true, assertions };
}

module.exports = { validateContinuity };
