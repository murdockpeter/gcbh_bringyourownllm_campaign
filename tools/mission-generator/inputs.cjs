'use strict';

const fs = require('node:fs');
const { GeneratorError } = require('./errors.cjs');
const { canonicalize, hashValue } = require('./rng.cjs');

const ARCHETYPES = new Set([
  'convoy_escort', 'withdrawal', 'corridor_opening', 'interception',
  'limited_strike', 'reconnaissance', 'recovery',
]);
const STATUSES = new Set(['operational', 'damaged', 'under_repair', 'destroyed']);
const PRESENCE_STATES = new Set(['active', 'reserve', 'staged', 'maintenance']);

function readJson(filePath, label) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (error) {
    throw new GeneratorError('INPUT_READ', `Could not read ${label}: ${filePath}`, error.message);
  }
}

function assertObject(value, path, errors) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    errors.push(`${path} must be an object`);
    return false;
  }
  return true;
}

function assertPercent(value, path, errors) {
  if (!Number.isFinite(value) || value < 0 || value > 100) errors.push(`${path} must be between 0 and 100`);
}

function normalizeUnit(unit, side, index, errors) {
  const path = `sides.${side}.units[${index}]`;
  if (!assertObject(unit, path, errors)) return null;
  for (const key of ['unit_name', 'platform_class', 'status']) {
    if (typeof unit[key] !== 'string' || !unit[key].trim()) errors.push(`${path}.${key} must be a non-empty string`);
  }
  if (!STATUSES.has(unit.status)) errors.push(`${path}.status is unsupported: ${unit.status}`);
  if (typeof unit.mission_capable !== 'boolean') errors.push(`${path}.mission_capable must be boolean`);
  for (const key of ['structural_integrity_pct', 'readiness_pct', 'crew_fatigue_pct', 'fuel_pct', 'ammo_pct']) {
    assertPercent(unit[key], `${path}.${key}`, errors);
  }
  if (!Number.isFinite(unit.speed_limit_kts) || unit.speed_limit_kts < 0) errors.push(`${path}.speed_limit_kts must be non-negative`);
  return canonicalize({ ...unit, side });
}

function normalizeState(raw) {
  const errors = [];
  if (!assertObject(raw, 'campaign state', errors)) throw new GeneratorError('STATE_INVALID', 'Campaign state is invalid', errors);
  for (const key of ['campaign_id', 'campaign_name', 'version', 'current_time_local', 'turn', 'sides']) {
    if (raw[key] === undefined || raw[key] === null || raw[key] === '') errors.push(`campaign state.${key} is required`);
  }
  if (!assertObject(raw.sides, 'sides', errors)) throw new GeneratorError('STATE_INVALID', 'Campaign state is invalid', errors);
  const sides = {};
  const identities = new Set();
  for (const side of ['blue', 'red']) {
    const source = raw.sides?.[side];
    if (!assertObject(source, `sides.${side}`, errors) || !Array.isArray(source.units)) {
      errors.push(`sides.${side}.units must be an array`);
      continue;
    }
    const units = source.units.map((unit, index) => normalizeUnit(unit, side, index, errors)).filter(Boolean);
    for (const unit of units) {
      const identity = `${side}:${unit.unit_name.toLowerCase()}`;
      if (identities.has(identity)) errors.push(`Duplicate unit identity: ${side}/${unit.unit_name}`);
      identities.add(identity);
    }
    sides[side] = canonicalize({ ...source, units });
  }
  if (errors.length) throw new GeneratorError('STATE_INVALID', 'Campaign state validation failed', errors);
  return canonicalize({ ...raw, sides });
}

function rejectUnknown(object, allowed, path, errors) {
  for (const key of Object.keys(object)) if (!allowed.has(key)) errors.push(`${path}.${key} is not supported by schema version 1`);
}

function validateLauncherList(value, path, errors) {
  if (!Array.isArray(value) || !value.length) {
    errors.push(`${path} must be a non-empty launcher array`);
    return;
  }
  value.forEach((launcher, index) => {
    const itemPath = `${path}[${index}]`;
    if (!assertObject(launcher, itemPath, errors)) return;
    rejectUnknown(launcher, new Set(['launcherId', 'item', 'quantity']), itemPath, errors);
    if (!Number.isInteger(launcher.launcherId) || launcher.launcherId < 0) errors.push(`${itemPath}.launcherId must be a non-negative integer`);
    if (typeof launcher.item !== 'string' || !launcher.item.trim()) errors.push(`${itemPath}.item must be a non-empty string`);
    if (!Number.isInteger(launcher.quantity) || launcher.quantity < 1) errors.push(`${itemPath}.quantity must be a positive integer`);
  });
}

function normalizeSeed(raw) {
  const errors = [];
  if (!assertObject(raw, 'scenario seed', errors)) throw new GeneratorError('SEED_INVALID', 'Scenario seed is invalid', errors);
  rejectUnknown(raw, new Set([
    'schema_version', 'scenario_id', 'scenario_name', 'theater_id', 'date_time', 'playable_side',
    'rng_seed', 'archetype', 'premise', 'blue_intent', 'red_intent', 'escalation_constraints',
    'duration_hours', 'force_policy', 'objectives', 'placement', 'variation', 'sea_state', 'svp',
    'loadout_overrides', 'loadout_selections', 'loadout_presets', 'aviation_support',
    'unit_directives',
    'continuity_assertions',
  ]), 'scenario seed', errors);
  for (const key of ['schema_version', 'scenario_id', 'scenario_name', 'theater_id', 'date_time', 'playable_side', 'archetype', 'premise', 'placement']) {
    if (raw[key] === undefined || raw[key] === null || raw[key] === '') errors.push(`scenario seed.${key} is required`);
  }
  if (raw.schema_version !== 1) errors.push('scenario seed.schema_version must be 1');
  if (!ARCHETYPES.has(raw.archetype)) errors.push(`scenario seed.archetype is unsupported: ${raw.archetype}`);
  if (!['blue', 'red'].includes(raw.playable_side)) errors.push('scenario seed.playable_side must be blue or red');
  if (Number.isNaN(Date.parse(raw.date_time))) errors.push('scenario seed.date_time must be an ISO 8601 date-time');
  if (raw.duration_hours !== undefined && (!Number.isFinite(raw.duration_hours) || raw.duration_hours <= 0)) errors.push('scenario seed.duration_hours must be positive');
  if (raw.sea_state !== undefined && (!Number.isInteger(raw.sea_state) || raw.sea_state < 0 || raw.sea_state > 9)) errors.push('scenario seed.sea_state must be an integer from 0 to 9');
  if (!assertObject(raw.placement, 'scenario seed.placement', errors)) errors.push('scenario seed.placement is required');
  if (raw.loadout_overrides !== undefined && assertObject(raw.loadout_overrides, 'scenario seed.loadout_overrides', errors)) {
    for (const [name, launchers] of Object.entries(raw.loadout_overrides)) validateLauncherList(launchers, `scenario seed.loadout_overrides.${name}`, errors);
  }
  if (raw.loadout_selections !== undefined && assertObject(raw.loadout_selections, 'scenario seed.loadout_selections', errors)) {
    for (const [name, selection] of Object.entries(raw.loadout_selections)) {
      if (typeof selection !== 'string' || !selection.trim()) errors.push(`scenario seed.loadout_selections.${name} must be a non-empty string`);
    }
  }
  if (raw.loadout_presets !== undefined && assertObject(raw.loadout_presets, 'scenario seed.loadout_presets', errors)) {
    for (const [className, presets] of Object.entries(raw.loadout_presets)) {
      const classPath = `scenario seed.loadout_presets.${className}`;
      if (!assertObject(presets, classPath, errors)) continue;
      for (const [presetName, launchers] of Object.entries(presets)) validateLauncherList(launchers, `${classPath}.${presetName}`, errors);
    }
  }
  if (raw.unit_directives !== undefined && assertObject(raw.unit_directives, 'scenario seed.unit_directives', errors)) {
    for (const side of ['blue', 'red']) {
      const directives = raw.unit_directives[side] || {};
      if (!assertObject(directives, `scenario seed.unit_directives.${side}`, errors)) continue;
      for (const [name, directive] of Object.entries(directives)) {
        const path = `scenario seed.unit_directives.${side}.${name}`;
        if (!assertObject(directive, path, errors)) continue;
        if (directive.presence !== undefined && !PRESENCE_STATES.has(directive.presence)) errors.push(`${path}.presence is unsupported: ${directive.presence}`);
        if (['staged', 'maintenance'].includes(directive.presence) && (typeof directive.host !== 'string' || !directive.host.trim())) errors.push(`${path}.host is required for ${directive.presence} aircraft`);
        if (directive.flight_deck_location !== undefined && ![1, 2, 3].includes(directive.flight_deck_location)) errors.push(`${path}.flight_deck_location must be 1, 2, or 3`);
        if (directive.tasks !== undefined && (!Array.isArray(directive.tasks) || directive.tasks.some((task) => typeof task !== 'string' || !task.trim()))) errors.push(`${path}.tasks must contain non-empty strings`);
      }
    }
  }
  if (errors.length) throw new GeneratorError('SEED_INVALID', 'Scenario seed validation failed', errors);
  return canonicalize({
    duration_hours: 6,
    force_policy: {},
    objectives: {},
    variation: {},
    loadout_overrides: {},
    loadout_selections: {},
    loadout_presets: {},
    aviation_support: {},
    unit_directives: { blue: {}, red: {} },
    continuity_assertions: {},
    sea_state: 3,
    svp: '0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000',
    escalation_constraints: [],
    blue_intent: '',
    red_intent: '',
    ...raw,
  });
}

function loadInputs(statePath, seedPath) {
  const state = normalizeState(readJson(statePath, 'campaign state'));
  const seed = normalizeSeed(readJson(seedPath, 'scenario seed'));
  return {
    state,
    seed,
    hashes: { campaign_state: hashValue(state), scenario_seed: hashValue(seed) },
  };
}

module.exports = { ARCHETYPES, PRESENCE_STATES, readJson, normalizeState, normalizeSeed, loadInputs };
