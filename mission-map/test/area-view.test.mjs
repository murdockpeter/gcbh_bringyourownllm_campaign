import assert from 'node:assert/strict';
import test from 'node:test';
import { operationalBounds, preferredAreaScenario, scenariosForArea } from '../renderer/area-view.js';

const scenarios = [
  { name: 'baltic_setup_validation.py', path: '/setup.py', theaterId: 'baltic' },
  { name: 'operation_baltic_shield.py', path: '/shield.py', theaterId: 'baltic' },
  { name: 'operation_gate_latch.py', path: '/gate.py', theaterId: 'hormuz' },
  { name: 'other.py', path: '/other.py', theaterId: '' },
];

test('area filters isolate Baltic missions while All retains other areas', () => {
  assert.deepEqual(scenariosForArea(scenarios, 'baltic').map(s => s.path), ['/setup.py', '/shield.py']);
  assert.equal(scenariosForArea(scenarios).length, 4);
  assert.deepEqual(scenariosForArea(scenarios, 'missing'), []);
});

test('area switching retains the current mission or prefers a playable operation over the fixture', () => {
  const baltic = scenariosForArea(scenarios, 'baltic');
  assert.equal(preferredAreaScenario(baltic, '/gate.py').path, '/shield.py');
  assert.equal(preferredAreaScenario(baltic, '/setup.py').path, '/setup.py');
  assert.equal(preferredAreaScenario([]), null);
});

test('full-area bounds use the operational envelope rather than unit positions', () => {
  assert.deepEqual(operationalBounds({ coverage_bounds: { west: 18, south: 54.5, east: 30, north: 60.3 } }), { west: 18, south: 54.5, east: 30, north: 60.3 });
  assert.equal(operationalBounds(null), null);
  assert.equal(operationalBounds({ coverage_bounds: { west: NaN } }), null);
});
