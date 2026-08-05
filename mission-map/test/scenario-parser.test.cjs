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
    UI.AddTask('Ship1', 2.0, 3)
    UI.add_waypoint_advanced(26.2, 57.0, 0, 12)
  `);
  assert.equal(parsed.units[0].allianceName, 'Blue');
  assert.equal(parsed.units[0].domain, 'surface');
  assert.equal(parsed.units[0].waypoints.length, 1);
});
