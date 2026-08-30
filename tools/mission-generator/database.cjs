'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { DatabaseSync } = require('node:sqlite');
const { GeneratorError } = require('./errors.cjs');

const PLATFORM_TABLES = ['ship', 'air', 'simpleair', 'ground', 'sub'];

function defaultDatabasePath() {
  const profile = process.env.USERPROFILE;
  if (!profile) throw new GeneratorError('DATABASE_PATH', 'USERPROFILE is unavailable; pass --database explicitly');
  return path.join(profile, 'AppData', 'LocalLow', 'Wardstone Games', 'GCB Horizon', 'Database', 'database.db');
}

class GameDatabase {
  constructor(databasePath = defaultDatabasePath()) {
    this.path = databasePath;
    if (!fs.existsSync(databasePath)) throw new GeneratorError('DATABASE_MISSING', `GCB Horizon database not found: ${databasePath}`);
    try {
      this.db = new DatabaseSync(databasePath, { readOnly: true });
      const row = this.db.prepare("SELECT Value FROM version WHERE Attribute = 'Version'").get();
      this.schemaVersion = Number(row?.Value);
    } catch (error) {
      throw new GeneratorError('DATABASE_OPEN', `Could not open GCB Horizon database: ${databasePath}`, error.message);
    }
    if (!Number.isInteger(this.schemaVersion) || this.schemaVersion < 2 || this.schemaVersion > 4) {
      throw new GeneratorError('DATABASE_VERSION', `Supported database schema versions are 2 through 4; found ${this.schemaVersion}`);
    }
    const requiredTables = ['platform_setup', 'platform_launcher', 'launcher_loadout', 'launcher_configuration'];
    const availableTables = new Set(this.db.prepare("SELECT name FROM sqlite_master WHERE type = 'table'").all().map((row) => row.name));
    const missingTables = requiredTables.filter((name) => !availableTables.has(name));
    if (missingTables.length) throw new GeneratorError('DATABASE_SCHEMA', 'Game database is missing required generation tables', missingTables);
    this.platformCache = new Map();
    this.loadoutCache = new Map();
    this.loadoutCatalogCache = new Map();
  }

  close() {
    this.db.close();
  }

  platform(className) {
    if (this.platformCache.has(className)) return this.platformCache.get(className);
    let found = null;
    for (const table of PLATFORM_TABLES) {
      const flightportColumn = table === 'ship' || table === 'ground' ? ', FlightportClass' : '';
      const row = this.db.prepare(`SELECT DatabaseClass, MaxSpeed_kts${flightportColumn} FROM ${table} WHERE DatabaseClass = ?`).get(className);
      if (row) {
        found = { className: row.DatabaseClass, domain: table === 'simpleair' ? 'air' : table, maxSpeedKts: Number(row.MaxSpeed_kts || 0), flightportClass: row.FlightportClass || '' };
        break;
      }
    }
    this.platformCache.set(className, found);
    return found;
  }

  loadoutFromSetup(className, setup) {
    const launcherRows = setup?.LauncherLoadout ? this.db.prepare(`
      SELECT ll.LauncherId AS launcherId, ll.Item AS item, ll.Quantity AS quantity,
             pl.LauncherClass AS launcherClass
      FROM launcher_loadout ll
      JOIN platform_launcher pl ON pl.DatabaseClass = ? AND pl.LauncherId = ll.LauncherId
      WHERE ll.DatabaseClass = ? AND ll.Item IS NOT NULL AND ll.Quantity > 0
      ORDER BY ll.LauncherId
    `).all(className, setup.LauncherLoadout).map((row) => ({
      launcherId: Number(row.launcherId), item: row.item, quantity: Number(row.quantity), launcherClass: row.launcherClass,
    })) : [];
    const launchersById = new Map();
    for (const launcher of launcherRows) {
      const current = launchersById.get(launcher.launcherId);
      if (!current || launcher.quantity > current.quantity || (launcher.quantity === current.quantity && launcher.item.localeCompare(current.item) < 0)) {
        launchersById.set(launcher.launcherId, launcher);
      }
    }
    const launchers = [...launchersById.values()].sort((left, right) => left.launcherId - right.launcherId);
    const magazines = setup?.MagazineLoadout ? this.db.prepare(`
      SELECT MagazineId AS magazineId, Item AS item, Quantity AS quantity
      FROM magazine_loadout
      WHERE DatabaseClass = ? AND Item IS NOT NULL AND Quantity > 0
      ORDER BY MagazineId, Item
    `).all(setup.MagazineLoadout).map((row) => ({
      magazineId: Number(row.magazineId), item: row.item, quantity: Number(row.quantity),
    })) : [];
    return { setupName: setup?.SetupName || null, launchers, magazines };
  }

  applicableSetupRows(className, year) {
    return this.db.prepare(`
      SELECT LauncherLoadout, MagazineLoadout, SetupName
      FROM platform_setup
      WHERE DatabaseClass = ? AND InitialYear <= ? AND FinalYear >= ?
      ORDER BY InitialYear DESC, SetupName ASC
    `).all(className, year, year);
  }

  defaultLoadout(className, year) {
    const key = `${className}:${year}`;
    if (this.loadoutCache.has(key)) return this.loadoutCache.get(key);
    const result = this.loadoutFromSetup(className, this.applicableSetupRows(className, year)[0]);
    this.loadoutCache.set(key, result);
    return result;
  }

  availableLoadouts(className, year) {
    const key = `${className}:${year}`;
    if (this.loadoutCatalogCache.has(key)) return this.loadoutCatalogCache.get(key);
    const seen = new Set();
    const result = this.applicableSetupRows(className, year)
      .filter((setup) => {
        if (seen.has(setup.SetupName)) return false;
        seen.add(setup.SetupName);
        return true;
      })
      .map((setup) => this.loadoutFromSetup(className, setup));
    this.loadoutCatalogCache.set(key, result);
    return result;
  }

  namedLoadout(className, year, setupName) {
    const available = this.availableLoadouts(className, year);
    const normalized = String(setupName).trim().replace(/\s+/g, ' ').toLowerCase();
    const short = (name) => String(name).trim().replace(/\s+\d{4}(?:\.\d+)?$/, '').replace(/\s+/g, ' ').toLowerCase();
    const matches = available.filter((loadout) => loadout.setupName === setupName
      || loadout.setupName.trim().replace(/\s+/g, ' ').toLowerCase() === normalized
      || short(loadout.setupName) === normalized);
    if (matches.length === 1) return matches[0];
    const names = available.map((loadout) => loadout.setupName);
    if (matches.length > 1) throw new GeneratorError('DATABASE_LOADOUT_SELECTION', `Loadout ${setupName} is ambiguous for ${className} in ${year}`, matches.map((loadout) => loadout.setupName));
    throw new GeneratorError('DATABASE_LOADOUT_SELECTION', `Loadout ${setupName} is not available for ${className} in ${year}`, names);
  }

  isLauncherCompatible(launcherClass, item) {
    const direct = this.db.prepare(`
      SELECT 1 AS ok FROM launcher_configuration
      WHERE DatabaseClass = ? AND ChildClass = ? LIMIT 1
    `).get(launcherClass, item);
    if (direct) return true;
    const grouped = this.db.prepare(`
      SELECT 1 AS ok
      FROM launcher_configuration lc
      JOIN equipment_group eg ON eg.DatabaseClass = lc.EquipmentGroup
      WHERE lc.DatabaseClass = ? AND eg.EquipmentClass = ?
      LIMIT 1
    `).get(launcherClass, item);
    return Boolean(grouped);
  }

  validateLoadout(className, launchers) {
    const errors = [];
    const seen = new Set();
    const launcherQuery = this.db.prepare('SELECT LauncherClass FROM platform_launcher WHERE DatabaseClass = ? AND LauncherId = ?');
    for (const launcher of launchers) {
      if (seen.has(launcher.launcherId)) errors.push(`launcher ${launcher.launcherId} is assigned more than once`);
      seen.add(launcher.launcherId);
      const row = launcherQuery.get(className, launcher.launcherId);
      if (!row) {
        errors.push(`launcher ${launcher.launcherId} does not exist`);
      } else if (!this.isLauncherCompatible(row.LauncherClass, launcher.item)) {
        errors.push(`launcher ${launcher.launcherId} is incompatible with ${launcher.item}`);
      }
      if (!Number.isInteger(launcher.quantity) || launcher.quantity < 1) errors.push(`launcher ${launcher.launcherId} quantity must be a positive integer`);
    }
    if (errors.length) throw new GeneratorError('DATABASE_LOADOUT', `Loadout override for ${className} is invalid`, errors);
    return launchers.map((launcher) => ({ launcherId: launcher.launcherId, item: launcher.item, quantity: launcher.quantity }));
  }
}

module.exports = { PLATFORM_TABLES, defaultDatabasePath, GameDatabase };
