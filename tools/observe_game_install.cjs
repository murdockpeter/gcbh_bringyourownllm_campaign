'use strict';

const crypto = require('node:crypto');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { DatabaseSync } = require('node:sqlite');

const root = path.resolve(__dirname, '..');
const defaultGame = 'D:\\SteamLibrary\\steamapps\\common\\Global Conflict Blue Horizon';
const gameRoot = process.argv[2] ? path.resolve(process.argv[2]) : defaultGame;
const userDb = path.join(os.homedir(), 'AppData', 'LocalLow', 'Wardstone Games', 'GCB Horizon', 'Database', 'database.db');
const installDb = path.join(gameRoot, 'database', 'database.db');
const steamManifest = path.resolve(gameRoot, '..', '..', 'appmanifest_4069800.acf');

function hash(file) {
  return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

function manifestValue(source, key) {
  return new RegExp(`"${key}"\\s+"([^"]+)"`).exec(source)?.[1] || null;
}

function fileRecord(file) {
  const stat = fs.statSync(file);
  return { path: file, bytes: stat.size, modified_utc: stat.mtime.toISOString(), sha256: hash(file) };
}

for (const file of [installDb, userDb, steamManifest]) {
  if (!fs.existsSync(file)) throw new Error(`Required game file not found: ${file}`);
}

const manifest = fs.readFileSync(steamManifest, 'utf8');
const db = new DatabaseSync(userDb, { readOnly: true });
const tableNames = db.prepare("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").all().map((row) => row.name);
const counts = {};
for (const table of ['air', 'simpleair', 'ship', 'sub', 'ground', 'platform_setup', 'missile', 'radar', 'sonar']) {
  counts[table] = Number(db.prepare(`SELECT COUNT(*) AS count FROM ${table}`).get().count);
}

const campaignClasses = [
  'America LHA', 'Wasp LHDM', 'San Antonio LPDM', 'Landing Craft Air Cushion LCAC',
  'MV-22 Osprey', 'CH-53K', 'AH-1Z Viper', 'UH-1Y Venom', 'F-35B', 'EA-18G',
  'Khordad-15', 'Shahed OWA TEL', 'Fateh', 'Pr 877EKM Paltus(Iran)',
];
const platforms = [];
for (const className of campaignClasses) {
  for (const table of ['air', 'simpleair', 'ship', 'sub', 'ground']) {
    const columns = new Set(db.prepare(`PRAGMA table_info(${table})`).all().map((row) => row.name));
    const select = ['DatabaseClass', 'DisplayClass', 'Country', 'Subtype', 'InitialYear', 'FinalYear', 'FlightportClass']
      .filter((column) => columns.has(column)).join(', ');
    const row = db.prepare(`SELECT ${select} FROM ${table} WHERE DatabaseClass = ?`).get(className);
    if (row) {
      const setups = db.prepare(`SELECT SetupName FROM platform_setup WHERE DatabaseClass = ? AND InitialYear <= 2026 AND FinalYear >= 2026 ORDER BY SetupName`)
        .all(className).map((entry) => entry.SetupName);
      platforms.push({ table, ...row, setups });
      break;
    }
  }
}

const scriptFiles = ['tasks/auto_attack.py', 'tasks/ship1.py', 'tasks/aircraft1.py', 'tasks/wait_for_group.py', 'tasks/land_helicopter.py'];
const observation = {
  observed_utc: new Date().toISOString(),
  steam: {
    appid: manifestValue(manifest, 'appid'),
    name: manifestValue(manifest, 'name'),
    buildid: manifestValue(manifest, 'buildid'),
    last_updated_epoch: Number(manifestValue(manifest, 'LastUpdated')),
    install_root: gameRoot,
  },
  database: {
    schema_version: Number(db.prepare("SELECT Value FROM version WHERE Attribute = 'Version'").get().Value),
    installed: fileRecord(installDb),
    player_copy: fileRecord(userDb),
    copies_match: hash(installDb) === hash(userDb),
    table_count: tableNames.length,
    tables: tableNames,
    row_counts: counts,
  },
  relevant_platforms: platforms,
  behavior_scripts: scriptFiles.map((relative) => fileRecord(path.join(gameRoot, 'scripts', relative))),
};
db.close();

const stamp = new Date().toISOString().slice(0, 10).replaceAll('-', '');
const out = path.join(root, 'docs', `database_observation_${stamp}.json`);
fs.writeFileSync(out, `${JSON.stringify(observation, null, 2)}\n`);
process.stdout.write(`Observed build ${observation.steam.buildid}, schema ${observation.database.schema_version}, ${observation.database.table_count} tables.\n`);
process.stdout.write(`Database copies match: ${observation.database.copies_match}. Wrote ${out}\n`);
