import test from 'node:test';
import assert from 'node:assert/strict';

import { inferUnitMission } from '../renderer/unit-mission.js';

const unit = (overrides = {}) => ({ name: 'Test', className: 'Unknown', domain: 'unknown', launcherItems: [], tasks: [], ...overrides });

test('infers CAP and SEAD missions from aircraft tasking and loadout', () => {
  assert.equal(inferUnitMission(unit({ className: 'F/A-18F', domain: 'air', launcherItems: [{ item: 'AIM-120D' }] })).code, 'CAP');
  assert.equal(inferUnitMission(unit({ name: 'Lancer 1', className: 'F-15E', domain: 'air', launcherItems: [{ item: 'GBU-39 SDB' }] })).code, 'SEAD / STRIKE');
});

test('infers combined ASuW and ASW maritime patrol', () => {
  assert.equal(inferUnitMission(unit({ className: 'P-8 MPA', domain: 'air', launcherItems: [{ item: 'AGM-84D Harpoon' }, { item: 'Mk-46 Mod5' }] })).code, 'ASuW / ASW');
});

test('infers surface warfare capabilities and specialized support roles', () => {
  assert.equal(inferUnitMission(unit({ className: 'Arleigh Burke DDG', domain: 'surface', launcherItems: [{ item: 'RIM-174A' }, { item: 'RGM-84 Harpoon' }, { item: 'Mk-54' }] })).code, 'AAW / ASuW / ASW');
  assert.equal(inferUnitMission(unit({ className: 'Avenger MCM', domain: 'surface' })).code, 'MCM');
  assert.equal(inferUnitMission(unit({ className: 'Kaman FACM', domain: 'surface' })).code, 'ASuW');
  assert.equal(inferUnitMission(unit({ className: 'K-300P Bastion-P', domain: 'ground' })).code, 'ASuW');
});
