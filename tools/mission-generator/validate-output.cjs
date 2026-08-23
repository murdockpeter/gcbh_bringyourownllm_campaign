'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { parseScenario } = require('../../mission-map/src/scenario-parser.cjs');
const { selectTheater } = require('../../mission-map/src/theater-selector.cjs');
const { GeneratorError } = require('./errors.cjs');

async function validateOutput(source, filePath, expectedTheaterId) {
  const projectRoot = path.resolve(__dirname, '..', '..');
  const theaterRoot = path.join(projectRoot, 'theaters');
  const theaters = fs.readdirSync(theaterRoot).filter((name) => name.endsWith('.json'))
    .map((name) => JSON.parse(fs.readFileSync(path.join(theaterRoot, name), 'utf8')));
  const theater = theaters.find((item) => item.theater_id === expectedTheaterId);
  if (!theater) throw new GeneratorError('THEATER_MISSING', `Theater definition not found: ${expectedTheaterId}`);
  const parsed = parseScenario(source, filePath);
  if (parsed.version !== '0.2.1' || parsed.coordinateConvention.order !== 'lat-lng') {
    throw new GeneratorError('OUTPUT_CONVENTION', 'Generated scenario did not parse as version 0.2.1 latitude/longitude');
  }
  const names = parsed.units.map((unit) => unit.name);
  const duplicates = names.filter((name, index) => names.indexOf(name) !== index);
  if (duplicates.length) throw new GeneratorError('OUTPUT_NAMES', 'Generated unit names are not unique', [...new Set(duplicates)]);
  if (/TimeGoal\s*\(/.test(source)) throw new GeneratorError('OUTPUT_GOAL', 'Generated source contains forbidden TimeGoal');
  const selected = selectTheater(parsed, theaters);
  if (selected?.theater_id !== expectedTheaterId) throw new GeneratorError('THEATER_SELECTION', `Generated scenario did not select theater ${expectedTheaterId}`);
  const geometry = await import(pathToFileURL(path.join(projectRoot, 'mission-map', 'renderer', 'geometry.js')));
  const landPath = path.join(projectRoot, 'mission-map', 'renderer', 'data', 'global-land.geojson');
  const landIndex = geometry.buildLandIndex(JSON.parse(fs.readFileSync(landPath, 'utf8')));
  const findings = [
    ...geometry.validateMission(parsed, theater, 1).map((finding) => ({ source: 'GCBH mask', ...finding })),
    ...geometry.validateRealWorld(parsed, theater, landIndex, 1),
    ...geometry.validateAircraftLoadouts(parsed),
  ];
  const errors = findings.filter((finding) => finding.severity === 'error');
  if (errors.length) {
    throw new GeneratorError('OUTPUT_AUDIT', `Generated scenario has ${errors.length} audit error(s)`, errors.map((finding) => `${finding.unit}: ${finding.message}`));
  }
  return { parser: 'passed', theater: selected.theater_id, errors: 0, warnings: findings.length, findings };
}

module.exports = { validateOutput };
