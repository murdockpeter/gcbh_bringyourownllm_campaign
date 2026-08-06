'use strict';

function scenarioCenter(scenario) {
  if (scenario.theaterCenter) return scenario.theaterCenter;
  const points = scenario.units?.map((unit) => unit.position).filter(Boolean) || [];
  if (!points.length) return null;
  return {
    lat: points.reduce((sum, point) => sum + point.lat, 0) / points.length,
    lng: points.reduce((sum, point) => sum + point.lng, 0) / points.length,
  };
}

function inferredBounds(theater) {
  const points = theater.safe_water_polygons?.flatMap((polygon) => polygon.points) || [];
  if (!points.length) return null;
  return points.reduce((bounds, [lng, lat]) => ({
    west: Math.min(bounds.west, lng), south: Math.min(bounds.south, lat),
    east: Math.max(bounds.east, lng), north: Math.max(bounds.north, lat),
  }), { west: Infinity, south: Infinity, east: -Infinity, north: -Infinity });
}

function theaterCoversScenario(theater, scenario) {
  const center = scenarioCenter(scenario);
  const bounds = theater.coverage_bounds || inferredBounds(theater);
  if (!center || !bounds) return false;
  return center.lng >= bounds.west && center.lng <= bounds.east
    && center.lat >= bounds.south && center.lat <= bounds.north;
}

function selectTheater(scenario, theaters) {
  return theaters.find((theater) => theaterCoversScenario(theater, scenario)) || null;
}

module.exports = { scenarioCenter, selectTheater, theaterCoversScenario };
