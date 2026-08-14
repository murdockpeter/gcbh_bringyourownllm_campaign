const fs = require('node:fs');
const path = require('node:path');

const outputPath = path.resolve(__dirname, '..', 'scenarios', 'operation_resolute_passage.py');

const westbound = [
  [25.86, 57.06, 0, 0],
  [26.40, 56.52, 0, 0],
  [26.42, 56.38, 0, 0],
  [26.40, 55.78, 0, 0],
  [26.38, 55.76, 0, 0],
];

const burkeLoadout = [
  [0, 'RIM-174A', 8], [1, 'RIM-156', 12], [2, 'RUM-139 Mod4 ASROC', 6],
  [3, 'RIM-162B', 16], [4, 'RIM-162B', 16], [5, '20mm mark 244-0 ELC', 97],
  [6, '20mm mark 244-0 ELC', 97], [7, 'RGM-84F Harpoon', 4], [8, 'RGM-84F Harpoon', 4],
  [9, '127mm mk 127 HE-CVT mk 67', 20], [10, 'Mk-54', 3], [11, 'Mk-54', 3],
];
const burke3Loadout = [
  [0, 'RIM-174A', 16], [1, 'RIM-162B', 64], [2, 'RUM-139 Mod4 ASROC', 8],
  [3, '20mm mark 244-0 ELC', 97], [4, '20mm mark 244-0 ELC', 97],
  [5, 'RGM-84F Harpoon', 4], [6, 'RGM-84F Harpoon', 4],
  [7, '127mm mk 127 HE-CVT mk 67', 20], [8, 'Mk-54', 3], [9, 'Mk-54', 3],
];

const blue = [];
const red = [];

function add(side, spec) {
  (side === 1 ? blue : red).push({ side, ...spec });
}

function surface(name, className, lat, lon, speed, launchers = [], options = {}) {
  return {
    name, className, lat, lon, alt: 0, heading: options.heading ?? 285, speed,
    launchers,
    magazines: options.magazines ?? [],
    tasks: options.tasks ?? [['Ship1', 2, 3], ['ShipDefense', 3, 3], ['Nav', 1, 0]],
    waypoints: options.waypoints ?? westbound,
    visible: options.visible,
    sensors: options.sensors ?? [],
  };
}

function aircraft(name, className, lat, lon, alt, speed, launchers, waypoints, options = {}) {
  return {
    name, className, lat, lon, alt, heading: options.heading ?? 285, speed,
    throttle: options.throttle ?? 0.72,
    launchers,
    tasks: options.tasks ?? [['Aircraft1', 2, 3], ['AutoAttack', 3, 0], ['AirEvade', 4, 3], ['Nav', 1, 0]],
    waypoints,
    loop: options.loop ?? false,
  };
}

const fortLoadout = [[0, '20mm Mark 149-4', 120], [1, '20mm Mark 149-4', 120]];
const cycloneLoadout = [
  [0, '.50 cal bullet', 450], [1, '.50 cal bullet', 450], [2, '.50 cal bullet', 450],
  [3, '.50 cal bullet', 450], [4, '25mm APDS', 250], [5, '25mm APDS', 250], [6, 'FIM-92 Stinger', 4],
];
const type45Loadout = [
  [0, 'ASTER 30', 1], [1, 'ASTER 15', 1], [2, '20mm mark 244-0 ELC', 97],
  [3, '20mm mark 244-0 ELC', 97], [4, '114mm N4A1 HE', 1],
];
const ticoLoadout = [
  [0, 'RIM-174A', 24], [1, 'RIM-156', 24], [2, '20mm mark 244-0 ELC', 97],
  [3, '20mm mark 244-0 ELC', 97], [4, 'RGM-84F Harpoon', 4], [5, 'RGM-84F Harpoon', 4],
  [6, '127mm mk 127 HE-CVT mk 67', 20], [7, '127mm mk 127 HE-CVT mk 67', 20],
  [8, 'Mk-54', 3], [9, 'Mk-54', 3],
];
const legendLoadout = [
  [0, '.50 cal bullet', 400], [1, '.50 cal bullet', 400], [2, '.50 cal bullet', 400],
  [3, '.50 cal bullet', 400], [4, '20mm mark 244-0 ELC', 97], [5, '57mm HE', 100],
];
const type23Loadout = [
  [0, 'Sea Wolf', 6], [1, 'RGM-84F Harpoon', 4], [2, 'RGM-84F Harpoon', 4],
  [3, '114mm N4A1 HE', 16], [4, '30mm/75 GCM-AO3-2 HE', 83], [5, '30mm/75 GCM-AO3-2 HE', 83],
  [6, 'Stingray', 3], [7, 'Stingray', 3],
];
const avengerLoadout = [[0, '.50 cal bullet', 600], [1, '.50 cal bullet', 600]];

// Six ships carry the bulk stores that cannot be replaced by airlift.
add(1, surface('RFA Fort Victoria', 'Fort Victoria AOR', 25.96, 57.10, 12, fortLoadout));
add(1, surface('USNS John Ericsson', 'Henry J Kaiser', 25.86, 57.28, 14));
add(1, surface('USNS Amelia Earhart', 'Lewis and Clark', 25.76, 57.46, 14));
add(1, surface('RFA Tidespring', 'Fort Victoria AOR', 25.58, 57.72, 13, fortLoadout));
add(1, surface('USNS Guadalupe', 'Henry J Kaiser', 25.48, 57.90, 14));
add(1, surface('USNS Cesar Chavez', 'Lewis and Clark', 25.38, 58.08, 14));

add(1, surface('USS Mason', 'Arleigh Burke IIA DDGHM', 26.08, 56.98, 20, burkeLoadout));
add(1, surface('USS Chosin', 'Ticonderoga CG Baseline 4', 25.82, 57.18, 20, ticoLoadout));
add(1, surface('USS Thomas Hudner', 'Arleigh Burke IIA DDGHM', 25.66, 57.55, 22, burkeLoadout));
add(1, surface('USS Arleigh Burke', 'Arleigh Burke III DDGHM', 25.52, 57.82, 22, burke3Loadout));
add(1, surface('HMS Diamond', 'Type 45 DDG', 25.72, 57.32, 21, type45Loadout));
add(1, surface('HMS Richmond', 'Type 23 FF', 25.42, 58.00, 20, type23Loadout));
add(1, surface('USS Tempest', 'Cyclone PBFM', 26.00, 57.06, 22, cycloneLoadout));
add(1, surface('USCGC Stone', 'Legend WMSL', 25.62, 57.64, 19, legendLoadout));

add(1, surface('USS Devastator', 'Avenger MCM', 26.12, 56.88, 10, avengerLoadout));
add(1, surface('USS Dextrous', 'Avenger MCM', 26.04, 56.96, 10, avengerLoadout));

// The carrier remains outside the Strait and provides recovery for Tiger flight.
add(1, surface('USS George H.W. Bush', 'CVN-77 (Nimitz) USS George H.W. Bush', 25.30, 58.15, 12, [], {
  heading: 305,
  tasks: [['Ship1', 2, 3], ['ShipDefense', 4, 3]],
  waypoints: [],
}));

add(1, {
  name: 'Al Dhafra Air Base', className: 'Airstrip(USA)', lat: 24.248, lon: 54.547, alt: 20,
  heading: 130, speed: 0, visible: true,
  magazines: [
    ['Fuel', 400000], ['AIM-120D', 96], ['AIM-9X', 64], ['GBU-39 SDB', 128],
    ['GBU-31A(v)2', 48], ['Chaff-1', 960], ['Flare-1', 960],
  ],
  tasks: [['Ground1', 2, 3]], launchers: [], waypoints: [], sensors: [],
});

const f18Cap = [
  [0, '1400 liter tank', 1], [1, 'AIM-120D', 2], [2, 'AIM-120D', 2], [3, 'AIM-120D', 2],
  [4, 'AIM-9X', 2], [5, 'AIM-9X', 2], [6, '20mm PGU', 46], [7, 'Chaff-1', 25], [8, 'Flare-1', 25],
];
const f15Cap = [
  [0, '600 gallon tank', 1], [1, 'AIM-120D', 2], [2, 'AIM-9X', 2], [4, 'AIM-120D', 4],
  [6, 'Flare-1', 120], [7, 'Chaff-1', 120], [8, '20mm PGU', 46],
];
const f15Strike = [
  [0, 'GBU-39 SDB', 8], [1, 'AIM-120D', 2], [2, 'AIM-9X', 2], [3, 'GBU-12/B', 4],
  [4, 'GBU-31A(v)2', 2], [6, 'Flare-1', 120], [7, 'Chaff-1', 120], [8, '20mm PGU', 46],
];
const capTrack1 = [[26.05, 57.30, 8200, 380], [26.30, 56.75, 8200, 380], [26.05, 57.30, 8200, 380]];
const capTrack2 = [[25.90, 57.50, 8600, 380], [26.20, 56.90, 8600, 380], [25.90, 57.50, 8600, 380]];
const strikeTrack = [[25.65, 56.95, 7600, 390], [26.55, 56.35, 7600, 390], [24.60, 54.90, 6000, 360]];

add(1, aircraft('Tiger 1', 'F/A-18F', 25.95, 58.05, 7800, 360, f18Cap, capTrack1, { loop: true }));
add(1, aircraft('Tiger 2', 'F/A-18F', 25.87, 58.12, 7800, 360, f18Cap, capTrack1, { loop: true }));
add(1, aircraft('Lancer 1', 'F-15E', 24.95, 55.20, 7600, 390, f15Strike, strikeTrack));
add(1, aircraft('Lancer 2', 'F-15E', 24.88, 55.28, 7600, 390, f15Strike, strikeTrack));
add(1, aircraft('Viper 1', 'F-15E', 25.40, 57.30, 8600, 380, f15Cap, capTrack2, { loop: true }));
add(1, aircraft('Viper 2', 'F-15E', 25.32, 57.38, 8600, 380, f15Cap, capTrack2, { loop: true }));
add(1, aircraft('Wildcat 1', 'F-15E', 25.18, 56.15, 7600, 390, f15Strike, strikeTrack));
add(1, aircraft('Wildcat 2', 'F-15E', 25.10, 56.22, 7600, 390, f15Strike, strikeTrack));

const p8Loadout = [
  [0, 'Mk-46 Mod5', 4], [1, 'AGM-84D Harpoon', 4], [5, 'AN/AAQ-24 Nemesis Laser Beam', 100],
  [6, 'Chaff-1', 30], [7, 'Flare-1', 30],
];
const patrolTrack = [[26.10, 57.50, 7600, 280], [25.95, 56.95, 7600, 280], [25.70, 57.60, 7600, 280]];
add(1, aircraft('Broadarrow', 'P-8 MPA', 26.25, 58.05, 7600, 280, p8Loadout, patrolTrack, { loop: true, throttle: 0.58, tasks: [['Aircraft1', 2, 3], ['Nav', 1, 0]] }));
add(1, aircraft('Trident', 'P-8 MPA', 25.95, 58.25, 7600, 280, p8Loadout, patrolTrack, { loop: true, throttle: 0.58, tasks: [['Aircraft1', 2, 3], ['Nav', 1, 0]] }));
add(1, aircraft('Sentinel', 'E-2D', 25.30, 58.20, 8500, 260, [], [[25.40, 57.90, 8500, 260], [25.20, 58.30, 8500, 260]], { loop: true, throttle: 0.55, tasks: [['Aircraft1', 2, 3], ['Nav', 1, 0]] }));
add(1, aircraft('Shell 1', 'KC-135R', 25.10, 58.45, 9000, 300, [], [[25.20, 58.00, 9000, 300], [25.00, 58.50, 9000, 300]], { loop: true, throttle: 0.54, tasks: [['Aircraft1', 2, 3], ['Nav', 1, 0]] }));

// Place the sixteen moving BLUE surface units on the verified 2 nm-clear approach line.
const corridorStarts = [
  [25.380, 58.080], [25.410, 58.016], [25.440, 57.952], [25.470, 57.888],
  [25.500, 57.824], [25.530, 57.760], [25.560, 57.696], [25.590, 57.632],
  [25.620, 57.568], [25.650, 57.504], [25.680, 57.440], [25.710, 57.376],
  [25.740, 57.312], [25.770, 57.248], [25.800, 57.184], [25.830, 57.120],
];
const movingBlueSurface = blue.filter((unit) => unit.alt === 0 && unit.waypoints?.length);
if (movingBlueSurface.length !== corridorStarts.length) throw new Error('Unexpected BLUE surface-route count');
movingBlueSurface.forEach((unit, index) => {
  [unit.lat, unit.lon] = corridorStarts[index];
  unit.waypoints = westbound;
});

const redRetreat = [[26.28, 56.62, 0, 0], [26.45, 56.52, 0, 0]];
const kamanLoadout = [[0, 'RGM-84A Harpoon', 1], [2, '76mm HE-MOM', 40], [3, '40mm HE-T', 20]];
const moudgeLoadout = [[0, '76mm HC', 60], [1, 'Noor', 2], [2, 'Noor', 2], [3, '40mm HE-T', 55], [4, '20mm HE-T x2', 50]];
const osaLoadout = [[0, 'P-20M Rubezh', 4], [1, '30mm OF-83 HE-FRAG', 250], [2, '30mm OF-83 HE-FRAG', 250]];

add(2, surface('Khanjar', 'Kaman FACM', 26.10, 56.95, 24, kamanLoadout, { heading: 300, waypoints: redRetreat, tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['Nav', 1, 0]] }));
add(2, surface('Falakhon', 'Kaman FACM', 26.18, 56.88, 18, [[2, '76mm HE-MOM', 24], [3, '40mm HE-T', 12]], { heading: 305, waypoints: redRetreat, tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['Nav', 1, 0]] }));
add(2, surface('Dagger', 'Kaman FACM', 26.30, 56.78, 26, kamanLoadout, { heading: 135, waypoints: [[26.15, 56.82, 0, 0], [26.02, 56.98, 0, 0]], tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['Nav', 1, 0]] }));
add(2, surface('Scimitar', 'Kaman FACM', 26.38, 56.68, 26, kamanLoadout, { heading: 140, waypoints: [[26.24, 56.75, 0, 0], [26.08, 56.92, 0, 0]], tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['Nav', 1, 0]] }));
add(2, surface('Zolfaghar', 'Kaman FACM', 26.46, 56.58, 25, kamanLoadout, { heading: 145, waypoints: [[26.32, 56.66, 0, 0], [26.16, 56.84, 0, 0]], tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['Nav', 1, 0]] }));
add(2, surface('IRIS Sahand', 'Moudge FFG', 26.55, 56.72, 20, moudgeLoadout, { heading: 150, waypoints: [[26.38, 56.70, 0, 0], [26.20, 56.78, 0, 0]], tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['ShipDefense', 4, 3], ['Nav', 1, 0]] }));
add(2, surface('IRIS Dena', 'Moudge FFG', 26.62, 56.62, 20, moudgeLoadout, { heading: 155, waypoints: [[26.44, 56.64, 0, 0], [26.26, 56.72, 0, 0]], tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['ShipDefense', 4, 3], ['Nav', 1, 0]] }));
add(2, surface('Tsunami 1', 'Pr 205ER Tsunami (Iran)', 26.48, 56.42, 25, osaLoadout, { heading: 105, waypoints: [[26.36, 56.55, 0, 0], [26.22, 56.70, 0, 0]], tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['Nav', 1, 0]] }));
add(2, surface('Tsunami 2', 'Pr 205ER Tsunami (Iran)', 26.56, 56.32, 25, osaLoadout, { heading: 110, waypoints: [[26.42, 56.48, 0, 0], [26.28, 56.64, 0, 0]], tasks: [['Ship1', 2, 3], ['AutoAttack', 3, 0], ['Nav', 1, 0]] }));

// Iranian surface units form a west-to-east blocking line inside the same navigable channel.
const redSurfaceStarts = [
  [26.420, 56.380], [26.419, 56.395], [26.417, 56.410], [26.415, 56.425],
  [26.413, 56.440], [26.411, 56.455], [26.409, 56.470], [26.406, 56.490],
  [26.403, 56.510],
];
const redIntercept = [[26.40, 56.52, 0, 0], [25.86, 57.06, 0, 0]];
const movingRedSurface = red.filter((unit) => unit.alt === 0 && unit.waypoints?.length);
if (movingRedSurface.length !== redSurfaceStarts.length) throw new Error('Unexpected RED surface-route count');
movingRedSurface.forEach((unit, index) => {
  [unit.lat, unit.lon] = redSurfaceStarts[index];
  unit.waypoints = redIntercept;
});

function ground(name, className, lat, lon, launchers, options = {}) {
  return {
    name, className, lat, lon, alt: options.alt ?? 10, heading: options.heading ?? 180, speed: 0,
    launchers, magazines: options.magazines ?? [], visible: options.visible ?? true,
    sensors: options.sensors ?? [], tasks: options.tasks ?? [['Ground1', 2, 3], ['AutoAttack', 3, 0]], waypoints: [],
  };
}

add(2, ground('Bastion 1', 'K-300P Bastion-P', 26.835440, 56.333700, [[0, 'P-800 Oniks', 2]]));
add(2, ground('Bastion 2', 'K-300P Bastion-P', 26.880000, 56.398544, [[0, 'P-800 Oniks', 2]]));
add(2, ground('Bastion 3', 'K-300P Bastion-P', 27.052409, 56.483620, [[0, 'P-800 Oniks', 2]]));
const pantsirLoadout = [[0, '95Ya6', 3], [1, '95Ya6', 3], [2, '95Ya6', 3], [3, '95Ya6', 3], [4, '30mm 3UBR8 APDS', 400]];
add(2, ground('Pantsir 1', 'Pantsir-S1', 26.834632, 56.338093, pantsirLoadout, { sensors: [[0, 1]], tasks: [['Ground1', 2, 3], ['PointDefense', 3, 3], ['AutoAttack', 4, 0]] }));
add(2, ground('Pantsir 2', 'Pantsir-S1', 26.870324, 56.399035, pantsirLoadout, { sensors: [[0, 1]], tasks: [['Ground1', 2, 3], ['PointDefense', 3, 3], ['AutoAttack', 4, 0]] }));
add(2, ground('Pantsir 3', 'Pantsir-S1', 27.053302, 56.482007, pantsirLoadout, { sensors: [[0, 1]], tasks: [['Ground1', 2, 3], ['PointDefense', 3, 3], ['AutoAttack', 4, 0]] }));
add(2, ground('S-300 Site North', 'S-300PMU-2', 27.036039, 56.865368, [[0, '48N6E2', 4], [1, '48N6E2', 4], [2, '48N6E2', 4], [3, '48N6E2', 4]], { sensors: [[0, 1]], tasks: [['Ground1', 2, 3], ['PointDefense', 3, 3], ['AutoAttack', 4, 0]] }));
add(2, ground('Coastwatch 1', 'Generic Radar Post 170', 26.792083, 56.078986, [], { sensors: [[0, 1]], tasks: [['Ground1', 2, 3], ['PointDefense', 3, 3]] }));

add(2, {
  name: 'Bandar Abbas Strip', className: 'Airstrip', lat: 27.08, lon: 56.98, alt: 12,
  heading: 90, speed: 0, launchers: [], visible: false, sensors: [], waypoints: [],
  magazines: [['Fuel', 250000], ['R-27R', 48], ['R-73', 48], ['Kh-59MK', 24], ['Chaff-1', 480], ['Flare-1', 480]],
  tasks: [['Ground1', 2, 3]],
});

const migLoadout = [
  [0, '1520 Liter Tank', 1], [1, 'R-27R', 2], [2, 'R-73', 2], [3, 'R-73', 2],
  [4, '30mm NR-30 HEI', 20], [5, 'Chaff-1', 30], [6, 'Flare-1', 30],
];
const su24Loadout = [
  [0, 'R-60', 2], [1, 'Kh-59MK', 2], [2, 'Kh-29T', 2], [3, 'KAB-500L', 2],
  [4, '23mm AM-23', 6], [5, 'Chaff-1', 30], [6, 'Flare-1', 30],
];
const redCap = [[26.20, 57.05, 7800, 410], [26.85, 56.85, 7800, 410]];
const redStrike = [[26.25, 57.20, 6200, 420], [25.65, 57.55, 6200, 420], [27.00, 56.60, 6200, 420]];
add(2, aircraft('Fulcrum 1', 'MiG-29', 26.85, 56.85, 7800, 410, migLoadout, redCap, { loop: true, heading: 165, throttle: 0.78 }));
add(2, aircraft('Fulcrum 2', 'MiG-29', 26.92, 56.78, 7800, 410, migLoadout, redCap, { loop: true, heading: 168, throttle: 0.78 }));
add(2, aircraft('Fulcrum 3', 'MiG-29', 27.00, 56.72, 8200, 410, migLoadout, redCap, { loop: true, heading: 172, throttle: 0.78 }));
add(2, aircraft('Fulcrum 4', 'MiG-29', 27.06, 56.65, 8200, 410, migLoadout, redCap, { loop: true, heading: 175, throttle: 0.78 }));
add(2, aircraft('Fencer 1', 'Su-24M', 26.95, 56.65, 6200, 420, su24Loadout, redStrike, { heading: 150, throttle: 0.80 }));
add(2, aircraft('Fencer 2', 'Su-24M', 27.00, 56.58, 6200, 420, su24Loadout, redStrike, { heading: 152, throttle: 0.80 }));

if (blue.length !== 30 || red.length !== 24) {
  throw new Error(`Expected 30 BLUE and 24 RED units, found ${blue.length} and ${red.length}`);
}

const q = (value) => JSON.stringify(value);
const f = (value) => Number(value).toFixed(6);

function renderUnit(u) {
  const lines = [
    '    unit = SM.GetDefaultUnit()',
    `    unit.className = ${q(u.className)}`,
    `    unit.unitName = ${q(u.name)}`,
    `    unit.SetPosition(${f(u.lat)}, ${f(u.lon)}, ${f(u.alt ?? 0)})`,
    `    unit.heading = ${f(u.heading ?? 0)}`,
    `    unit.speed = ${f(u.speed ?? 0)}`,
  ];
  if (u.throttle !== undefined) lines.push(`    unit.throttle = ${f(u.throttle)}`);
  lines.push('    unit.cost = 0.0', `    SM.AddUnitToAlliance(unit, ${u.side})`);
  for (const [id, item, qty] of u.launchers ?? []) {
    lines.push(`    SM.SetUnitLauncherItem(unit.unitName, ${id}, ${q(item)}, ${qty})`);
  }
  if (u.visible) lines.push('    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)');
  lines.push('    UI = SM.GetUnitInterface(unit.unitName)');
  for (const [item, qty] of u.magazines ?? []) lines.push(`    SM.AddToUnitMagazine(unit.unitName, ${q(item)}, ${qty})`);
  for (const [id, state] of u.sensors ?? []) lines.push(`    UI.SetSensorState(${id}, ${state})`);
  for (const [task, priority, mode] of u.tasks ?? []) lines.push(`    UI.AddTask(${q(task)}, ${f(priority)}, ${mode})`);
  for (const [lat, lon, alt, speed] of u.waypoints ?? []) {
    lines.push(`    UI.add_waypoint_advanced(${f(lat)}, ${f(lon)}, ${f(alt)}, ${f(speed)})`);
  }
  if (u.loop) lines.push('    UI.SetNavLoopState(True)');
  return `${lines.join('\n')}\n`;
}

const scenario = `# Scenario version: 0.2.1
# Campaign turn 5: generated from the multiplayer outcome of Operation Silver Current
from math import *
from random import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Resolute Passage'
    d['description'] = """Eight hours after the improved Silver Current action, the coalition has a narrow opportunity to reopen Hormuz. All fifteen BLUE platforms survived, while both Iranian Phantom interceptors and the FAC Shamshir were destroyed. The success demonstrated that disciplined standoff tactics can contain the immediate threat.

The opportunity cannot be left unused. Missile-defense reloads, aviation fuel, repair modules, and medical stores for the forward force in Bahrain are aboard six auxiliaries east of the Strait. Airlift cannot move the required fuel or vertical-launch-system reloads, and inventories inside the Gulf will fall below contingency levels before another sealift package can arrive. The convoy must therefore make a westbound passage through Hormuz.

Iran has declared a temporary exclusion zone and reinforced the surviving coastal network with frigates, missile boats, fighters, and strike aircraft. The coalition response remains a corridor-opening operation, not a general attack on Iran."""
    d['author'] = 'OpenAI Codex'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'ships3.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 54
    d['scenarioId'] = 'resolute_passage_001'
    return d


def CreateScenario(SM):
    SM.SetScenarioInfo(ScenarioInfo())

    SM.CreateAlliance(1, 'Blue')
    SM.AddAllianceCountry(1, 'Blue')
    SM.AddAllianceCountry(1, 'USA')
    SM.AddAllianceCountry(1, 'UK')
    SM.SetAlliancePlayable(1, 1)

    SM.CreateAlliance(2, 'Red')
    SM.AddAllianceCountry(2, 'Red')
    SM.AddAllianceCountry(2, 'Iran')
    SM.SetAlliancePlayable(2, 0)

    SM.SetAllianceRelationship(1, 2, 'Hostile')
    SM.SetUserAlliance(1)
    SM.SetDateTime(2026, 5, 22, 14, 0, 0)
    SM.SetSeaState(3)
    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>

Your improved Silver Current action destroyed both hostile Phantoms and Shamshir without losing a BLUE platform. That success has opened a short corridor-reentry window.

Bahrain's forward force will fall below contingency stocks of missile-defense reloads, aviation fuel, repair modules, and medical stores within twenty-four hours. Those supplies are aboard six auxiliaries east of Hormuz. Airlift cannot move the required bulk fuel or VLS reloads. The convoy must pass west through the Strait now, before Iran completes another coastal-force cycle.

Iran has declared an exclusion zone and doubled down with reinforced FAC, frigate, fighter, strike, and coastal-missile elements. National authority permits force necessary to open and hold the navigation corridor; it does not authorize attacks beyond the designated coastal kill chain.

<color=#00a8ff>MISSION</color>

Preserve at least five of the six logistics ships. Destroy at least six of the nine hostile surface combatants. Neutralize at least three designated coastal kill-chain nodes.

<color=#00a8ff>EXECUTION</color>

The convoy and close escorts are already committed westbound. Devastator and Dextrous lead the formation through the traffic corridor. The carrier remains in the Gulf of Oman to recover Tiger flight; Al Dhafra supports the land-based package.

Keep the auxiliaries behind the air-defense screen. Use Broadarrow and Trident to classify surface contacts, then engage from standoff range. Lancer and Wildcat are the shore-strike elements and require manual positive-control target designation. Do not repeat the close FAC engagement from the earlier solo run.

<color=#00a8ff>ROE</color>

Engage hostile aircraft, missiles, and designated attacking surface units. Shore attack is limited to Bastion 1, Bastion 2, Bastion 3, S-300 Site North, and Coastwatch 1.""")
    SM.SetSimpleBriefing(2, 'Red is not playable in this scenario.')

    ##############################
    ### Alliance 1 - corridor force (30 assets)
    ##############################

${blue.map(renderUnit).join('\n')}
    ##############################
    ### Alliance 2 - exclusion force (24 assets)
    ##############################

${red.map(renderUnit).join('\n')}
    ##############################
    ### Goals
    ##############################

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.AddTarget('RFA Tidespring')
    goal_temp.AddTarget('USNS Guadalupe')
    goal_temp.AddTarget('USNS Cesar Chavez')
    goal_temp.SetQuantity(5)
    goal_blue_protect = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Khanjar')
    goal_temp.AddTarget('Falakhon')
    goal_temp.AddTarget('Dagger')
    goal_temp.AddTarget('Scimitar')
    goal_temp.AddTarget('Zolfaghar')
    goal_temp.AddTarget('IRIS Sahand')
    goal_temp.AddTarget('IRIS Dena')
    goal_temp.AddTarget('Tsunami 1')
    goal_temp.AddTarget('Tsunami 2')
    goal_temp.SetQuantity(6)
    goal_blue_surface = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Bastion 1')
    goal_temp.AddTarget('Bastion 2')
    goal_temp.AddTarget('Bastion 3')
    goal_temp.AddTarget('S-300 Site North')
    goal_temp.AddTarget('Coastwatch 1')
    goal_temp.SetQuantity(3)
    goal_blue_shore = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_blue_protect)
    goal_temp.AddGoal(goal_blue_surface)
    goal_temp.AddGoal(goal_blue_shore)
    SM.SetAllianceGoal(1, goal_temp)

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.AddTarget('RFA Tidespring')
    goal_temp.AddTarget('USNS Guadalupe')
    goal_temp.AddTarget('USNS Cesar Chavez')
    goal_temp.SetQuantity(3)
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)
    SM.SetAllianceROEByType(2, 2, 2, 2, 2)
`;

fs.writeFileSync(outputPath, scenario, 'utf8');
console.log(`Generated ${outputPath}`);
console.log(`Units: ${blue.length} BLUE, ${red.length} RED, ${blue.length + red.length} total`);
