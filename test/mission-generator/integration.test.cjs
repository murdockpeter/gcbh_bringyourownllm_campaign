'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const test = require('node:test');
const { defaultDatabasePath, GameDatabase } = require('../../tools/mission-generator/database.cjs');
const { generateMission } = require('../../tools/mission-generator/generate.cjs');

const projectRoot = path.resolve(__dirname, '..', '..');
const databasePath = defaultDatabasePath();
const hasDatabase = fs.existsSync(databasePath);

test('opens the game database read-only and resolves campaign classes/loadouts', { skip: !hasDatabase }, () => {
  const database = new GameDatabase(databasePath);
  try {
    assert.ok(database.schemaVersion >= 2);
    assert.equal(database.platform('Arleigh Burke IIA DDGHM').domain, 'ship');
    const loadout = database.defaultLoadout('Arleigh Burke IIA DDGHM', 2026).launchers;
    assert.ok(loadout.length);
    assert.equal(new Set(loadout.map((launcher) => launcher.launcherId)).size, loadout.length);
    assert.throws(() => database.validateLoadout('F-15E', [{ launcherId: 999, item: 'Imaginary', quantity: 1 }]), /invalid/);
  } finally {
    database.close();
  }
});

test('three archetype fixtures generate distinct, deterministic, audit-clean missions', { skip: !hasDatabase, timeout: 60000 }, async () => {
  const temporaryRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'gcbh-generator-'));
  const statePath = path.join(projectRoot, 'campaign', 'campaign_state_mvp.json');
  const baseSeed = JSON.parse(fs.readFileSync(path.join(projectRoot, 'campaign', 'next_scenario_seed_mvp.json'), 'utf8'));
  const variants = [
    { name: 'convoy_escort', mutate: () => {} },
    { name: 'withdrawal', mutate(seed) {
      seed.objectives.protect.blue = ['USS Mason'];
      seed.objectives.protect_quantity.blue = 1;
      seed.objectives.destroy.blue = ['Khanjar', 'Falakhon'];
      seed.objectives.destroy_quantity.blue = 1;
      seed.objectives.destroy_quantity.red = 1;
      seed.force_policy.blue.max_units = 10;
      seed.force_policy.red.max_units = 6;
      seed.placement.surface_routes.blue = seed.placement.surface_routes.blue.slice(0, 4);
    } },
    { name: 'limited_strike', mutate(seed) {
      seed.objectives.protect.blue = ['Lancer Flight'];
      seed.objectives.protect_quantity.blue = 1;
      seed.objectives.destroy.blue = ['Bastion 1', 'Bastion 2', 'S-300 Site North'];
      seed.objectives.destroy_quantity.blue = 2;
      seed.objectives.destroy_quantity.red = 1;
      seed.force_policy.blue.max_units = 9;
      seed.force_policy.red.max_units = 8;
      seed.placement.air_boxes.blue = { south: 24.8, north: 25.4, west: 55.0, east: 56.0, altitude: 7600 };
    } },
  ];
  const sources = [];
  for (const variant of variants) {
    const seed = structuredClone(baseSeed);
    seed.archetype = variant.name;
    seed.scenario_id = `fixture_${variant.name}`;
    seed.scenario_name = `Fixture ${variant.name}`;
    variant.mutate(seed);
    const seedPath = path.join(temporaryRoot, `${variant.name}.json`);
    fs.writeFileSync(seedPath, `${JSON.stringify(seed, null, 2)}\n`);
    const outputPath = path.join(temporaryRoot, `${variant.name}.py`);
    const manifestPath = path.join(temporaryRoot, `${variant.name}.manifest.json`);
    await generateMission({ statePath, seedPath, databasePath, outputPath, manifestPath, rngSeed: `fixture-${variant.name}` });
    const firstSource = fs.readFileSync(outputPath, 'utf8');
    const firstManifest = fs.readFileSync(manifestPath, 'utf8');
    await generateMission({ statePath, seedPath, databasePath, outputPath, manifestPath, rngSeed: `fixture-${variant.name}` });
    assert.equal(fs.readFileSync(outputPath, 'utf8'), firstSource);
    assert.equal(fs.readFileSync(manifestPath, 'utf8'), firstManifest);
    assert.doesNotMatch(firstSource, /TimeGoal/);
    assert.equal(JSON.parse(firstManifest).validation.errors, 0);
    assert.ok(JSON.parse(firstManifest).rejected_units.some((unit) => unit.reasons.some((reason) => /destroyed|mission_capable/.test(reason))));
    sources.push(firstSource);
  }
  assert.equal(new Set(sources).size, 3);
});

test('unsatisfiable objectives fail without creating partial output', { skip: !hasDatabase, timeout: 30000 }, async () => {
  const temporaryRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'gcbh-generator-failure-'));
  const statePath = path.join(projectRoot, 'campaign', 'campaign_state_mvp.json');
  const seed = JSON.parse(fs.readFileSync(path.join(projectRoot, 'campaign', 'next_scenario_seed_mvp.json'), 'utf8'));
  seed.objectives.protect.blue = ['Destroyed Ship That Cannot Exist'];
  const seedPath = path.join(temporaryRoot, 'bad-seed.json');
  const outputPath = path.join(temporaryRoot, 'should-not-exist.py');
  const manifestPath = path.join(temporaryRoot, 'should-not-exist.json');
  fs.writeFileSync(seedPath, `${JSON.stringify(seed, null, 2)}\n`);
  await assert.rejects(generateMission({ statePath, seedPath, databasePath, outputPath, manifestPath }), /Required blue units are unavailable/);
  assert.equal(fs.existsSync(outputPath), false);
  assert.equal(fs.existsSync(manifestPath), false);
});
