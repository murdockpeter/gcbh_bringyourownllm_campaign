'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { applyScenarioEdits } = require('../src/scenario-editor.cjs');

test('updates current latitude/longitude positions and waypoints', () => {
  const source = [
    "unit.SetPosition(25.000000, 56.000000, 0.0)",
    "UI.add_waypoint_advanced(25.500000, 56.500000, 0.000000, 12.000000)",
    '',
  ].join('\n');
  const updated = applyScenarioEdits(source, [
    { kind: 'position', sourceLine: 1, lat: 26.1, lng: 57.2 },
    { kind: 'waypoint', sourceLine: 2, lat: 26.2, lng: 57.3 },
  ], 'lat-lng');
  assert.match(updated, /SetPosition\(26\.100000, 57\.200000, 0\.0\)/);
  assert.match(updated, /waypoint_advanced\(26\.200000, 57\.300000, 0\.000000, 12\.000000\)/);
});

test('preserves legacy longitude/latitude SetPosition order', () => {
  const updated = applyScenarioEdits(
    'unit.SetPosition(56.000000, 25.000000, 0.0)\n',
    [{ kind: 'position', sourceLine: 1, lat: 26.1, lng: 57.2 }],
    'lng-lat',
  );
  assert.equal(updated, 'unit.SetPosition(57.200000, 26.100000, 0.0)\n');
});

test('inserts detour waypoints before the original target', () => {
  const source = '    UI.add_waypoint_advanced(26.000000, 57.000000, 0.000000, 15.000000)\n';
  const updated = applyScenarioEdits(source, [{
    kind: 'insert-waypoint', sourceLine: 1, lat: 25.9, lng: 56.8, altitude: 0, speed: 15,
  }], 'lat-lng');
  assert.equal(updated, [
    '    UI.add_waypoint_advanced(25.900000, 56.800000, 0.000000, 15.000000)',
    '    UI.add_waypoint_advanced(26.000000, 57.000000, 0.000000, 15.000000)',
    '',
  ].join('\n'));
});

test('refuses to edit a stale or unexpected source line', () => {
  assert.throws(() => applyScenarioEdits(
    "unit.heading = 90\n",
    [{ kind: 'position', sourceLine: 1, lat: 26, lng: 57 }],
    'lat-lng',
  ), /no longer a SetPosition/);
});
