'use strict';

const fs = require('node:fs/promises');
const path = require('node:path');

const SOURCES = [
  'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_land.geojson',
  'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_minor_islands.geojson',
];
const OUTPUT_PATH = path.resolve(__dirname, '..', 'renderer', 'data', 'global-land.geojson');

async function main() {
  const featureCollections = await Promise.all(SOURCES.map(async (source) => {
    const response = await fetch(source);
    if (!response.ok) throw new Error(`Unable to download ${source}: HTTP ${response.status}`);
    return response.json();
  }));
  const features = featureCollections.flatMap((collection) => collection.features).map((feature) => ({
    type: 'Feature',
    properties: {},
    geometry: feature.geometry,
  }));
  const output = {
    type: 'FeatureCollection',
    metadata: {
      title: 'Natural Earth 1:10m global land and minor islands',
      source: 'Natural Earth public-domain 1:10m land and minor-islands datasets',
      sourceUrls: SOURCES,
      generatedAt: new Date().toISOString(),
      bounds: { west: -180, south: -90, east: 180, north: 90 },
    },
    features,
  };
  await fs.mkdir(path.dirname(OUTPUT_PATH), { recursive: true });
  await fs.writeFile(OUTPUT_PATH, `${JSON.stringify(output)}\n`, 'utf8');
  const bytes = (await fs.stat(OUTPUT_PATH)).size;
  console.log(`Wrote ${features.length} global land features (${bytes} bytes) to ${OUTPUT_PATH}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
