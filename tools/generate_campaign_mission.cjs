#!/usr/bin/env node
'use strict';

const path = require('node:path');
const { generateMission } = require('./mission-generator/generate.cjs');
const { GeneratorError, formatError } = require('./mission-generator/errors.cjs');

function usage() {
  return `Usage:
  npm run generate -- --state <campaign.json> --seed <scenario-seed.json> \\
    --output <scenario.py> --manifest <manifest.json> [--database <database.db>] [--rng-seed <seed>]
`;
}

function parseArgs(argv) {
  const options = {};
  for (let index = 0; index < argv.length; index += 1) {
    const flag = argv[index];
    if (flag === '--help' || flag === '-h') return { help: true };
    if (!flag.startsWith('--')) throw new GeneratorError('CLI_ARGUMENT', `Unexpected argument: ${flag}`);
    const key = flag.slice(2).replace(/-([a-z])/g, (_, letter) => letter.toUpperCase());
    const value = argv[index + 1];
    if (!value || value.startsWith('--')) throw new GeneratorError('CLI_ARGUMENT', `Missing value for ${flag}`);
    options[key] = value;
    index += 1;
  }
  return options;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    process.stdout.write(usage());
    return;
  }
  for (const key of ['state', 'seed', 'output', 'manifest']) {
    if (!options[key]) throw new GeneratorError('CLI_ARGUMENT', `Missing required --${key} argument.\n\n${usage()}`);
  }
  const result = await generateMission({
    statePath: path.resolve(options.state),
    seedPath: path.resolve(options.seed),
    databasePath: options.database ? path.resolve(options.database) : undefined,
    outputPath: path.resolve(options.output),
    manifestPath: path.resolve(options.manifest),
    rngSeed: options.rngSeed,
  });
  process.stdout.write(`Generated ${result.outputPath}\nManifest ${result.manifestPath}\n`);
  process.stdout.write(`Units: ${result.unitCounts.blue} BLUE, ${result.unitCounts.red} RED\n`);
  process.stdout.write(`Difficulty ratio: ${result.balance.ratio}\n`);
}

main().catch((error) => {
  process.stderr.write(`${formatError(error)}\n`);
  process.exitCode = error instanceof GeneratorError ? 2 : 1;
});
