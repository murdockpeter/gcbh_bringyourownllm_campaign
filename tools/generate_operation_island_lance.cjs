'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { GameDatabase, defaultDatabasePath } = require('./mission-generator/database.cjs');
const { parseScenario } = require('../mission-map/src/scenario-parser.cjs');

const root = path.resolve(__dirname, '..');
const outputPath = path.join(root, 'scenarios', 'operation_island_lance.py');
const manifestPath = path.join(root, 'scenarios', 'operation_island_lance.manifest.json');
const year = 2026;
const db = new GameDatabase(process.argv[2] || defaultDatabasePath());
const sides = { blue: [], red: [], neutral: [] };
const formations = [];

function q(value) { return JSON.stringify(value); }
function f(value) { return Number(value).toFixed(6); }
function point(lat, lon, altitude = 0, speed = 0, tasks = '') { return { lat, lon, altitude, speed, tasks }; }
function grid(lat, lon, index, columns = 5, stepLat = 0.018, stepLon = 0.024) {
  return { lat: lat + Math.floor(index / columns) * stepLat, lon: lon + (index % columns) * stepLon };
}

const fallbackLoadouts = new Map();
for (const file of ['operation_resolute_passage.py', 'operation_crossed_sabers.py', 'operation_narrow_furnace.py']) {
  const scenario = parseScenario(fs.readFileSync(path.join(root, 'scenarios', file), 'utf8'), file);
  for (const unit of scenario.units) {
    if (!fallbackLoadouts.has(unit.className) && unit.launcherItems.length) {
      fallbackLoadouts.set(unit.className, unit.launcherItems);
    }
  }
}

function loadoutFor(className, setupName) {
  let loadout = setupName ? db.namedLoadout(className, year, setupName) : db.defaultLoadout(className, year);
  if (!loadout.launchers.length && fallbackLoadouts.has(className)) {
    const launchers = db.validateLoadout(className, fallbackLoadouts.get(className));
    loadout = { setupName: 'campaign-validated fallback', launchers, magazines: [] };
  }
  return loadout;
}

function add(side, spec) {
  const platform = db.platform(spec.className);
  if (!platform) throw new Error(`Database class not found: ${spec.className}`);
  const loadout = loadoutFor(spec.className, spec.setup);
  sides[side].push({
    side,
    domain: platform.domain,
    heading: side === 'blue' ? 285 : side === 'red' ? 120 : 285,
    speed: spec.speed ?? Math.min(platform.maxSpeedKts || 0, platform.domain === 'air' ? 360 : 18),
    altitude: platform.domain === 'air' ? 6500 : platform.domain === 'sub' ? -80 : 0,
    fuel: 1,
    route: [],
    role: 'support',
    visible: false,
    ...spec,
    loadout,
  });
}

function addSeries(side, prefix, className, count, center, options = {}) {
  for (let index = 0; index < count; index += 1) {
    const pos = grid(center.lat, center.lon, index, options.columns || 5, options.stepLat, options.stepLon);
    add(side, {
      name: `${prefix} ${index + 1}`,
      className,
      lat: pos.lat,
      lon: pos.lon,
      ...options,
      route: typeof options.route === 'function' ? options.route(index) : (options.route || []),
    });
  }
}

const convoyRoute = [point(26.31, 56.33, 0, 12), point(26.34, 56.05, 0, 12), point(26.37, 55.80, 0, 12)];
const escortRoute = [point(26.27, 56.38, 0, 18), point(26.31, 56.08, 0, 18), point(26.35, 55.83, 0, 18)];
const amphibRoute = [point(25.77, 56.02, 0, 16), point(25.88, 55.72, 0, 16), point(26.02, 55.50, 0, 14)];
const landingRoute = [point(26.03, 55.52, 0, 28), point(26.13, 55.40, 0, 24), point(26.20, 55.34, 0, 18)];

const convoy = [
  ['RFA Fort Victoria', 'Fort Victoria AOR'], ['USNS John Ericsson', 'Henry J Kaiser'],
  ['USNS Amelia Earhart', 'Lewis and Clark'], ['RFA Tidespring', 'Fort Victoria AOR'],
  ['USNS Guadalupe', 'Henry J Kaiser'], ['USNS Cesar Chavez', 'Lewis and Clark'],
];
convoy.forEach(([name, className], index) => add('blue', { name, className, ...grid(26.12, 56.62, index, 3, 0.035, 0.045), speed: 12, role: 'convoy', route: convoyRoute, visible: true }));

const escorts = [
  ['USS Mason', 'Arleigh Burke IIA DDGHM'], ['USS Chosin', 'Ticonderoga CG Baseline 4'],
  ['USS Thomas Hudner', 'Arleigh Burke IIA DDGHM'], ['USS Arleigh Burke', 'Arleigh Burke III DDGHM'],
  ['HMS Diamond', 'Type 45 DDG'], ['HMS Richmond', 'Type 23 FF'], ['USS Tempest', 'Cyclone PBFM'],
  ['USCGC Stone', 'Legend WMSL'], ['USS Devastator', 'Avenger MCM'], ['USS Dextrous', 'Avenger MCM'],
];
escorts.forEach(([name, className], index) => add('blue', { name, className, ...grid(26.03, 56.55, index, 5, 0.17, 0.055), speed: className === 'Avenger MCM' ? 10 : 18, role: 'escort', route: escortRoute }));
formations.push({ leader: 'RFA Fort Victoria', members: convoy.slice(1).map(([name]) => name) });
formations.push({ leader: 'USS Mason', members: escorts.slice(1).map(([name]) => name) });

add('blue', { name: 'USS George H.W. Bush', className: 'CVN-77 (Nimitz) USS George H.W. Bush', lat: 25.20, lon: 57.45, speed: 16, role: 'carrier', visible: true });
const amphibShips = [
  ['USS Iwo Jima', 'Wasp LHDM'], ['USS America', 'America LHA'],
  ['USS Arlington', 'San Antonio LPDM'], ['HMS Albion', 'Albion Class LPD'],
];
amphibShips.forEach(([name, className], index) => add('blue', { name, className, ...grid(25.64, 56.26, index, 2, 0.055, 0.075), speed: 16, role: 'amphibious', route: amphibRoute, visible: true }));
formations.push({ leader: 'USS Iwo Jima', members: amphibShips.slice(1).map(([name]) => name) });
addSeries('blue', 'Surf Rider', 'Landing Craft Air Cushion LCAC', 4, { lat: 25.97, lon: 55.67 }, { speed: 32, role: 'landing_craft', route: landingRoute, columns: 4 });
addSeries('blue', 'Beachmaster', 'LCU 1600 LCU-Navy', 2, { lat: 25.94, lon: 55.62 }, { speed: 10, role: 'landing_craft', route: landingRoute, columns: 2 });
formations.push({ leader: 'Surf Rider 1', members: ['Surf Rider 2', 'Surf Rider 3', 'Surf Rider 4', 'Beachmaster 1', 'Beachmaster 2'] });

addSeries('blue', 'Silent Service', 'SSN 774.4 Virginia', 2, { lat: 25.35, lon: 56.30 }, { altitude: -90, speed: 8, role: 'submarine', columns: 2, route: [point(25.62, 55.92, -90, 8), point(25.86, 55.62, -90, 6)] });
add('blue', { name: 'HMS Ambush', className: 'Astute SSN', lat: 25.48, lon: 57.00, altitude: -100, speed: 8, role: 'submarine', route: [point(25.72, 56.55, -100, 8), point(25.92, 56.12, -100, 6)] });

const assaultRoute = [point(25.82, 55.92, 900, 190, 'WaitForGroup'), point(26.08, 55.52, 500, 190), point(26.255, 55.305, 120, 80, 'Land')];
const gunshipRoute = [point(25.88, 55.84, 800, 150, 'WaitForGroup,AutoAttack'), point(26.16, 55.42, 500, 150, 'AutoAttack'), point(26.27, 55.30, 350, 120, 'AutoAttack')];
addSeries('blue', 'Osprey', 'MV-22 Osprey', 8, { lat: 25.58, lon: 56.14 }, { altitude: 800, speed: 220, role: 'air_assault', route: assaultRoute, columns: 4, landingTarget: 'Tunb Expeditionary LZ' });
addSeries('blue', 'King', 'CH-53K', 4, { lat: 25.56, lon: 56.02 }, { altitude: 600, speed: 150, role: 'air_assault', route: assaultRoute, columns: 4, landingTarget: 'Tunb Expeditionary LZ' });
addSeries('blue', 'Viper Gunship', 'AH-1Z Viper', 4, { lat: 25.66, lon: 55.98 }, { altitude: 500, speed: 145, role: 'attack_helo', route: gunshipRoute, setup: 'AT2 2003', columns: 4 });
addSeries('blue', 'Venom', 'UH-1Y Venom', 2, { lat: 25.62, lon: 55.94 }, { altitude: 500, speed: 140, role: 'attack_helo', route: gunshipRoute, columns: 2 });

const capRoute = (index) => [point(25.70 + index * 0.006, 56.10, 7600, 420, 'WaitForGroup,AutoAttack'), point(26.25, 55.38, 7600, 420, 'AirPatrolArea,AutoAttack'), point(25.78, 55.92, 7600, 420, 'AutoAttack')];
addSeries('blue', 'Tiger', 'F/A-18F', 8, { lat: 25.44, lon: 56.48 }, { altitude: 7600, speed: 410, role: 'escort_cap', route: capRoute, setup: 'AW1 2010', columns: 4 });
const seadRoute = [point(25.72, 56.68, 8500, 430, 'WaitForGroup,AutoAttack'), point(26.45, 56.48, 7800, 440, 'GroundStrike,AutoAttack'), point(25.66, 56.84, 8000, 400, 'AutoAttack')];
addSeries('blue', 'Razor', 'F/A-18F', 6, { lat: 25.30, lon: 57.05 }, { altitude: 8500, speed: 420, role: 'sead', route: seadRoute, setup: 'SD1 2010', columns: 3 });
addSeries('blue', 'Growler', 'EA-18G', 4, { lat: 25.22, lon: 56.92 }, { altitude: 9000, speed: 410, role: 'electronic_attack', route: seadRoute, setup: 'EA-18G-1', columns: 4 });
addSeries('blue', 'Viper Strike', 'F-15E', 6, { lat: 24.94, lon: 56.90 }, { altitude: 9000, speed: 430, role: 'strike', route: seadRoute, columns: 3 });
const maritimeStrikeRoute = [point(25.62, 56.78, 7600, 420, 'WaitForGroup,AutoAttack'), point(26.02, 56.18, 5200, 430, 'AutoAttack'), point(25.48, 56.72, 7600, 400, 'AutoAttack')];
addSeries('blue', 'Hammer', 'F/A-18F', 4, { lat: 25.34, lon: 56.90 }, { altitude: 7600, speed: 420, role: 'maritime_strike', route: maritimeStrikeRoute, setup: 'SM1 2010', columns: 4 });

const patrolRoute = [point(25.75, 56.95, 7000, 300, 'WaitForGroup,AutoAttack'), point(26.10, 56.20, 6500, 300, 'ASWPatrol,EngageAll'), point(25.70, 56.72, 6500, 300, 'ASWPatrol,EngageAll')];
addSeries('blue', 'Poseidon', 'P-8 MPA', 4, { lat: 25.08, lon: 57.55 }, { altitude: 7000, speed: 310, role: 'maritime_patrol', route: patrolRoute, columns: 4 });
addSeries('blue', 'Hawkeye', 'E-2D', 2, { lat: 25.12, lon: 57.30 }, { altitude: 8500, speed: 280, role: 'aew', route: [point(25.38, 56.92, 8500, 280), point(25.12, 57.30, 8500, 280)], columns: 2 });
addSeries('blue', 'Shell', 'KC-135R', 2, { lat: 24.92, lon: 57.55 }, { altitude: 9000, speed: 310, role: 'tanker', route: [point(25.05, 57.10, 9000, 310), point(24.92, 57.55, 9000, 310)], columns: 2 });
addSeries('blue', 'Sea Guardian', 'MQ-9B SeaGuardian', 4, { lat: 25.55, lon: 56.82 }, { altitude: 9000, speed: 220, role: 'reconnaissance', route: patrolRoute, setup: 'MQ-9B SeaGuardian (2019)', columns: 4 });
addSeries('blue', 'Romeo', 'S-70B Seahawk', 4, { lat: 25.78, lon: 56.42 }, { altitude: 500, speed: 135, role: 'asw', route: [point(25.92, 56.05, 400, 130), point(26.05, 55.72, 400, 130)], columns: 4 });

add('blue', { name: 'Tunb Expeditionary LZ', className: 'Airstrip, Small (USA)', lat: 26.258, lon: 55.304, altitude: 8, speed: 0, role: 'lodgment', visible: true });
addSeries('blue', 'Pathfinder', 'M113 APC', 3, { lat: 26.253, lon: 55.299 }, { speed: 0, role: 'lodgment', columns: 3, stepLon: 0.004, stepLat: 0.004, visible: true });
addSeries('blue', 'Rampart', 'M2A3 Bradley', 2, { lat: 26.255, lon: 55.301 }, { speed: 0, role: 'lodgment', columns: 2, stepLon: 0.004, visible: true });
addSeries('blue', 'Stinger Team', 'Stinger Vehicle', 2, { lat: 26.255, lon: 55.309 }, { speed: 0, role: 'lodgment', columns: 2, stepLon: 0.004, visible: true });

const redShips = [
  ['Khanjar', 'Kaman FACM'], ['Falakhon', 'Kaman FACM'], ['Scimitar', 'Kaman FACM'], ['Zolfaghar', 'Kaman FACM'],
  ['Tsunami 1', 'Pr 205ER Tsunami (Iran)'], ['Tsunami 2', 'Pr 205ER Tsunami (Iran)'],
  ['Shamshir', 'Kaman FACM'], ['Neyzeh', 'Kaman FACM'], ['Tabarzin', 'Kaman FACM'],
  ['IRIS Jamaran', 'Moudge FFG'], ['IRIS Damavand', 'Moudge FFG'], ['Tsunami 3', 'Pr 205ER Tsunami (Iran)'],
];
const redSurfaceRoute = [point(26.24, 56.02, 0, 22), point(26.18, 56.28, 0, 22), point(26.12, 56.48, 0, 20)];
redShips.forEach(([name, className], index) => add('red', { name, className, ...grid(26.18, 55.58, index, 6, 0.075, 0.065), speed: 22, role: 'surface_raider', route: redSurfaceRoute }));
formations.push({ leader: 'Khanjar', members: ['Falakhon', 'Tsunami 1', 'Tsunami 2'] });
formations.push({ leader: 'IRIS Jamaran', members: ['IRIS Damavand', 'Shamshir', 'Neyzeh', 'Tabarzin', 'Tsunami 3'] });
addSeries('red', 'Fateh Patrol', 'Fateh', 3, { lat: 25.78, lon: 55.66 }, { altitude: -45, speed: 5, role: 'submarine', route: [point(25.92, 55.82, -50, 5), point(26.02, 56.00, -55, 5)], columns: 3 });
addSeries('red', 'Kilo Patrol', 'Pr 877EKM Paltus(Iran)', 2, { lat: 25.54, lon: 56.08 }, { altitude: -90, speed: 5, role: 'submarine', route: [point(25.72, 56.22, -90, 5), point(25.90, 56.36, -90, 5)], columns: 2 });

const redCapRoute = [point(26.72, 56.78, 7600, 410, 'WaitForGroup,AutoAttack'), point(26.18, 55.62, 7600, 410, 'AirPatrolArea,AutoAttack'), point(26.55, 56.42, 7600, 410, 'AutoAttack')];
addSeries('red', 'Shahin', 'F-14A', 4, { lat: 26.88, lon: 56.92 }, { altitude: 7600, speed: 420, role: 'fighter', route: redCapRoute, columns: 4 });
addSeries('red', 'Fulcrum Reserve', 'MiG-29', 10, { lat: 27.00, lon: 56.72 }, { altitude: 7200, speed: 420, role: 'fighter', route: redCapRoute, columns: 5 });
const redStrikeRoute = [point(26.70, 56.42, 7000, 410, 'WaitForGroup,AutoAttack'), point(26.22, 56.05, 5500, 420, 'GroundStrike,AutoAttack'), point(26.55, 56.62, 7000, 390, 'AutoAttack')];
addSeries('red', 'Fencer Reserve', 'Su-24M', 8, { lat: 27.04, lon: 56.48 }, { altitude: 7000, speed: 410, role: 'strike', route: redStrikeRoute, columns: 4 });
addSeries('red', 'Persian Orion', 'P-3F Orion', 2, { lat: 26.82, lon: 56.58 }, { altitude: 5500, speed: 300, role: 'maritime_patrol', route: patrolRoute, setup: 'T1 12', columns: 2 });

const redGround = [];
function redSite(name, className, lat, lon, role = 'ground_defense') {
  add('red', { name, className, lat, lon, altitude: 10, speed: 0, role, visible: role === 'coastal_strike' });
  redGround.push(name);
}
redSite('Tunb Khordad', 'Khordad-15', 26.270, 55.306, 'island_defense');
redSite('Tunb Watch', 'Generic Mobile Radar Post 170', 26.276, 55.299, 'island_defense');
redSite('Tunb Shilka 1', 'ZSU-23-4M4 Biryusa', 26.263, 55.296, 'island_defense');
redSite('Tunb Shilka 2', 'ZSU-23-4M4 Biryusa', 26.267, 55.314, 'island_defense');
redSite('Tunb Armor 1', 'T-72 MBT', 26.272, 55.316, 'island_defense');
redSite('Tunb Armor 2', 'T-72 MBT', 26.279, 55.310, 'island_defense');
for (let i = 0; i < 3; i += 1) redSite(`Bastion ${i + 1}`, 'K-300P Bastion-P', 26.80 + i * 0.09, 56.28 + i * 0.10, 'coastal_strike');
for (let i = 0; i < 3; i += 1) redSite(`Pantsir ${i + 1}`, 'Pantsir-S1', 26.805 + i * 0.09, 56.29 + i * 0.10);
redSite('S-300 Site North', 'S-300PMU-2', 27.04, 56.86);
for (let i = 0; i < 3; i += 1) redSite(`Khordad Coast ${i + 1}`, 'Khordad-15', 26.72 + i * 0.12, 56.52 + i * 0.11);
for (let i = 0; i < 6; i += 1) redSite(`Shahed Battery ${i + 1}`, 'Shahed OWA TEL', 26.66 + Math.floor(i / 3) * 0.13, 56.18 + (i % 3) * 0.16, 'coastal_strike');
redSite('Coastwatch North', 'Generic Radar Post 300', 26.93, 56.63);
redSite('Coastwatch West', 'Generic Mobile Radar Post 220', 26.73, 56.08);

// Place every mainland system on verified inland points. The sparse Natural Earth
// coastline is deliberately treated as authoritative by the project validator.
const coastSlots = [
  [26.72, 57.10], [26.72, 57.15], [26.745, 57.075], [26.745, 57.125],
  [26.77, 56.00], [26.77, 57.10], [26.77, 57.15], [26.795, 56.025],
  [26.795, 57.075], [26.795, 57.125], [26.82, 56.00], [26.82, 56.05],
  [26.82, 57.10], [26.82, 57.15], [26.845, 56.025], [26.845, 56.075],
  [26.845, 57.05], [26.845, 57.125],
];
sides.red.filter((unit) => unit.domain === 'ground' && unit.role !== 'island_defense').forEach((unit, index) => {
  [unit.lat, unit.lon] = coastSlots[index];
});

const merchantClasses = ['Container Ship', 'Oil Tanker', 'General Cargo', 'Chemical Tanker'];
for (let i = 0; i < 15; i += 1) {
  add('neutral', {
    name: `Merchant ${String(i + 1).padStart(2, '0')}`,
    className: merchantClasses[i % merchantClasses.length],
    ...grid(25.72, 57.12, i, 5, 0.055, 0.10),
    speed: 11,
    role: 'merchant',
    route: [point(25.88, 56.72, 0, 11), point(26.05, 56.38, 0, 11), point(26.21, 56.04, 0, 11)],
    visible: true,
  });
}

function reposition(name, lat, lon, route = []) {
  const unit = [...sides.blue, ...sides.red, ...sides.neutral].find((candidate) => candidate.name === name);
  if (!unit) throw new Error(`Cannot reposition missing unit: ${name}`);
  unit.lat = lat;
  unit.lon = lon;
  unit.route = route;
}

// Preserve the already-audited Turn 7 convoy lanes exactly.
const auditedBlue = {
  'HMS Diamond': [26.030, 57.090, [[26.211, 56.815], [26.436, 56.550], [26.466, 56.400], [26.446, 56.120], [26.446, 55.820]]],
  'HMS Richmond': [25.920, 57.200, [[26.199, 56.815], [26.424, 56.550], [26.454, 56.400], [26.434, 56.120], [26.434, 55.820]]],
  'RFA Fort Victoria': [25.868, 57.108, [[26.176, 56.800], [26.401, 56.535], [26.431, 56.385], [26.411, 56.100], [26.411, 55.800]]],
  'RFA Tidespring': [25.832, 57.072, [[26.156, 56.770], [26.391, 56.525], [26.416, 56.380], [26.396, 56.080], [26.396, 55.780]]],
  'USCGC Stone': [25.900, 57.000, [[26.152, 56.770], [26.387, 56.525], [26.412, 56.380], [26.392, 56.080], [26.392, 55.780]]],
  'USNS Amelia Earhart': [25.958, 57.018, [[26.184, 56.800], [26.409, 56.535], [26.439, 56.385], [26.419, 56.100], [26.419, 55.800]]],
  'USNS Cesar Chavez': [25.922, 56.982, [[26.164, 56.770], [26.399, 56.525], [26.424, 56.380], [26.404, 56.080], [26.404, 55.780]]],
  'USNS Guadalupe': [25.877, 57.027, [[26.160, 56.770], [26.395, 56.525], [26.420, 56.380], [26.400, 56.080], [26.400, 55.780]]],
  'USNS John Ericsson': [25.913, 57.063, [[26.180, 56.800], [26.405, 56.535], [26.435, 56.385], [26.415, 56.100], [26.415, 55.800]]],
  'USS Arleigh Burke': [25.785, 57.045, [[26.134, 56.770], [26.384, 56.530], [26.414, 56.380], [26.394, 56.080], [26.394, 55.780]]],
  'USS Chosin': [25.975, 57.145, [[26.205, 56.815], [26.430, 56.550], [26.460, 56.400], [26.440, 56.120], [26.440, 55.820]]],
  'USS Devastator': [25.980, 56.925, [[26.168, 56.770], [26.403, 56.525], [26.428, 56.380], [26.408, 56.080], [26.408, 55.780]]],
  'USS Dextrous': [26.015, 56.955, [[26.188, 56.800], [26.413, 56.535], [26.443, 56.385], [26.423, 56.100], [26.423, 55.800]]],
  'USS Mason': [25.895, 56.935, [[26.146, 56.770], [26.396, 56.530], [26.426, 56.380], [26.406, 56.080], [26.406, 55.780]]],
  'USS Tempest': [25.945, 57.075, [[26.172, 56.800], [26.397, 56.535], [26.427, 56.385], [26.407, 56.100], [26.407, 55.800]]],
  'USS Thomas Hudner': [25.840, 56.990, [[26.140, 56.769], [26.390, 56.529], [26.420, 56.379], [26.400, 56.079], [26.400, 55.779]]],
};
for (const [name, [lat, lon, rawRoute]] of Object.entries(auditedBlue)) {
  const speed = sides.blue.find((unit) => unit.name === name).speed;
  reposition(name, lat, lon, rawRoute.map(([wpLat, wpLon]) => point(wpLat, wpLon, 0, speed)));
}
reposition('USS George H.W. Bush', 25.323411, 58.113014, [point(25.40, 57.95, 0, 16), point(25.55, 57.75, 0, 16), point(25.35, 58.05, 0, 16)]);

const extraBlueSurface = ['USS Iwo Jima', 'USS America', 'USS Arlington', 'HMS Albion'];
const extraBlueSlots = [[25.20, 57.625], [25.20, 57.675], [25.20, 57.725], [25.20, 57.775]];
extraBlueSurface.forEach((name, index) => reposition(name, ...extraBlueSlots[index]));
const landingNames = ['Surf Rider 1', 'Surf Rider 2', 'Surf Rider 3', 'Surf Rider 4', 'Beachmaster 1', 'Beachmaster 2'];
const landingSlots = [[26.225, 55.600], [26.225, 55.675], [26.225, 55.750], [26.275, 55.600], [26.275, 55.675], [26.275, 55.750]];
landingNames.forEach((name, index) => reposition(name, ...landingSlots[index]));

const redSurfaceSlots = [[26.20, 56.525], [26.20, 56.600], [26.20, 56.675], [26.20, 56.750], [26.20, 56.825], [26.20, 56.900], [26.25, 56.525], [26.25, 56.600], [26.25, 56.675], [26.25, 56.750], [26.25, 56.825], [26.25, 56.900]];
redShips.forEach(([name], index) => reposition(name, ...redSurfaceSlots[index]));

const neutralSlots = [[25.20, 57.825], [25.20, 57.875], [25.20, 57.925], [25.20, 57.975], [25.20, 58.025], [25.20, 58.075], [25.20, 58.125], [25.20, 58.175], [25.20, 58.225], [25.20, 58.275], [25.25, 57.525], [25.25, 57.625], [25.25, 57.675], [25.25, 57.725], [25.25, 57.775]];
sides.neutral.forEach((unit, index) => reposition(unit.name, ...neutralSlots[index]));

const allUnits = [...sides.blue, ...sides.red, ...sides.neutral];
if (sides.blue.length !== 100 || sides.red.length !== 65 || sides.neutral.length !== 15 || allUnits.length !== 180) {
  throw new Error(`ORBAT count mismatch: blue=${sides.blue.length}, red=${sides.red.length}, neutral=${sides.neutral.length}`);
}

function tasksFor(unit) {
  if (unit.domain === 'air') return ['Aircraft1', ...(unit.role === 'tanker' || unit.role === 'aew' || unit.role === 'air_assault' ? [] : ['AutoAttack']), 'AirEvade', 'Nav'];
  if (unit.domain === 'ship') return ['Ship1', ...(unit.side === 'neutral' ? [] : ['ShipDefense', 'AutoAttack']), 'Nav'];
  if (unit.domain === 'sub') return ['Submarine1', 'SubmarineAttack', 'SubmarineEvade', 'Nav'];
  return ['Ground1', ...(unit.role === 'lodgment' || unit.role === 'merchant' ? [] : ['GroundDefense', 'AutoAttack'])];
}

function renderUnit(unit, alliance) {
  const lines = [
    '    unit = SM.GetDefaultUnit()',
    `    unit.className = ${q(unit.className)}`,
    `    unit.unitName = ${q(unit.name)}`,
    `    unit.SetPosition(${f(unit.lat)}, ${f(unit.lon)}, ${f(unit.altitude)})`,
    `    unit.heading = ${f(unit.heading)}`,
    `    unit.speed = ${f(unit.speed)}`,
    '    unit.cost = 0.0',
    `    SM.AddUnitToAlliance(unit, ${alliance})`,
  ];
  if (unit.visible) lines.push('    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)');
  for (const launcher of unit.loadout.launchers) lines.push(`    SM.SetUnitLauncherItem(unit.unitName, ${launcher.launcherId}, ${q(launcher.item)}, ${launcher.quantity})`);
  lines.push('    UI = SM.GetUnitInterface(unit.unitName)');
  lines.push(`    UI.SetFuelFraction(${f(unit.fuel)})`);
  if (!['convoy', 'merchant', 'air_assault', 'tanker'].includes(unit.role)) lines.push('    UI.SetAllSensorState(1)');
  for (const magazine of unit.loadout.magazines) lines.push(`    SM.AddToUnitMagazine(unit.unitName, ${q(magazine.item)}, ${magazine.quantity})`);
  tasksFor(unit).forEach((task, index) => lines.push(`    UI.AddTask(${q(task)}, ${f(index + 1)}, ${task === 'AutoAttack' ? 0 : 3})`));
  if (unit.landingTarget) {
    lines.push('    BB = UI.GetBlackboardInterface()');
    lines.push(`    BB.Write('LandTarget', ${q(unit.landingTarget)})`);
  }
  unit.route.forEach((waypoint, index) => {
    lines.push(`    UI.add_waypoint_advanced(${f(waypoint.lat)}, ${f(waypoint.lon)}, ${f(waypoint.altitude)}, ${f(waypoint.speed || unit.speed)})`);
    if (waypoint.tasks) lines.push(`    UI.SetNavWaypointTasks(${index}, ${q(waypoint.tasks)})`);
  });
  return lines.join('\n');
}

function simpleGoal(type, targets, quantity, variable) {
  return [`    goal_temp = SM.${type}('')`, ...targets.map((name) => `    goal_temp.AddTarget(${q(name)})`), `    goal_temp.SetQuantity(${quantity})`, `    ${variable} = goal_temp`].join('\n');
}

const blueGoals = [
  { type: 'ProtectGoal', targets: convoy.map(([name]) => name), quantity: 5, label: 'convoy survival' },
  { type: 'ProtectGoal', targets: ['USS Iwo Jima', 'USS America', 'USS Arlington', 'HMS Albion', 'Tunb Expeditionary LZ', 'Pathfinder 1', 'Pathfinder 2', 'Pathfinder 3', 'Rampart 1', 'Rampart 2'], quantity: 7, label: 'island lodgment' },
  { type: 'DestroyGoal', targets: ['Tunb Khordad', 'Tunb Watch', 'Tunb Shilka 1', 'Tunb Shilka 2', 'Tunb Armor 1', 'Tunb Armor 2'], quantity: 4, label: 'island defenses' },
  { type: 'DestroyGoal', targets: redShips.map(([name]) => name).concat(['Fateh Patrol 1', 'Fateh Patrol 2', 'Fateh Patrol 3', 'Kilo Patrol 1', 'Kilo Patrol 2']), quantity: 8, label: 'maritime interdiction' },
  { type: 'DestroyGoal', targets: ['Bastion 1', 'Bastion 2', 'Bastion 3', 'Pantsir 1', 'Pantsir 2', 'Pantsir 3', 'S-300 Site North', 'Khordad Coast 1', 'Khordad Coast 2', 'Khordad Coast 3', 'Coastwatch North', 'Coastwatch West'], quantity: 7, label: 'coastal suppression' },
  { type: 'ProtectGoal', targets: Array.from({ length: 15 }, (_, i) => `Merchant ${String(i + 1).padStart(2, '0')}`), quantity: 12, label: 'civilian protection' },
];

const source = `# Scenario version: 0.2.1
# Generated for GCB Horizon build 25411882; database schema ${db.schemaVersion}
from math import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Island Lance'
    d['description'] = """Campaign Turn 7. A 180-entity, multi-axis operation replaces the repetitive Strait gauntlet with simultaneous island air assault, convoy protection, coastal suppression, maritime interdiction, counter-air, and civilian deconfliction missions."""
    d['author'] = 'Dynamic Campaign Mission Generator'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'ships3.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 180
    d['scenarioId'] = 'island_lance_001'
    return d


def CreateScenario(SM):
    SM.SetScenarioInfo(ScenarioInfo())
    SM.CreateAlliance(1, 'Blue')
    SM.AddAllianceCountry(1, 'USA')
    SM.AddAllianceCountry(1, 'UK')
    SM.SetAlliancePlayable(1, 1)
    SM.CreateAlliance(2, 'Red')
    SM.AddAllianceCountry(2, 'Iran')
    SM.SetAlliancePlayable(2, 0)
    SM.CreateAlliance(3, 'Neutral')
    SM.AddAllianceCountry(3, 'Neutral')
    SM.SetAlliancePlayable(3, 0)
    SM.SetAllianceRelationship(1, 2, 'Hostile')
    SM.SetAllianceRelationship(1, 3, 'Neutral')
    SM.SetAllianceRelationship(2, 3, 'Neutral')
    SM.SetUserAlliance(1)
    SM.SetDateTime(2026, 5, 23, 2, 30, 0)
    SM.SetSeaState(3)
    SM.SetSVP('0.000000,1521.000000,3.000000,1480.000000,20.000000,1485.000000,100.000000,1500.000000,200.000000,1520.000000,300.000000,1530.000000')
    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>\n\nNarrow Furnace preserved the sealift but lost both Lancers and left the Iranian coastal belt largely intact. A reinforced amphibious ready group will now seize a lodgment on Greater Tunb while the convoy completes passage and carrier/land aviation suppress the mainland network. Neutral shipping remains in the battlespace.\n\n<color=#00a8ff>MISSION</color>\n\nExecute six linked missions at once: preserve five convoy auxiliaries; establish the Greater Tunb lodgment; suppress four island-defense nodes; interdict eight hostile maritime units; neutralize seven mainland kill-chain nodes; and protect at least twelve neutral merchants.\n\n<color=#00a8ff>EXECUTION</color>\n\nOsprey and King flights form on the southern approach with Tiger escort and Viper/Venom gunships. Razor/Growler/Viper Strike remain at standoff against the mainland IADS. Poseidon, Romeo, and the submarines isolate the eastern approaches. Do not repeat Narrow Furnace by driving strike aircraft into surviving FAC gun envelopes.\n\n<color=#00a8ff>NEW BUILD NOTES</color>\n\nUse group auto-attack and formation-leader selection to control packages. Improved grounding avoidance should help surface groups, but the player remains responsible for spacing and route changes. Anti-air gun ranges were corrected in this build; respect the displayed envelopes.""")
    SM.SetSimpleBriefing(2, """Contest the Greater Tunb lodgment, break the convoy and amphibious force, and exploit the mainland IADS to fragment BLUE's simultaneous packages. Preserve mobile launchers where possible.""")

    ##############################
    ### Alliance 1 - BLUE (100)
    ##############################

${sides.blue.map((unit) => renderUnit(unit, 1)).join('\n\n')}

    ##############################
    ### Alliance 2 - RED (65)
    ##############################

${sides.red.map((unit) => renderUnit(unit, 2)).join('\n\n')}

    ##############################
    ### Alliance 3 - NEUTRAL (15)
    ##############################

${sides.neutral.map((unit) => renderUnit(unit, 3)).join('\n\n')}

    ##############################
    ### Initial formations
    ##############################

${formations.flatMap((formation) => formation.members.map((member) => `    UI = SM.GetUnitInterface(${q(member)})\n    UI.SetFormationLeader(SM.GetUnitIdByName(${q(formation.leader)}))\n    UI.SetFormationMode(1)`)).join('\n')}

    ##############################
    ### Multi-mission goals
    ##############################

${blueGoals.map((goal, index) => simpleGoal(goal.type, goal.targets, goal.quantity, `blue_${index}`)).join('\n\n')}
    goal_temp = SM.CompoundGoal(0)
${blueGoals.map((_, index) => `    goal_temp.AddGoal(blue_${index})`).join('\n')}
    SM.SetAllianceGoal(1, goal_temp)

${simpleGoal('DestroyGoal', ['USS Iwo Jima', 'USS America', 'USS Arlington', 'HMS Albion', 'Tunb Expeditionary LZ', ...convoy.map(([name]) => name)], 5, 'red_strike')}
    SM.SetAllianceGoal(2, red_strike)

${simpleGoal('ProtectGoal', Array.from({ length: 15 }, (_, i) => `Merchant ${String(i + 1).padStart(2, '0')}`), 10, 'neutral_survival')}
    SM.SetAllianceGoal(3, neutral_survival)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)
    SM.SetAllianceROEByType(2, 2, 2, 2, 2)
    SM.SetAllianceROEByType(3, 0, 0, 0, 0)
`;

const roleCounts = {};
for (const unit of allUnits) roleCounts[unit.role] = (roleCounts[unit.role] || 0) + 1;
const manifest = {
  scenario_id: 'island_lance_001',
  scenario_name: 'Operation Island Lance',
  campaign_turn: 7,
  baseline: { scenario: 'Operation Crossed Sabers', entities: 45, multiplier: 4, target_entities: 180 },
  generated: { utc: new Date().toISOString(), database_schema_version: db.schemaVersion, entities: allUnits.length },
  sides: { blue: sides.blue.length, red: sides.red.length, neutral: sides.neutral.length },
  mission_threads: [
    'Greater Tunb air assault and lodgment', 'legacy convoy completion', 'mainland SEAD and strike',
    'surface/subsurface maritime interdiction', 'counter-air and escort', 'neutral merchant deconfliction',
  ],
  role_counts: roleCounts,
  objectives: { blue: blueGoals, red: { destroy_quantity: 5 }, neutral: { protect_quantity: 10 } },
  units: allUnits.map((unit) => ({ side: unit.side, unit_name: unit.name, platform_class: unit.className, domain: unit.domain, role: unit.role, loadout_setup: unit.loadout.setupName })),
};

fs.writeFileSync(outputPath, source);
fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
db.close();
process.stdout.write(`Generated ${outputPath} with ${allUnits.length} entities (BLUE ${sides.blue.length}, RED ${sides.red.length}, NEUTRAL ${sides.neutral.length}).\n`);
