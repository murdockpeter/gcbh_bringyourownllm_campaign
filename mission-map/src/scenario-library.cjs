'use strict';

const fs = require('node:fs/promises');
const path = require('node:path');
const { parseScenario } = require('./scenario-parser.cjs');
const { selectTheater } = require('./theater-selector.cjs');

async function readTheaters(theaterRoot) {
  const names = (await fs.readdir(theaterRoot)).filter((name) => name.toLowerCase().endsWith('.json')).sort();
  return Promise.all(names.map(async (name) => JSON.parse(await fs.readFile(path.join(theaterRoot, name), 'utf8'))));
}

async function listScenarios(scenarioRoot, theaters) {
  const entries = (await fs.readdir(scenarioRoot, { withFileTypes: true }))
    .filter((entry) => entry.isFile() && entry.name.toLowerCase().endsWith('.py'));
  const scenarios = await Promise.all(entries.map(async (entry) => {
    const filePath = path.join(scenarioRoot, entry.name);
    const scenario = parseScenario(await fs.readFile(filePath, 'utf8'), filePath);
    return { name: entry.name, path: filePath, title: scenario.info.name || entry.name, theaterId: selectTheater(scenario, theaters)?.theater_id || '' };
  }));
  return scenarios.sort((left, right) => left.name.localeCompare(right.name));
}

module.exports = { readTheaters, listScenarios };
