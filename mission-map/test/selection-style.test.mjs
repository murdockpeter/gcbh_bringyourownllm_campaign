import test from 'node:test';
import assert from 'node:assert/strict';

import { ACTIVE_UNIT_COLOR, routeVisualStyle, waypointVisualStyle } from '../renderer/selection-style.js';

test('selected routes use the active orange style', () => {
  assert.deepEqual(routeVisualStyle('#4aa9ff', true), {
    strokeColor: ACTIVE_UNIT_COLOR, strokeOpacity: 1, strokeWeight: 4, zIndex: 220,
  });
});

test('unselected route and waypoint styles retain their alliance color', () => {
  assert.equal(routeVisualStyle('#ef5a61').strokeColor, '#ef5a61');
  assert.equal(waypointVisualStyle('#4aa9ff').color, '#4aa9ff');
});

test('selected waypoints use orange and stronger emphasis', () => {
  const selected = waypointVisualStyle('#4aa9ff', true);
  const normal = waypointVisualStyle('#4aa9ff');
  assert.equal(selected.color, ACTIVE_UNIT_COLOR);
  assert.ok(selected.strokeWeight > normal.strokeWeight);
  assert.ok(selected.scale > normal.scale);
});
