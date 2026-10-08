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
    const hornetLoadouts = database.availableLoadouts('F/A-18F', 2026);
    assert.ok(hornetLoadouts.length > 1);
    assert.equal(database.namedLoadout('F/A-18F', 2026, 'SM1').setupName.trim().replace(/\s+/g, ' '), 'SM1 2010');
    assert.throws(() => database.namedLoadout('F/A-18F', 2026, 'not-a-loadout'), /not available/);
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

test('Baltic operational references and route library pass mask and coastline checks', async () => {
  const geometry = await import('../../mission-map/renderer/geometry.js');
  const read = (name) => JSON.parse(fs.readFileSync(path.join(projectRoot, name), 'utf8'));
  const theater = read('theaters/baltic_latvia_estonia.json');
  const area = read('campaign/baltic_operational_area.json');
  const land = geometry.buildLandIndex(read('mission-map/renderer/data/global-land.geojson'));
  const { selectTheater } = require('../../mission-map/src/theater-selector.cjs');
  assert.equal(selectTheater({ theaterCenter: { lat: 57.4, lng: 24 } }, [read('theaters/hormuz_mvp.json'), theater]).theater_id, theater.theater_id);
  for (const node of area.ground_reference_nodes) assert.ok(geometry.pointInLand({ lat: node.lat, lng: node.lon }, land), node.id);
  for (const [name, route] of Object.entries(area.surface_route_library)) {
    const points = route.map((p) => ({ ...p, lng: p.lon }));
    const scenario = { units: [{ name, className: 'Sachsen FFGHM', domain: 'surface', position: points[0], waypoints: points.slice(1) }] };
    assert.deepEqual(geometry.validateMission(scenario, theater, 1), [], name);
    assert.deepEqual(geometry.validateRealWorld(scenario, theater, land, 1), [], name);
  }
});

test('Baltic fixture generates deterministically with NATO/Russia and no audit findings', { skip: !hasDatabase, timeout: 60000 }, async (t) => {
  const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'gcbh-baltic-'));
  t.after(() => fs.rmSync(temporary, { recursive: true, force: true }));
  const options = { statePath: path.join(projectRoot, 'campaign/campaign_state_baltic_setup.json'), seedPath: path.join(projectRoot, 'campaign/scenario_seed_baltic_setup.json'), databasePath, outputPath: path.join(temporary, 'setup.py'), manifestPath: path.join(temporary, 'setup.json') };
  await generateMission(options);
  const source = fs.readFileSync(options.outputPath, 'utf8');
  const manifest = fs.readFileSync(options.manifestPath, 'utf8');
  assert.match(source, /CreateAlliance\(1, "NATO"\)/);
  assert.match(source, /AddAllianceCountry\(2, "Russia"\)/);
  assert.doesNotMatch(source, /Iran/);
  assert.equal(JSON.parse(manifest).validation.warnings, 0);
  await generateMission(options);
  assert.equal(fs.readFileSync(options.outputPath, 'utf8'), source);
  assert.equal(fs.readFileSync(options.manifestPath, 'utf8'), manifest);
});

test('Baltic Shield preserves combined-arms forces, conventional loadouts and player-controlled strike aircraft', { skip: !hasDatabase, timeout: 60000 }, async (t) => {
  const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'gcbh-baltic-shield-'));
  t.after(() => {
    assert.ok(path.resolve(temporary).startsWith(path.resolve(os.tmpdir()) + path.sep));
    fs.rmSync(temporary, { recursive: true, force: true });
  });
  const options = { statePath: path.join(projectRoot, 'campaign/campaign_state_baltic_shield.json'), seedPath: path.join(projectRoot, 'campaign/scenario_seed_baltic_shield.json'), databasePath, outputPath: path.join(temporary, 'shield.py'), manifestPath: path.join(temporary, 'shield.json') };
  await generateMission(options);
  const manifest = JSON.parse(fs.readFileSync(options.manifestPath));
  assert.equal(manifest.validation.errors, 0);
  assert.equal(manifest.validation.warnings, 0);
  assert.equal(manifest.selected_units.filter(u => u.side === 'blue').length, 20);
  assert.equal(manifest.selected_units.filter(u => u.side === 'red').length, 16);
  for (const side of ['blue', 'red']) for (const domain of ['ship', 'air', 'ground']) assert.ok(manifest.selected_units.some(u => u.side === side && u.domain === domain));
  const aew = manifest.selected_units.find(u => u.unit_name === 'Magic AEW');
  assert.equal(aew.role, 'reconnaissance');
  const coastal = manifest.selected_units.find(u => u.unit_name === 'Russian Coastal Battery');
  assert.deepEqual(coastal.applied.launchers, [{ launcherId: 0, item: 'P-800 Oniks', quantity: 2 }]);
  for (const u of manifest.selected_units) {
    if (/Raven|Falcon|Seeker|Magic|Shell/.test(u.unit_name)) assert.ok(!u.applied.tasks.includes('AutoAttack'), u.unit_name);
    assert.ok(!u.applied.launchers.some(l => /TN-1000|nuclear|B61/i.test(l.item)), u.unit_name);
  }
  assert.deepEqual(manifest.objectives.blue.goals.map(g => g.quantity), [3, 2, 1]);
  const source = fs.readFileSync(options.outputPath, 'utf8');
  const provenance = fs.readFileSync(options.manifestPath, 'utf8');
  await generateMission(options);
  assert.equal(fs.readFileSync(options.outputPath, 'utf8'), source);
  assert.equal(fs.readFileSync(options.manifestPath, 'utf8'), provenance);
});
