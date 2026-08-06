'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { selectTheater, theaterCoversScenario } = require('../src/theater-selector.cjs');

const hormuz = {
  theater_id: 'hormuz',
  coverage_bounds: { west: 54, south: 23, east: 60.5, north: 28.8 },
  safe_water_polygons: [],
};

test('selects a regional mask only when it covers the scenario center', () => {
  const hormuzScenario = { units: [{ position: { lat: 26, lng: 57 } }] };
  const senkakuScenario = { units: [{ position: { lat: 26, lng: 124 } }] };
  assert.equal(theaterCoversScenario(hormuz, hormuzScenario), true);
  assert.equal(theaterCoversScenario(hormuz, senkakuScenario), false);
  assert.equal(selectTheater(senkakuScenario, [hormuz]), null);
});
