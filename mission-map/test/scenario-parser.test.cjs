'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const { parseScenario } = require('../src/scenario-parser.cjs');

const projectRoot = path.resolve(__dirname, '..', '..');

test('detects legacy longitude/latitude SetPosition order in Gate Latch', () => {
  const filePath = path.join(projectRoot, 'scenarios', 'operation_gate_latch.py');
  const parsed = parseScenario(fs.readFileSync(filePath, 'utf8'), filePath);
  assert.equal(parsed.coordinateConvention.order, 'lng-lat');
  assert.equal(parsed.info.name, 'Operation Gate Latch');
  assert.ok(parsed.units.length >= 8);
  assert.deepEqual(parsed.units[0].position, { lat: 25.98, lng: 57.22, altitude: 0, sourceLine: 68 });
  assert.equal(parsed.units[0].waypoints[0].lat, 26.02);
  assert.equal(parsed.units[0].waypoints[0].lng, 56.85);
});

test('honors version 0.2.1 latitude/longitude order in Iron Shelter', () => {
  const filePath = path.join(projectRoot, 'scenarios', 'operation_iron_shelter.py');
  const parsed = parseScenario(fs.readFileSync(filePath, 'utf8'), filePath);
  assert.equal(parsed.version, '0.2.1');
  assert.equal(parsed.coordinateConvention.order, 'lat-lng');
  assert.deepEqual(parsed.units[0].position, { lat: 25.98, lng: 57, altitude: 0, sourceLine: 77 });
});

test('captures alliances and routes on the active unit', () => {
  const parsed = parseScenario(`
# Scenario version: 0.2.1
def ScenarioInfo():
    d = dict()
    d['name'] = 'Test Mission'
    d['playableSides'] = 'Blue'
    return d
def CreateScenario(SM):
    SM.CreateAlliance(1, 'Blue')
    SM.SetStartTheater(56.8, 26.2)
    unit = SM.GetDefaultUnit()
    unit.className = 'Test Ship'
    unit.unitName = 'Alpha'
    unit.SetPosition(26.1, 56.9, 0)
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Test Missile', 4)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.add_waypoint_advanced(26.2, 57.0, 0, 12)
  `);
  assert.equal(parsed.units[0].allianceName, 'Blue');
  assert.equal(parsed.units[0].domain, 'surface');
  assert.equal(parsed.units[0].waypoints.length, 1);
  assert.deepEqual(parsed.units[0].tasks, ['Ship1', 'AutoAttack']);
  assert.deepEqual(
    { ...parsed.units[0].launcherItems[0], sourceLine: undefined },
    { launcherId: 2, item: 'Test Missile', quantity: 4, sourceLine: undefined },
  );
});

test('captures the official multiline SetUnitLauncherList syntax', () => {
  const parsed = parseScenario(`
# Scenario version: 0.2.1
def CreateScenario(SM):
    SM.CreateAlliance(1, 'Japan')
    unit = SM.GetDefaultUnit()
    unit.className = 'F-15JSI'
    unit.unitName = 'Eagle 11'
    unit.SetPosition(26.5, 126.5, 10000)
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherList(unit.unitName, [
        (0, 'AIM-120D', 4),
        (1, 'AIM-9X', 2),
    ])
    UI.AddTask('Aircraft1', 1.0, 0)
    UI.AddTask('AutoAttack', 2.0, 0)
  `);
  assert.deepEqual(
    parsed.units[0].launcherItems.map(({ launcherId, item, quantity }) => ({ launcherId, item, quantity })),
    [
      { launcherId: 0, item: 'AIM-120D', quantity: 4 },
      { launcherId: 1, item: 'AIM-9X', quantity: 2 },
    ],
  );
});
