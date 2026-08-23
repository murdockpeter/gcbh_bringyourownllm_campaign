'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { loadInputs } = require('./inputs.cjs');
const { createRng, canonicalJson, hashValue } = require('./rng.cjs');
const { GameDatabase, defaultDatabasePath } = require('./database.cjs');
const { indexCampaign } = require('./state.cjs');
const { selectRoster } = require('./roster.cjs');
const { applyLogistics } = require('./logistics.cjs');
const { getArchetype } = require('./archetypes.cjs');
const { buildObjectives } = require('./objectives.cjs');
const { placeUnits } = require('./placement.cjs');
const { assessBalance } = require('./balance.cjs');
const { renderScenario } = require('./renderer.cjs');
const { finalizeManifest } = require('./manifest.cjs');
const { validateOutput } = require('./validate-output.cjs');
const { applyVariation } = require('./variation.cjs');
const { validateContinuity } = require('./continuity.cjs');

function atomicWrite(filePath, contents) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  const temporary = `${filePath}.tmp-${process.pid}`;
  try {
    fs.writeFileSync(temporary, contents, 'utf8');
    fs.renameSync(temporary, filePath);
  } finally {
    if (fs.existsSync(temporary)) fs.unlinkSync(temporary);
  }
}

async function generateMission(options) {
  const inputs = loadInputs(options.statePath, options.seedPath);
  const effectiveSeed = String(options.rngSeed ?? inputs.seed.rng_seed ?? hashValue({ state: inputs.state, seed: inputs.seed }).slice(0, 16));
  const rng = createRng(effectiveSeed);
  const variation = applyVariation(inputs.seed, rng);
  const seed = variation.seed;
  const database = new GameDatabase(options.databasePath || defaultDatabasePath());
  try {
    const indexed = indexCampaign(inputs.state, database);
    const roster = selectRoster(indexed, seed, rng);
    const supplied = applyLogistics(
      roster, database, seed.date_time, seed.loadout_overrides,
      inputs.state.sides, seed.aviation_support, seed.duration_hours,
    );
    const archetype = getArchetype(seed.archetype);
    const objectives = buildObjectives(supplied, seed, archetype);
    const units = placeUnits(supplied, seed, rng);
    const continuity = validateContinuity(units, seed.continuity_assertions);
    const balance = assessBalance(units, objectives);
    const model = { state: inputs.state, seed, sourceSeed: inputs.seed, variation: variation.applied, effectiveSeed, archetype, objectives, units, continuity, balance };
    const source = renderScenario(model);
    const validation = await validateOutput(source, options.outputPath, seed.theater_id);
    const manifest = finalizeManifest(model, {
      hashes: inputs.hashes,
      draws: rng.draws,
      databaseSchemaVersion: database.schemaVersion,
      validation,
    }, source);
    const manifestSource = `${JSON.stringify(manifest, null, 2)}\n`;
    atomicWrite(options.outputPath, source);
    atomicWrite(options.manifestPath, manifestSource);
    return {
      outputPath: options.outputPath,
      manifestPath: options.manifestPath,
      unitCounts: { blue: units.blue.length, red: units.red.length },
      balance,
      sourceHash: hashValue(source),
      manifestHash: hashValue(canonicalJson(manifest)),
    };
  } finally {
    database.close();
  }
}

module.exports = { atomicWrite, generateMission };
