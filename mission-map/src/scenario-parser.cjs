'use strict';

function readString(source, key) {
  const triple = new RegExp(`d\\['${key}'\\]\\s*=\\s*(?:[rubfRUBF]*)\"\"\"([\\s\\S]*?)\"\"\"`);
  const single = new RegExp(`d\\['${key}'\\]\\s*=\\s*(['\"])(.*?)\\1`);
  return triple.exec(source)?.[1]?.trim() ?? single.exec(source)?.[2]?.trim() ?? '';
}

function parseNumberList(value) {
  return value.split(',').map((part) => Number(part.trim()));
}

function decimalVersionAtLeast(version, minimum) {
  const left = String(version || '0').split('.').map(Number);
  const right = String(minimum).split('.').map(Number);
  for (let index = 0; index < Math.max(left.length, right.length); index += 1) {
    const delta = (left[index] || 0) - (right[index] || 0);
    if (delta !== 0) return delta > 0;
  }
  return true;
}

function distanceScore(point, reference) {
  if (!reference) return 0;
  const meanLat = ((point.lat + reference.lat) / 2) * Math.PI / 180;
  const x = (point.lng - reference.lng) * Math.cos(meanLat);
  const y = point.lat - reference.lat;
  return Math.hypot(x, y);
}

function choosePositionConvention(rawPositions, version, theaterCenter, waypoints) {
  if (decimalVersionAtLeast(version, '0.2.1')) {
    return { order: 'lat-lng', reason: `scenario version ${version}` };
  }

  const waypointReference = waypoints.length
    ? {
        lat: waypoints.reduce((sum, point) => sum + point.lat, 0) / waypoints.length,
        lng: waypoints.reduce((sum, point) => sum + point.lng, 0) / waypoints.length,
      }
    : null;
  const reference = theaterCenter || waypointReference;
  if (!reference || rawPositions.length === 0) {
    return { order: 'lat-lng', reason: 'default; no geographic reference found' };
  }

  const latLngScore = rawPositions.reduce(
    (sum, point) => sum + distanceScore({ lat: point.first, lng: point.second }, reference),
    0,
  );
  const lngLatScore = rawPositions.reduce(
    (sum, point) => sum + distanceScore({ lat: point.second, lng: point.first }, reference),
    0,
  );
  return lngLatScore < latLngScore
    ? { order: 'lng-lat', reason: 'legacy draft inferred from theater/waypoint proximity' }
    : { order: 'lat-lng', reason: 'inferred from theater/waypoint proximity' };
}

function parseScenario(source, filePath = '') {
  const version = /#\s*Scenario version:\s*([^\s]+)/i.exec(source)?.[1] || '';
  const dateMatch = /SM\.SetDateTime\(([^)]+)\)/.exec(source);
  const startMatch = /SM\.SetStartTheater\(([^)]+)\)/.exec(source);
  const theaterValues = startMatch ? parseNumberList(startMatch[1]) : [];
  const theaterCenter = theaterValues.length >= 2
    ? { lng: theaterValues[0], lat: theaterValues[1] }
    : null;

  const allianceNames = new Map();
  for (const match of source.matchAll(/SM\.CreateAlliance\(\s*(\d+)\s*,\s*['\"]([^'\"]+)['\"]\s*\)/g)) {
    allianceNames.set(Number(match[1]), match[2]);
  }

  const units = [];
  let current = null;
  let launcherListTarget = null;
  const flush = () => {
    if (current?.className && current?.name && current?.rawPosition) units.push(current);
    current = null;
    launcherListTarget = null;
  };

  const lines = source.split(/\r?\n/);
  lines.forEach((line, lineIndex) => {
    let match = /unit\.className\s*=\s*['\"]([^'\"]+)['\"]/.exec(line);
    if (match) {
      flush();
      current = { className: match[1], waypoints: [], launcherItems: [], tasks: [], sourceLine: lineIndex + 1 };
      return;
    }
    if (!current) return;

    if (/SM\.SetUnitLauncherList\(\s*unit\.unitName\s*,\s*\[/.test(line)) {
      launcherListTarget = current;
    }
    if (launcherListTarget) {
      for (const itemMatch of line.matchAll(/\(\s*(\d+)\s*,\s*['"]([^'"]+)['"]\s*,\s*(\d+)\s*\)/g)) {
        launcherListTarget.launcherItems.push({
          launcherId: Number(itemMatch[1]),
          item: itemMatch[2],
          quantity: Number(itemMatch[3]),
          sourceLine: lineIndex + 1,
        });
      }
      if (/\]\s*\)/.test(line)) launcherListTarget = null;
    }

    match = /unit\.unitName\s*=\s*['\"]([^'\"]+)['\"]/.exec(line);
    if (match) current.name = match[1];

    match = /unit\.SetPosition\(\s*([-+\d.eE]+)\s*,\s*([-+\d.eE]+)\s*,\s*([-+\d.eE]+)\s*\)/.exec(line);
    if (match) {
      current.rawPosition = {
        first: Number(match[1]),
        second: Number(match[2]),
        altitude: Number(match[3]),
        sourceLine: lineIndex + 1,
      };
    }

    match = /unit\.heading\s*=\s*([-+\d.eE]+)/.exec(line);
    if (match) current.heading = Number(match[1]);
    match = /unit\.speed\s*=\s*([-+\d.eE]+)/.exec(line);
    if (match) current.speed = Number(match[1]);

    match = /SM\.AddUnitToAlliance\(\s*unit\s*,\s*(\d+)\s*\)/.exec(line);
    if (match) current.allianceId = Number(match[1]);

    match = /SM\.SetUnitLauncherItem\(\s*unit\.unitName\s*,\s*(\d+)\s*,\s*['\"]([^'\"]+)['\"]\s*,\s*(\d+)\s*\)/.exec(line);
    if (match) {
      current.launcherItems.push({
        launcherId: Number(match[1]),
        item: match[2],
        quantity: Number(match[3]),
        sourceLine: lineIndex + 1,
      });
    }

    match = /UI\.AddTask\(\s*['\"]([^'\"]+)['\"]/.exec(line);
    if (match) {
      current.tasks.push(match[1]);
      current.domain ||= { Ship1: 'surface', Aircraft1: 'air', Ground1: 'ground' }[match[1]];
    }

    match = /UI\.add_waypoint_advanced\(\s*([-+\d.eE]+)\s*,\s*([-+\d.eE]+)\s*,\s*([-+\d.eE]+)\s*,\s*([-+\d.eE]+)\s*\)/.exec(line);
    if (match) {
      current.waypoints.push({
        lat: Number(match[1]),
        lng: Number(match[2]),
        altitude: Number(match[3]),
        speed: Number(match[4]),
        sourceLine: lineIndex + 1,
      });
    }
  });
  flush();

  const rawPositions = units.map((unit) => unit.rawPosition);
  const allWaypoints = units.flatMap((unit) => unit.waypoints);
  const convention = choosePositionConvention(rawPositions, version, theaterCenter, allWaypoints);

  units.forEach((unit) => {
    unit.position = convention.order === 'lng-lat'
      ? { lat: unit.rawPosition.second, lng: unit.rawPosition.first, altitude: unit.rawPosition.altitude, sourceLine: unit.rawPosition.sourceLine }
      : { lat: unit.rawPosition.first, lng: unit.rawPosition.second, altitude: unit.rawPosition.altitude, sourceLine: unit.rawPosition.sourceLine };
    unit.allianceName = allianceNames.get(unit.allianceId) || `Alliance ${unit.allianceId ?? '?'}`;
    unit.domain ||= 'unknown';
    delete unit.rawPosition;
  });

  const playableSides = readString(source, 'playableSides').split(',').map((side) => side.trim()).filter(Boolean);
  return {
    filePath,
    fileName: filePath ? filePath.split(/[\\/]/).pop() : '',
    version,
    coordinateConvention: convention,
    info: {
      name: readString(source, 'name') || 'Untitled scenario',
      description: readString(source, 'description'),
      dateLabel: readString(source, 'date'),
      playableSides,
    },
    dateTime: dateMatch ? parseNumberList(dateMatch[1]) : [],
    theaterCenter,
    alliances: Array.from(allianceNames, ([id, name]) => ({ id, name })),
    units,
  };
}

module.exports = { parseScenario, choosePositionConvention, decimalVersionAtLeast };
