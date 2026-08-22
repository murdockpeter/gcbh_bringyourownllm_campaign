'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const projectRoot = path.resolve(__dirname, '..');
const files = [path.join(projectRoot, 'tools', 'generate_campaign_mission.cjs')]
  .concat(fs.readdirSync(path.join(projectRoot, 'tools', 'mission-generator'))
    .filter((name) => name.endsWith('.cjs'))
    .sort()
    .map((name) => path.join(projectRoot, 'tools', 'mission-generator', name)));

for (const file of files) {
  const result = spawnSync(process.execPath, ['--check', file], { stdio: 'inherit' });
  if (result.status !== 0) process.exit(result.status || 1);
}

process.stdout.write(`Syntax checked ${files.length} generator files.\n`);
