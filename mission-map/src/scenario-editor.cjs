'use strict';

const fs = require('node:fs/promises');
const path = require('node:path');
const { parseScenario } = require('./scenario-parser.cjs');

const NUMBER = '[-+\\d.eE]+';
const POSITION_PATTERN = new RegExp(`^(\\s*unit\\.SetPosition\\()\\s*${NUMBER}\\s*,\\s*${NUMBER}\\s*,\\s*(.+)$`);
const WAYPOINT_PATTERN = new RegExp(`^(\\s*UI\\.add_waypoint_advanced\\()\\s*${NUMBER}\\s*,\\s*${NUMBER}\\s*,\\s*(.+)$`);

function coordinate(value) {
  const number = Number(value);
  if (!Number.isFinite(number)) throw new Error(`Invalid coordinate: ${value}`);
  return number.toFixed(6);
}

function validateLatLng(edit) {
  if (!Number.isFinite(edit.lat) || edit.lat < -90 || edit.lat > 90) throw new Error('Latitude is outside -90..90.');
  if (!Number.isFinite(edit.lng) || edit.lng < -180 || edit.lng > 180) throw new Error('Longitude is outside -180..180.');
}

function replaceCoordinateLine(line, pattern, first, second, label, sourceLine) {
  const match = pattern.exec(line);
  if (!match) throw new Error(`Line ${sourceLine} is no longer a ${label}; reload before saving.`);
  return `${match[1]}${coordinate(first)}, ${coordinate(second)}, ${match[2]}`;
}

function applyScenarioEdits(source, edits, coordinateOrder) {
  const newline = source.includes('\r\n') ? '\r\n' : '\n';
  const hadFinalNewline = source.endsWith('\n');
  const lines = source.split(/\r?\n/);
  if (hadFinalNewline) lines.pop();

  const normalized = edits.map((edit) => {
    validateLatLng(edit);
    if (!Number.isInteger(edit.sourceLine) || edit.sourceLine < 1 || edit.sourceLine > lines.length) {
      throw new Error(`Invalid source line ${edit.sourceLine}.`);
    }
    return { ...edit };
  }).sort((left, right) => right.sourceLine - left.sourceLine || (left.kind === 'insert-waypoint' ? 1 : -1));

  for (const edit of normalized) {
    const index = edit.sourceLine - 1;
    if (edit.kind === 'position') {
      const first = coordinateOrder === 'lng-lat' ? edit.lng : edit.lat;
      const second = coordinateOrder === 'lng-lat' ? edit.lat : edit.lng;
      lines[index] = replaceCoordinateLine(lines[index], POSITION_PATTERN, first, second, 'SetPosition call', edit.sourceLine);
    } else if (edit.kind === 'waypoint') {
      lines[index] = replaceCoordinateLine(lines[index], WAYPOINT_PATTERN, edit.lat, edit.lng, 'waypoint call', edit.sourceLine);
    } else if (edit.kind === 'insert-waypoint') {
      const targetMatch = WAYPOINT_PATTERN.exec(lines[index]);
      if (!targetMatch) throw new Error(`Line ${edit.sourceLine} is no longer a waypoint insertion target; reload before saving.`);
      const indentation = /^\s*/.exec(lines[index])[0];
      const altitude = Number.isFinite(edit.altitude) ? edit.altitude.toFixed(6) : '0.000000';
      const speed = Number.isFinite(edit.speed) ? edit.speed.toFixed(6) : '0.000000';
      lines.splice(index, 0, `${indentation}UI.add_waypoint_advanced(${coordinate(edit.lat)}, ${coordinate(edit.lng)}, ${altitude}, ${speed})`);
    } else {
      throw new Error(`Unsupported scenario edit kind: ${edit.kind}`);
    }
  }
  return `${lines.join(newline)}${hadFinalNewline ? newline : ''}`;
}

async function saveScenarioEdits(filePath, edits) {
  if (!Array.isArray(edits) || edits.length === 0) throw new Error('No coordinate edits were supplied.');
  if (edits.length > 500) throw new Error('Too many coordinate edits in one save.');
  const source = await fs.readFile(filePath, 'utf8');
  const scenario = parseScenario(source, filePath);
  const updated = applyScenarioEdits(source, edits, scenario.coordinateConvention.order);
  if (updated === source) throw new Error('The edits did not change the scenario.');

  const backupDirectory = path.join(path.dirname(filePath), '_backups');
  await fs.mkdir(backupDirectory, { recursive: true });
  const timestamp = new Date().toISOString().replaceAll(':', '-').replaceAll('.', '-');
  const backupPath = path.join(backupDirectory, `${path.basename(filePath, path.extname(filePath))}.${timestamp}.py`);
  await fs.copyFile(filePath, backupPath);
  try {
    await fs.writeFile(filePath, updated, 'utf8');
  } catch (error) {
    await fs.copyFile(backupPath, filePath);
    throw error;
  }
  return { backupPath, editCount: edits.length };
}

module.exports = { applyScenarioEdits, saveScenarioEdits };
