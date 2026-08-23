'use strict';

const { GeneratorError } = require('./errors.cjs');

function unitScore(unit, rng) {
  const base = unit.readiness_pct - unit.crew_fatigue_pct * 0.35 + unit.structural_integrity_pct * 0.25;
  return base + rng.next(`roster:${unit.side}:${unit.unit_name}`) * 0.001;
}

function selectSide(units, side, policy, protectedNames, rng) {
  const candidates = units.filter((unit) => unit.side === side);
  const excluded = new Set((policy.exclude || []).map((name) => name.toLowerCase()));
  const required = new Set([...(policy.require || []), ...protectedNames].map((name) => name.toLowerCase()));
  const filtered = candidates.filter((unit) => !excluded.has(unit.unit_name.toLowerCase()));
  const missing = [...required].filter((name) => !filtered.some((unit) => unit.unit_name.toLowerCase() === name));
  if (missing.length) throw new GeneratorError('ROSTER_REQUIRED', `Required ${side} units are unavailable`, missing);
  const maximum = policy.max_units === undefined ? filtered.length : Number(policy.max_units);
  if (!Number.isInteger(maximum) || maximum < required.size) throw new GeneratorError('ROSTER_POLICY', `${side}.max_units cannot satisfy required units`);
  return filtered
    .map((unit) => ({ unit, score: unitScore(unit, rng), required: required.has(unit.unit_name.toLowerCase()) }))
    .sort((left, right) => Number(right.required) - Number(left.required) || right.score - left.score || left.unit.unit_name.localeCompare(right.unit.unit_name))
    .slice(0, maximum)
    .map((entry) => entry.unit)
    .sort((left, right) => left.unit_name.localeCompare(right.unit_name));
}

function selectRoster(indexed, seed, rng) {
  const protectedBySide = seed.objectives?.protect || {};
  const destroyedBySide = seed.objectives?.destroy || {};
  const blueRequired = [...(protectedBySide.blue || []), ...(destroyedBySide.red || [])];
  const redRequired = [...(protectedBySide.red || []), ...(destroyedBySide.blue || [])];
  const blue = selectSide(indexed.accepted, 'blue', seed.force_policy?.blue || {}, blueRequired, rng);
  const red = selectSide(indexed.accepted, 'red', seed.force_policy?.red || {}, redRequired, rng);
  return { blue, red, rejected: indexed.rejected };
}

module.exports = { unitScore, selectRoster };
