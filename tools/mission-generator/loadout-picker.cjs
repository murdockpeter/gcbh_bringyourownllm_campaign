'use strict';

const fs = require('node:fs');
const readline = require('node:readline/promises');
const { stdin, stdout } = require('node:process');
const { readJson, normalizeState, normalizeSeed } = require('./inputs.cjs');
const { GameDatabase, defaultDatabasePath } = require('./database.cjs');
const { GeneratorError } = require('./errors.cjs');

function summarizeLaunchers(launchers) {
  const totals = new Map();
  for (const launcher of launchers) totals.set(launcher.item, (totals.get(launcher.item) || 0) + launcher.quantity);
  return [...totals].map(([item, quantity]) => `${quantity}x ${item}`).join(', ');
}

function loadoutMenus(state, seed, database) {
  const classes = new Set();
  for (const side of ['blue', 'red']) {
    for (const unit of state.sides[side].units) {
      if (!unit.mission_capable || unit.status === 'destroyed') continue;
      if (database.platform(unit.platform_class)?.domain === 'air') classes.add(unit.platform_class);
    }
  }
  const year = new Date(seed.date_time).getUTCFullYear();
  return [...classes].sort().map((className) => {
    const presets = Object.entries(seed.loadout_presets?.[className] || {}).map(([name, launchers]) => ({ name, launchers, source: 'preset' }));
    const presetNames = new Set(presets.map((entry) => entry.name));
    const databaseChoices = database.availableLoadouts(className, year)
      .filter((entry) => entry.launchers.length && !presetNames.has(entry.setupName))
      .map((entry) => ({ name: entry.setupName, launchers: entry.launchers, source: 'database' }));
    return {
      className,
      current: seed.loadout_selections?.[className] || null,
      overridden: Boolean(seed.loadout_overrides?.[className]),
      choices: [...presets, ...databaseChoices],
    };
  }).filter((menu) => menu.choices.length);
}

async function chooseLoadouts(options) {
  if (!stdin.isTTY || !stdout.isTTY) throw new GeneratorError('LOADOUT_PICKER_TTY', '--choose-loadouts requires an interactive terminal');
  const rawSeed = readJson(options.seedPath, 'scenario seed');
  const state = normalizeState(readJson(options.statePath, 'campaign state'));
  const seed = normalizeSeed(rawSeed);
  const database = new GameDatabase(options.databasePath || defaultDatabasePath());
  const prompt = readline.createInterface({ input: stdin, output: stdout });
  try {
    const menus = loadoutMenus(state, seed, database);
    if (!menus.length) {
      stdout.write('No selectable aircraft loadouts are available for this mission.\n');
      return;
    }
    stdout.write('\nAircraft loadout selection (Enter or 0 keeps the current/default choice)\n');
    for (const menu of menus) {
      stdout.write(`\n${menu.className}${menu.current ? ` — current: ${menu.current}` : ' — database default'}${menu.overridden ? ' [exact override currently active]' : ''}\n`);
      menu.choices.forEach((choice, index) => stdout.write(`  ${index + 1}. ${choice.name} [${choice.source}] — ${summarizeLaunchers(choice.launchers)}\n`));
      let answer;
      do {
        answer = (await prompt.question(`Choose ${menu.className} loadout: `)).trim();
        if (!answer || answer === '0') break;
        const choice = menu.choices[Number(answer) - 1];
        if (choice) {
          rawSeed.loadout_selections ||= {};
          rawSeed.loadout_selections[menu.className] = choice.name;
          if (rawSeed.loadout_overrides?.[menu.className]) delete rawSeed.loadout_overrides[menu.className];
          break;
        }
        stdout.write(`Enter a number from 0 to ${menu.choices.length}.\n`);
      } while (true);
    }
    fs.writeFileSync(options.seedPath, `${JSON.stringify(rawSeed, null, 2)}\n`, 'utf8');
    stdout.write(`\nSaved loadout choices to ${options.seedPath}\n\n`);
  } finally {
    prompt.close();
    database.close();
  }
}

module.exports = { summarizeLaunchers, loadoutMenus, chooseLoadouts };
