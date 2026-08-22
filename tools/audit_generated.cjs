'use strict';

const path = require('node:path');
const { spawnSync } = require('node:child_process');

const projectRoot = path.resolve(__dirname, '..');
const requested = process.argv.slice(2);
if (!requested.length) {
  process.stderr.write('Usage: npm run audit:generated -- <scenario.py> [more scenarios]\n');
  process.exit(2);
}
const scenarioPaths = requested.map((value) => path.resolve(projectRoot, value));
const auditScript = path.join(projectRoot, 'mission-map', 'tools', 'audit-scenarios.cjs');
const result = spawnSync(process.execPath, [auditScript, ...scenarioPaths], { cwd: projectRoot, stdio: 'inherit' });
process.exit(result.status ?? 1);
