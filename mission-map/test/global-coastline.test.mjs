import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

import { buildLandIndex, pointInLand } from '../renderer/geometry.js';

test('global coastline covers both Hormuz and the Senkaku operational area', () => {
  const land = buildLandIndex(JSON.parse(fs.readFileSync(
    new URL('../renderer/data/global-land.geojson', import.meta.url),
    'utf8',
  )));
  assert.equal(pointInLand({ lat: 26.0, lng: 57.0 }, land), false);
  assert.equal(pointInLand({ lat: 27.5, lng: 56.3 }, land), true);
  assert.equal(pointInLand({ lat: 24.73, lng: 125.3 }, land), true);
  assert.equal(pointInLand({ lat: 25.5, lng: 123.0 }, land), false);
});
