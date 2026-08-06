'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { parseScenario } = require('../src/scenario-parser.cjs');
const { selectTheater } = require('../src/theater-selector.cjs');

const projectRoot = path.resolve(__dirname, '..', '..');
const scenarioRoot = path.join(projectRoot, 'scenarios');
const theaterRoot = path.join(projectRoot, 'theaters');
const landPath = path.resolve(__dirname, '..', 'renderer', 'data', 'global-land.geojson');

async function main() {
  const { buildLandIndex, validateAircraftLoadouts, validateMission, validateRealWorld } = await import(
    pathToFileURL(path.resolve(__dirname, '..', 'renderer', 'geometry.js'))
  );
  const theaters = fs.readdirSync(theaterRoot)
    .filter((name) => name.toLowerCase().endsWith('.json'))
    .map((name) => JSON.parse(fs.readFileSync(path.join(theaterRoot, name), 'utf8')));
  const landIndex = buildLandIndex(JSON.parse(fs.readFileSync(landPath, 'utf8')));
  const requested = process.argv.slice(2);
  const scenarioPaths = requested.length
    ? requested.map((value) => path.resolve(process.cwd(), value))
    : fs.readdirSync(scenarioRoot)
      .filter((name) => name.toLowerCase().endsWith('.py'))
      .map((name) => path.join(scenarioRoot, name));

  let errorCount = 0;
  for (const scenarioPath of scenarioPaths) {
    const scenario = parseScenario(fs.readFileSync(scenarioPath, 'utf8'), scenarioPath);
    const theater = selectTheater(scenario, theaters);
    const maskFindings = theater
      ? validateMission(scenario, theater, 1).map((finding) => ({ source: 'GCBH mask', ...finding }))
      : [];
    const realFindings = validateRealWorld(scenario, theater, landIndex, 1);
    const findings = [...maskFindings, ...realFindings, ...validateAircraftLoadouts(scenario)];
    const errors = findings.filter((finding) => finding.severity === 'error');
    errorCount += errors.length;
    const maskLabel = theater ? theater.theater_id : 'global coastline only';
    console.log(`\n${path.basename(scenarioPath)} [${maskLabel}]: ${errors.length} errors, ${findings.length - errors.length} warnings/info`);
    for (const finding of findings) {
      const coordinate = finding.point ? ` @ ${finding.point.lat.toFixed(6)},${finding.point.lng.toFixed(6)}` : '';
      const suggestion = finding.suggestion
        ? ` -> candidate ${finding.suggestion.lat.toFixed(6)},${finding.suggestion.lng.toFixed(6)}`
        : '';
      console.log(`  [${finding.severity.toUpperCase()}] ${finding.source || 'Audit'} / ${finding.unit}: ${finding.message}${coordinate}${suggestion}`);
    }
  }
  console.log(`\nAudit complete: ${errorCount} errors across ${scenarioPaths.length} scenario(s).`);
  if (errorCount) process.exitCode = 1;
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 2;
});
