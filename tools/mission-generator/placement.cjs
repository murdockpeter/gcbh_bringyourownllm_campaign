'use strict';

const { GeneratorError } = require('./errors.cjs');

function validPoint(point) {
  return point && Number.isFinite(point.lat) && point.lat >= -90 && point.lat <= 90
    && Number.isFinite(point.lon) && point.lon >= -180 && point.lon <= 180;
}

function jitterPoint(point, jitterNm, rng, label) {
  if (!jitterNm) return { ...point };
  const distance = rng.next(`${label}:distance`) * jitterNm;
  const bearing = rng.next(`${label}:bearing`) * Math.PI * 2;
  const lat = point.lat + (distance * Math.cos(bearing)) / 60;
  const lon = point.lon + (distance * Math.sin(bearing)) / (60 * Math.max(0.2, Math.cos(point.lat * Math.PI / 180)));
  return { ...point, lat: Number(lat.toFixed(6)), lon: Number(lon.toFixed(6)) };
}

function pointFromBox(box, rng, label) {
  if (!box || ![box.south, box.north, box.west, box.east].every(Number.isFinite)) {
    throw new GeneratorError('PLACEMENT_BOX', `Missing or invalid aircraft box for ${label}`);
  }
  return {
    lat: Number((box.south + rng.next(`${label}:lat`) * (box.north - box.south)).toFixed(6)),
    lon: Number((box.west + rng.next(`${label}:lon`) * (box.east - box.west)).toFixed(6)),
    altitude: Number(box.altitude || 7500),
  };
}

function normalizeRoute(route, label) {
  if (!Array.isArray(route) || !route.length || route.some((point) => !validPoint(point))) {
    throw new GeneratorError('PLACEMENT_ROUTE', `${label} must contain valid latitude/longitude points`);
  }
  return route.map((point) => ({ lat: point.lat, lon: point.lon, altitude: Number(point.altitude || 0), speed: Number(point.speed || 0) }));
}

function placeSide(units, side, seed, rng) {
  const placement = seed.placement;
  const surfaceStarts = placement.surface_starts?.[side] || [];
  const surfaceVariants = placement.surface_route_variants?.[side];
  const surfaceRouteSource = surfaceVariants?.length
    ? rng.pick(surfaceVariants, `${side}:surface-route-variant`)
    : placement.surface_routes?.[side];
  const surfaceRoute = surfaceRouteSource ? normalizeRoute(surfaceRouteSource, `${side} surface route`) : [];
  const groundPositions = placement.ground_positions || {};
  const airBox = placement.air_boxes?.[side];
  const airRoutes = placement.air_routes || {};
  const jitterNm = Number(seed.variation?.position_jitter_nm || 0);
  let surfaceIndex = 0;
  return units.map((unit) => {
    let position;
    let route = [];
    if (unit.domain === 'ship' || unit.domain === 'sub') {
      const source = surfaceStarts[surfaceIndex];
      if (!validPoint(source)) throw new GeneratorError('PLACEMENT_SURFACE', `No valid ${side} surface start is available for ${unit.unit_name}`);
      position = jitterPoint({ ...source, altitude: unit.domain === 'sub' ? Number(source.altitude ?? -40) : 0 }, jitterNm, rng, `${side}:${unit.unit_name}:start`);
      route = surfaceRoute.map((point) => ({ ...point, speed: point.speed || unit.speed }));
      surfaceIndex += 1;
    } else if (unit.domain === 'air') {
      position = pointFromBox(airBox, rng, `${side}:${unit.unit_name}:air`);
      let source = airRoutes[unit.role] || airRoutes[side] || [];
      if (source.length && Array.isArray(source[0])) source = rng.pick(source, `${side}:${unit.role}:air-route-variant`);
      route = source.length ? normalizeRoute(source, `${unit.role} air route`).map((point) => ({ ...point, speed: point.speed || unit.speed, altitude: point.altitude || position.altitude })) : [];
    } else {
      const source = groundPositions[unit.unit_name] || groundPositions[unit.platform_class];
      if (!validPoint(source)) throw new GeneratorError('PLACEMENT_GROUND', `No valid ground position is defined for ${unit.unit_name}`);
      position = { ...source, altitude: Number(source.altitude || 10) };
    }
    const visibilityFraction = Number(seed.variation?.contact_visibility_fraction?.[side] || 0);
    if (visibilityFraction < 0 || visibilityFraction > 1) throw new GeneratorError('VARIATION_VISIBILITY', `contact_visibility_fraction.${side} must be between 0 and 1`);
    return {
      ...unit,
      position,
      route,
      heading: Number(position.heading ?? (side === 'blue' ? 285 : 135)),
      navLoop: unit.domain === 'air' && route.length > 1 && ['fighter', 'reconnaissance', 'maritime_patrol', 'tanker'].includes(unit.role),
      alwaysVisible: visibilityFraction > 0 && rng.next(`${side}:${unit.unit_name}:visibility`) < visibilityFraction,
    };
  });
}

function placeUnits(units, seed, rng) {
  return {
    blue: placeSide(units.blue, 'blue', seed, rng),
    red: placeSide(units.red, 'red', seed, rng),
    rejected: units.rejected,
    logistics: units.logistics,
    aviation: units.aviation,
  };
}

module.exports = { validPoint, jitterPoint, pointFromBox, normalizeRoute, placeUnits };
