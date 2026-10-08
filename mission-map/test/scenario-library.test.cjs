'use strict';

const assert = require('node:assert/strict');
const path = require('node:path');
const test = require('node:test');
const { readTheaters, listScenarios } = require('../src/scenario-library.cjs');
const root = path.resolve(__dirname, '../..');

test('workspace library discovers Baltic and Hormuz scenarios with readable titles', async () => {
  const theaters = await readTheaters(path.join(root, 'theaters'));
  const scenarios = await listScenarios(path.join(root, 'scenarios'), theaters);
  const baltic = scenarios.find((scenario) => scenario.name === 'operation_baltic_shield.py');
  assert.equal(baltic.theaterId, 'baltic_latvia_estonia');
  assert.equal(baltic.title, 'Operation Baltic Shield - First Contact');
  assert.ok(scenarios.some((scenario) => scenario.theaterId === 'hormuz_mvp'));
  assert.ok(scenarios.every((scenario) => path.extname(scenario.path) === '.py'));
});
