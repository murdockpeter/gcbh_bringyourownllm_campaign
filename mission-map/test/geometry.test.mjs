import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';
import {
  buildLandIndex,
  distanceToLandNm,
  firstLandIntersection,
  haversineNm,
  pointInLand,
  pointInPolygon,
  sampleSegment,
  validateMission,
  validateRealWorld,
} from '../renderer/geometry.js';

const theater = {
  surface_classes: ['Test Ship'],
  safe_water_polygons: [{ name: 'box', points: [[56, 25], [58, 25], [58, 27], [56, 27]] }],
};
const hormuzLand = buildLandIndex(JSON.parse(fs.readFileSync(
  new URL('../renderer/data/hormuz-land.geojson', import.meta.url),
  'utf8',
)));

test('calculates plausible nautical-mile distance', () => {
  const distance = haversineNm({ lat: 26, lng: 56 }, { lat: 27, lng: 56 });
  assert.ok(distance > 59.9 && distance < 60.2);
});

test('detects points inside longitude/latitude polygons', () => {
  assert.equal(pointInPolygon({ lat: 26, lng: 57 }, theater.safe_water_polygons[0].points), true);
  assert.equal(pointInPolygon({ lat: 29, lng: 57 }, theater.safe_water_polygons[0].points), false);
});

test('samples both endpoints of a route', () => {
  const samples = sampleSegment({ lat: 26, lng: 56 }, { lat: 26, lng: 57 }, 10);
  assert.deepEqual(samples[0], { lat: 26, lng: 56 });
  assert.deepEqual(samples.at(-1), { lat: 26, lng: 57 });
});

test('flags a surface route that exits safe water', () => {
  const findings = validateMission({
    units: [{
      className: 'Test Ship',
      name: 'Alpha',
      position: { lat: 26, lng: 57 },
      waypoints: [{ lat: 28, lng: 57 }],
    }],
  }, theater, 1);
  assert.ok(findings.some((finding) => finding.message.includes('exits')));
});

test('distinguishes Gulf water from mainland and peninsula land', () => {
  assert.equal(pointInLand({ lat: 26, lng: 57 }, hormuzLand), false);
  assert.equal(pointInLand({ lat: 27.5, lng: 56.3 }, hormuzLand), true);
  assert.equal(pointInLand({ lat: 25.3, lng: 56.3 }, hormuzLand), true);
  assert.ok(distanceToLandNm({ lat: 26, lng: 57 }, hormuzLand) > 0);
  assert.ok(distanceToLandNm({ lat: 27.5, lng: 56.3 }, hormuzLand) < 0);
});

test('finds the first exact coastline intersection on a sea-to-land route', () => {
  const crossing = firstLandIntersection(
    { lat: 26, lng: 57 },
    { lat: 27.5, lng: 56.3 },
    hormuzLand,
  );
  assert.ok(crossing);
  assert.ok(crossing.t > 0 && crossing.t < 1);
});

test('reports real-world ship land crossings and offshore ground units', () => {
  const regionalTheater = {
    ...theater,
    safe_water_polygons: [{ name: 'box', points: [[55, 24], [59, 24], [59, 29], [55, 29]] }],
  };
  const findings = validateRealWorld({
    units: [
      {
        domain: 'surface', className: 'New Ship', name: 'Ship',
        position: { lat: 26, lng: 57, sourceLine: 10 },
        waypoints: [{ lat: 27.5, lng: 56.3, sourceLine: 11, altitude: 0, speed: 15 }],
      },
      {
        domain: 'ground', className: 'Radar', name: 'Offshore radar',
        position: { lat: 26, lng: 57, sourceLine: 20 }, waypoints: [],
      },
    ],
  }, regionalTheater, hormuzLand, 1);
  const routeFinding = findings.find((finding) => finding.message.includes('crosses real-world land'));
  const groundFinding = findings.find((finding) => finding.message.includes('Ground unit is'));
  assert.equal(routeFinding.edit.kind, 'waypoint');
  assert.equal(routeFinding.edit.sourceLine, 11);
  assert.ok(routeFinding.suggestion);
  assert.equal(groundFinding.edit.kind, 'position');
  assert.equal(groundFinding.edit.sourceLine, 20);
  assert.ok(groundFinding.suggestion);
});
