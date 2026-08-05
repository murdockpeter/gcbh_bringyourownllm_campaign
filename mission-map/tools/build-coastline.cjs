'use strict';

const fs = require('node:fs/promises');
const path = require('node:path');

const SOURCES = [
  'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_land.geojson',
  'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_minor_islands.geojson',
];
const BOUNDS = { west: 54, south: 23, east: 60.5, north: 28.8 };
const OUTPUT_PATH = path.resolve(__dirname, '..', 'renderer', 'data', 'hormuz-land.geojson');

function clipRingAgainstBoundary(points, inside, intersect) {
  const output = [];
  for (let index = 0; index < points.length; index += 1) {
    const current = points[index];
    const previous = points[(index + points.length - 1) % points.length];
    const currentInside = inside(current);
    const previousInside = inside(previous);
    if (currentInside) {
      if (!previousInside) output.push(intersect(previous, current));
      output.push(current);
    } else if (previousInside) {
      output.push(intersect(previous, current));
    }
  }
  return output;
}

function clipRing(inputRing) {
  let ring = inputRing.slice(0, -1);
  const verticalIntersection = (longitude, left, right) => {
    const ratio = (longitude - left[0]) / (right[0] - left[0]);
    return [longitude, left[1] + (right[1] - left[1]) * ratio];
  };
  const horizontalIntersection = (latitude, left, right) => {
    const ratio = (latitude - left[1]) / (right[1] - left[1]);
    return [left[0] + (right[0] - left[0]) * ratio, latitude];
  };
  ring = clipRingAgainstBoundary(ring, ([lng]) => lng >= BOUNDS.west, (a, b) => verticalIntersection(BOUNDS.west, a, b));
  ring = clipRingAgainstBoundary(ring, ([lng]) => lng <= BOUNDS.east, (a, b) => verticalIntersection(BOUNDS.east, a, b));
  ring = clipRingAgainstBoundary(ring, ([, lat]) => lat >= BOUNDS.south, (a, b) => horizontalIntersection(BOUNDS.south, a, b));
  ring = clipRingAgainstBoundary(ring, ([, lat]) => lat <= BOUNDS.north, (a, b) => horizontalIntersection(BOUNDS.north, a, b));
  if (ring.length < 3) return [];
  ring.push([...ring[0]]);
  return ring;
}

function ringArea(ring) {
  return Math.abs(ring.reduce((sum, point, index) => {
    const next = ring[(index + 1) % ring.length];
    return sum + point[0] * next[1] - next[0] * point[1];
  }, 0) / 2);
}

function clipPolygon(rings) {
  const clippedOuter = clipRing(rings[0]);
  if (!clippedOuter.length || ringArea(clippedOuter) < 1e-8) return null;
  const holes = rings.slice(1).map(clipRing).filter((ring) => ring.length && ringArea(ring) >= 1e-8);
  return [clippedOuter, ...holes];
}

function clipGeometry(geometry) {
  const polygons = geometry.type === 'Polygon' ? [geometry.coordinates] : geometry.coordinates;
  const clipped = polygons.map(clipPolygon).filter(Boolean);
  if (!clipped.length) return null;
  return clipped.length === 1
    ? { type: 'Polygon', coordinates: clipped[0] }
    : { type: 'MultiPolygon', coordinates: clipped };
}

async function main() {
  const featureCollections = await Promise.all(SOURCES.map(async (source) => {
    const response = await fetch(source);
    if (!response.ok) throw new Error(`Unable to download ${source}: HTTP ${response.status}`);
    return response.json();
  }));
  const features = featureCollections
    .flatMap((collection) => collection.features)
    .map((feature) => ({ type: 'Feature', properties: {}, geometry: clipGeometry(feature.geometry) }))
    .filter((feature) => feature.geometry);
  const output = {
    type: 'FeatureCollection',
    metadata: {
      title: 'Natural Earth 1:10m land clipped to the GCBH Hormuz campaign area',
      source: 'Natural Earth public-domain 1:10m land and minor-islands datasets',
      sourceUrls: SOURCES,
      generatedAt: new Date().toISOString(),
      bounds: BOUNDS,
    },
    features,
  };
  await fs.mkdir(path.dirname(OUTPUT_PATH), { recursive: true });
  await fs.writeFile(OUTPUT_PATH, `${JSON.stringify(output)}\n`, 'utf8');
  const bytes = (await fs.stat(OUTPUT_PATH)).size;
  console.log(`Wrote ${features.length} clipped land features (${bytes} bytes) to ${OUTPUT_PATH}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
