import test from 'node:test';
import assert from 'node:assert/strict';

import { allianceSide, visibleFindings, visibleUnits } from '../renderer/side-filter.js';

const units = [
  { name: 'USS Test', allianceName: 'Blue', allianceId: 1 },
  { name: 'IRIS Test', allianceName: 'Iran', allianceId: 2 },
  { name: 'Observer', allianceName: 'Neutral' },
  { name: 'JS Test', allianceName: 'Japan', allianceId: 1 },
  { name: 'PLAN Test', allianceName: 'China', allianceId: 2 },
];

test('classifies the scenario alliance labels used by the map', () => {
  assert.equal(allianceSide('Blue'), 'blue');
  assert.equal(allianceSide('Coalition'), 'blue');
  assert.equal(allianceSide('Iran'), 'red');
  assert.equal(allianceSide('Red'), 'red');
  assert.equal(allianceSide('Japan', 1), 'blue');
  assert.equal(allianceSide('China', 2), 'red');
  assert.equal(allianceSide('Neutral'), 'other');
});

test('filters order-of-battle units by side', () => {
  assert.deepEqual(visibleUnits(units, 'blue').map(({ name }) => name), ['USS Test', 'JS Test']);
  assert.deepEqual(visibleUnits(units, 'red').map(({ name }) => name), ['IRIS Test', 'PLAN Test']);
  assert.equal(visibleUnits(units, 'all').length, 5);
});

test('filters unit findings while retaining mission-wide findings', () => {
  const findings = [
    { unit: 'USS Test', message: 'Blue issue' },
    { unit: 'IRIS Test', message: 'Red issue' },
    { unit: 'Scenario format', message: 'Mission issue' },
  ];
  assert.deepEqual(
    visibleFindings(findings, units, 'blue').map(({ message }) => message),
    ['Blue issue', 'Mission issue'],
  );
});
