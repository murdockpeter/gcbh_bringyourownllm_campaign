'use strict';

const { canonicalize, hashValue } = require('./rng.cjs');

function unitDecision(unit) {
  return {
    side: unit.side,
    unit_name: unit.unit_name,
    platform_class: unit.platform_class,
    domain: unit.domain,
    role: unit.role,
    presence: unit.presence,
    host: unit.host,
    source_state: unit.persistence,
    applied: {
      speed_kts: unit.speed,
      fuel_fraction: unit.fuelFraction,
      sorties: unit.sorties,
      loadout_setup: unit.loadoutSetup,
      launchers: unit.launchers,
      magazines: unit.magazines,
      position: unit.position,
      route: unit.route,
      tasks: unit.tasks,
      always_visible: unit.alwaysVisible,
      flight_deck_location: unit.flightDeckLocation,
    },
  };
}

function buildManifest(model, context) {
  return canonicalize({
    schema_version: 1,
    generator: { name: 'mission-generator-v2', version: '0.2.0', node: '>=24', database_schema_version: context.databaseSchemaVersion },
    scenario: { id: model.seed.scenario_id, name: model.seed.scenario_name, archetype: model.archetype.id, theater_id: model.seed.theater_id },
    inputs: context.hashes,
    effective_rng_seed: model.effectiveSeed,
    variation: { configured: model.sourceSeed.variation, applied: model.variation },
    random_draws: context.draws,
    selected_units: [...model.units.blue, ...model.units.red].map(unitDecision),
    rejected_units: model.units.rejected,
    logistics: model.units.logistics,
    aviation_support: model.units.aviation,
    continuity: model.continuity,
    objectives: model.objectives,
    balance: model.balance,
    validation: context.validation,
    output_hash: context.outputHash,
  });
}

function finalizeManifest(model, context, source) {
  return buildManifest(model, { ...context, outputHash: hashValue(source) });
}

module.exports = { unitDecision, buildManifest, finalizeManifest };
