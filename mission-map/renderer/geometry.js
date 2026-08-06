const EARTH_RADIUS_NM = 3440.065;

export function haversineNm(left, right) {
  const toRadians = (value) => value * Math.PI / 180;
  const dLat = toRadians(right.lat - left.lat);
  const dLng = toRadians(right.lng - left.lng);
  const lat1 = toRadians(left.lat);
  const lat2 = toRadians(right.lat);
  const value = Math.sin(dLat / 2) ** 2
    + Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLng / 2) ** 2;
  return 2 * EARTH_RADIUS_NM * Math.asin(Math.sqrt(value));
}

export function pointInPolygon(point, polygon) {
  let inside = false;
  for (let current = 0, previous = polygon.length - 1; current < polygon.length; previous = current, current += 1) {
    const [currentLng, currentLat] = polygon[current];
    const [previousLng, previousLat] = polygon[previous];
    const crosses = ((currentLat > point.lat) !== (previousLat > point.lat))
      && (point.lng < ((previousLng - currentLng) * (point.lat - currentLat))
        / (previousLat - currentLat || Number.EPSILON) + currentLng);
    if (crosses) inside = !inside;
  }
  return inside;
}

function localXY(point, origin) {
  const scale = 60;
  const longitudeScale = Math.cos(origin.lat * Math.PI / 180);
  return {
    x: (point.lng - origin.lng) * scale * longitudeScale,
    y: (point.lat - origin.lat) * scale,
  };
}

function distanceToSegmentNm(point, left, right) {
  const start = localXY(left, point);
  const end = localXY(right, point);
  const dx = end.x - start.x;
  const dy = end.y - start.y;
  if (dx === 0 && dy === 0) return Math.hypot(start.x, start.y);
  const projection = Math.max(0, Math.min(1, -(start.x * dx + start.y * dy) / (dx * dx + dy * dy)));
  return Math.hypot(start.x + projection * dx, start.y + projection * dy);
}

export function distanceToPolygonBoundaryNm(point, polygon) {
  let minimum = Number.POSITIVE_INFINITY;
  for (let index = 0; index < polygon.length; index += 1) {
    const [leftLng, leftLat] = polygon[index];
    const [rightLng, rightLat] = polygon[(index + 1) % polygon.length];
    minimum = Math.min(
      minimum,
      distanceToSegmentNm(point, { lat: leftLat, lng: leftLng }, { lat: rightLat, lng: rightLng }),
    );
  }
  return minimum;
}

export function sampleSegment(left, right, intervalNm = 0.5) {
  const distance = haversineNm(left, right);
  const steps = Math.max(1, Math.ceil(distance / intervalNm));
  return Array.from({ length: steps + 1 }, (_value, index) => {
    const ratio = index / steps;
    return {
      lat: left.lat + (right.lat - left.lat) * ratio,
      lng: left.lng + (right.lng - left.lng) * ratio,
    };
  });
}

export function isInsideSafeWater(point, theater) {
  if (!theater?.safe_water_polygons?.length) return true;
  return theater.safe_water_polygons.some((polygon) => pointInPolygon(point, polygon.points));
}

function ringBounds(ring) {
  return ring.reduce((bounds, [lng, lat]) => ({
    west: Math.min(bounds.west, lng),
    south: Math.min(bounds.south, lat),
    east: Math.max(bounds.east, lng),
    north: Math.max(bounds.north, lat),
  }), { west: Infinity, south: Infinity, east: -Infinity, north: -Infinity });
}

function boundsContain(bounds, point, padding = 0) {
  return point.lng >= bounds.west - padding && point.lng <= bounds.east + padding
    && point.lat >= bounds.south - padding && point.lat <= bounds.north + padding;
}

const LAND_GRID_DEGREES = 2;

function gridCell(value, offset) {
  return Math.floor((value + offset) / LAND_GRID_DEGREES);
}

function gridKeysForBounds(bounds, padding = 0) {
  const west = Math.max(-180, bounds.west - padding);
  const east = Math.min(180, bounds.east + padding);
  const south = Math.max(-90, bounds.south - padding);
  const north = Math.min(90, bounds.north + padding);
  const keys = [];
  for (let x = gridCell(west, 180); x <= gridCell(east, 180); x += 1) {
    for (let y = gridCell(south, 90); y <= gridCell(north, 90); y += 1) keys.push(`${x}:${y}`);
  }
  return keys;
}

function indexedPolygons(landIndex, bounds, padding = 0) {
  if (!landIndex.grid) return landIndex.polygons;
  const candidates = new Set();
  for (const key of gridKeysForBounds(bounds, padding)) {
    for (const polygon of landIndex.grid.get(key) || []) candidates.add(polygon);
  }
  return candidates;
}

function indexedSegments(landIndex, bounds, padding = 0) {
  if (!landIndex.segmentGrid) return [];
  const candidates = new Set();
  for (const key of gridKeysForBounds(bounds, padding)) {
    for (const segment of landIndex.segmentGrid.get(key) || []) candidates.add(segment);
  }
  return candidates;
}

function pointInIndexedRing(point, latitudeBands) {
  let inside = false;
  const band = latitudeBands.get(gridCell(point.lat, 90)) || [];
  for (const { left, right } of band) {
    const crosses = ((left.lat > point.lat) !== (right.lat > point.lat))
      && (point.lng < ((right.lng - left.lng) * (point.lat - left.lat))
        / (right.lat - left.lat || Number.EPSILON) + left.lng);
    if (crosses) inside = !inside;
  }
  return inside;
}

export function buildLandIndex(geoJson) {
  const polygons = [];
  const grid = new Map();
  const segmentGrid = new Map();
  for (const feature of geoJson.features || []) {
    const geometry = feature.geometry;
    if (!geometry) continue;
    const coordinateSets = geometry.type === 'Polygon' ? [geometry.coordinates] : geometry.coordinates;
    for (const rings of coordinateSets) {
      if (!rings?.[0]?.length) continue;
      const ringLatitudeBands = rings.map((ring) => {
        const bands = new Map();
        for (let index = 0; index < ring.length - 1; index += 1) {
          const left = { lng: ring[index][0], lat: ring[index][1] };
          const right = { lng: ring[index + 1][0], lat: ring[index + 1][1] };
          const segment = { left, right };
          const bounds = segmentBounds(left, right);
          const southBand = gridCell(bounds.south, 90);
          const northBand = gridCell(bounds.north, 90);
          for (let band = southBand; band <= northBand; band += 1) {
            if (!bands.has(band)) bands.set(band, []);
            bands.get(band).push(segment);
          }
          for (const key of gridKeysForBounds(bounds)) {
            if (!segmentGrid.has(key)) segmentGrid.set(key, []);
            segmentGrid.get(key).push(segment);
          }
        }
        return bands;
      });
      const polygon = { rings, bounds: ringBounds(rings[0]), ringLatitudeBands };
      polygons.push(polygon);
      for (const key of gridKeysForBounds(polygon.bounds)) {
        if (!grid.has(key)) grid.set(key, []);
        grid.get(key).push(polygon);
      }
    }
  }
  return { metadata: geoJson.metadata || {}, polygons, grid, segmentGrid };
}

export function pointInLand(point, landIndex) {
  const pointBounds = { west: point.lng, south: point.lat, east: point.lng, north: point.lat };
  return [...indexedPolygons(landIndex, pointBounds)].some((polygon) => {
    if (!boundsContain(polygon.bounds, point)) return false;
    if (!pointInIndexedRing(point, polygon.ringLatitudeBands[0])) return false;
    return !polygon.ringLatitudeBands.slice(1).some((hole) => pointInIndexedRing(point, hole));
  });
}

export function distanceToLandNm(point, landIndex) {
  const onLand = pointInLand(point, landIndex);
  let minimum = Number.POSITIVE_INFINITY;
  const pointBounds = { west: point.lng, south: point.lat, east: point.lng, north: point.lat };
  for (const padding of [1, 4, 16, 90, 180]) {
    for (const segment of indexedSegments(landIndex, pointBounds, padding)) {
      minimum = Math.min(minimum, distanceToSegmentNm(point, segment.left, segment.right));
    }
    if (minimum <= padding * 30) break;
  }
  return onLand ? -minimum : minimum;
}

function segmentIntersection(leftA, rightA, leftB, rightB) {
  const r = { lng: rightA.lng - leftA.lng, lat: rightA.lat - leftA.lat };
  const s = { lng: rightB.lng - leftB.lng, lat: rightB.lat - leftB.lat };
  const denominator = r.lng * s.lat - r.lat * s.lng;
  if (Math.abs(denominator) < 1e-12) return null;
  const offset = { lng: leftB.lng - leftA.lng, lat: leftB.lat - leftA.lat };
  const t = (offset.lng * s.lat - offset.lat * s.lng) / denominator;
  const u = (offset.lng * r.lat - offset.lat * r.lng) / denominator;
  if (t < 0 || t > 1 || u < 0 || u > 1) return null;
  return { lat: leftA.lat + r.lat * t, lng: leftA.lng + r.lng * t, t };
}

function segmentBounds(left, right) {
  return {
    west: Math.min(left.lng, right.lng), south: Math.min(left.lat, right.lat),
    east: Math.max(left.lng, right.lng), north: Math.max(left.lat, right.lat),
  };
}

function boundsOverlap(left, right) {
  return left.west <= right.east && left.east >= right.west
    && left.south <= right.north && left.north >= right.south;
}

export function firstLandIntersection(left, right, landIndex) {
  if (pointInLand(left, landIndex)) return { ...left, t: 0 };
  const routeBounds = segmentBounds(left, right);
  let first = null;
  for (const segment of indexedSegments(landIndex, routeBounds)) {
    const intersection = segmentIntersection(left, right, segment.left, segment.right);
    if (intersection && (!first || intersection.t < first.t)) first = intersection;
  }
  if (!first && pointInLand(right, landIndex)) return { ...right, t: 1 };
  return first;
}

function offsetPointNm(origin, distanceNm, bearingRadians) {
  const latOffset = Math.cos(bearingRadians) * distanceNm / 60;
  const longitudeScale = Math.max(0.1, Math.cos(origin.lat * Math.PI / 180));
  const lngOffset = Math.sin(bearingRadians) * distanceNm / (60 * longitudeScale);
  return { lat: origin.lat + latOffset, lng: origin.lng + lngOffset };
}

export function findNearestSafeWater(origin, landIndex, theater, clearanceNm = 1, maxRadiusNm = 30) {
  const radialStep = Math.max(0.5, clearanceNm / 2);
  for (let radius = radialStep; radius <= maxRadiusNm; radius += radialStep) {
    const angularSteps = Math.max(16, Math.ceil(radius * 2));
    for (let index = 0; index < angularSteps; index += 1) {
      const candidate = offsetPointNm(origin, radius, index * Math.PI * 2 / angularSteps);
      if (!isInsideSafeWater(candidate, theater)) continue;
      if (distanceToLandNm(candidate, landIndex) >= clearanceNm) return candidate;
    }
  }
  return null;
}

export function findNearestLand(origin, landIndex, maxRadiusNm = 30, minimumInlandNm = 0.25) {
  const radialStep = 0.25;
  for (let radius = radialStep; radius <= maxRadiusNm; radius += radialStep) {
    const angularSteps = Math.max(24, Math.ceil(radius * 3));
    for (let index = 0; index < angularSteps; index += 1) {
      const candidate = offsetPointNm(origin, radius, index * Math.PI * 2 / angularSteps);
      if (distanceToLandNm(candidate, landIndex) <= -minimumInlandNm) return candidate;
    }
  }
  return null;
}

export function findSafeDetour(left, right, crossing, landIndex, theater, clearanceNm = 1, maxRadiusNm = 40) {
  const radialStep = Math.max(1, clearanceNm);
  for (let radius = radialStep; radius <= maxRadiusNm; radius += radialStep) {
    const angularSteps = Math.max(24, Math.ceil(radius * 2));
    for (let index = 0; index < angularSteps; index += 1) {
      const candidate = offsetPointNm(crossing, radius, index * Math.PI * 2 / angularSteps);
      if (!isInsideSafeWater(candidate, theater)) continue;
      if (distanceToLandNm(candidate, landIndex) < clearanceNm) continue;
      if (firstLandIntersection(left, candidate, landIndex)) continue;
      if (firstLandIntersection(candidate, right, landIndex)) continue;
      return candidate;
    }
  }
  return null;
}

export function validateRealWorld(scenario, theater, landIndex, clearanceNm = 1) {
  const surfaceClasses = new Set(theater?.surface_classes || []);
  const findings = [];
  for (const unit of scenario.units) {
    const isSurface = unit.domain === 'surface' || surfaceClasses.has(unit.className);
    if (unit.domain === 'ground') {
      const distance = distanceToLandNm(unit.position, landIndex);
      if (distance > clearanceNm) {
        const suggestion = findNearestLand(unit.position, landIndex);
        findings.push({
          source: 'Real coastline', severity: 'error', unit: unit.name,
          message: `Ground unit is ${distance.toFixed(2)} nm offshore.`, point: unit.position, suggestion,
          edit: suggestion ? {
            kind: 'position', sourceLine: unit.position.sourceLine, unitName: unit.name,
          } : null,
        });
      } else if (distance >= 0) {
        findings.push({
          source: 'Real coastline', severity: 'warning', unit: unit.name,
          message: `Ground unit plots just offshore (${distance.toFixed(2)} nm); verify coastal resolution.`, point: unit.position,
        });
      }
      continue;
    }
    if (!isSurface) continue;
    const startDistance = distanceToLandNm(unit.position, landIndex);
    if (startDistance <= 0) {
      const suggestion = findNearestSafeWater(unit.position, landIndex, theater, clearanceNm);
      findings.push({
        source: 'Real coastline', severity: 'error', unit: unit.name,
        message: 'Ship start is on real-world land.', point: unit.position, suggestion,
        edit: suggestion ? {
          kind: 'position', sourceLine: unit.position.sourceLine, unitName: unit.name,
        } : null,
      });
      if (theater && isInsideSafeWater(unit.position, theater)) {
        findings.push({
          source: 'Mask disagreement', severity: 'error', unit: unit.name,
          message: 'The GCBH safe-water mask marks this real-world land position as safe.', point: unit.position,
        });
      }
    } else if (startDistance < clearanceNm) {
      findings.push({
        source: 'Real coastline', severity: 'warning', unit: unit.name,
        message: `Ship start is only ${startDistance.toFixed(2)} nm from real-world land.`, point: unit.position,
      });
    }

    const route = [unit.position, ...unit.waypoints];
    route.slice(0, -1).forEach((left, index) => {
      const right = route[index + 1];
      const intersection = firstLandIntersection(left, right, landIndex);
      if (intersection) {
        const suggestion = pointInLand(right, landIndex)
          ? findNearestSafeWater(right, landIndex, theater, clearanceNm)
          : findSafeDetour(left, right, intersection, landIndex, theater, clearanceNm);
        findings.push({
          source: 'Real coastline', severity: 'error', unit: unit.name,
          message: `Route leg ${index + 1} crosses real-world land.`, point: intersection, suggestion,
          edit: suggestion ? {
            kind: pointInLand(right, landIndex) ? 'waypoint' : 'insert-waypoint',
            sourceLine: right.sourceLine,
            unitName: unit.name,
            waypointIndex: index,
            altitude: right.altitude,
            speed: right.speed,
          } : null,
        });
        if (theater && isInsideSafeWater(intersection, theater)) {
          findings.push({
            source: 'Mask disagreement', severity: 'error', unit: unit.name,
            message: `GCBH mask incorrectly permits the land crossing on route leg ${index + 1}.`, point: intersection,
          });
        }
        return;
      }
      let nearest = { distance: Number.POSITIVE_INFINITY, point: left };
      for (const point of sampleSegment(left, right, 0.25)) {
        const distance = distanceToLandNm(point, landIndex);
        if (distance < nearest.distance) nearest = { distance, point };
      }
      if (nearest.distance < clearanceNm) {
        findings.push({
          source: 'Real coastline', severity: 'warning', unit: unit.name,
          message: `Route leg ${index + 1} closes to ${Math.max(0, nearest.distance).toFixed(2)} nm from real-world land.`,
          point: nearest.point,
        });
      }
    });
  }
  return findings;
}

export function safeWaterClearanceNm(point, theater) {
  const containing = theater.safe_water_polygons.filter((polygon) => pointInPolygon(point, polygon.points));
  if (containing.length === 0) return -Math.min(
    ...theater.safe_water_polygons.map((polygon) => distanceToPolygonBoundaryNm(point, polygon.points)),
  );
  return Math.max(...containing.map((polygon) => distanceToPolygonBoundaryNm(point, polygon.points)));
}

export function validateAircraftLoadouts(scenario) {
  return scenario.units
    .filter((unit) => unit.domain === 'air' && unit.tasks?.includes('AutoAttack'))
    .filter((unit) => !unit.launcherItems?.some((item) => item.quantity > 0))
    .map((unit) => ({
      source: 'Scenario loadout',
      severity: 'error',
      unit: unit.name,
      message: 'Combat aircraft has AutoAttack tasking but no launcher loadout.',
      point: unit.position,
    }));
}

export function validateMission(scenario, theater, clearanceNm = 1) {
  if (!theater?.safe_water_polygons?.length) return [];
  const surfaceClasses = new Set(theater.surface_classes);
  const findings = [];
  for (const unit of scenario.units) {
    const isSurface = unit.domain === 'surface' || surfaceClasses.has(unit.className);
    if (!isSurface) continue;

    const startClearance = safeWaterClearanceNm(unit.position, theater);
    if (startClearance < 0) {
      findings.push({ severity: 'error', unit: unit.name, message: 'Start is outside the GCBH safe-water mask.', point: unit.position });
    } else if (startClearance < clearanceNm) {
      findings.push({ severity: 'warning', unit: unit.name, message: `Start has only ${startClearance.toFixed(2)} nm mask clearance.`, point: unit.position });
    }

    const route = [unit.position, ...unit.waypoints];
    route.slice(0, -1).forEach((left, index) => {
      const right = route[index + 1];
      const samples = sampleSegment(left, right, 0.5);
      const outside = samples.find((point) => !isInsideSafeWater(point, theater));
      if (outside) {
        findings.push({
          severity: 'error',
          unit: unit.name,
          message: `Route leg ${index + 1} exits the GCBH safe-water mask.`,
          point: outside,
        });
      }
    });
  }
  return findings;
}

export function googleElevationSamples(scenario, theater, spacingNm = 1) {
  const surfaceClasses = new Set(theater?.surface_classes || []);
  const points = [];
  for (const unit of scenario.units.filter((candidate) => candidate.domain === 'surface' || surfaceClasses.has(candidate.className))) {
    const route = [unit.position, ...unit.waypoints];
    if (route.length === 1) points.push({ ...unit.position, unit: unit.name, leg: 0, domain: 'surface' });
    route.slice(0, -1).forEach((left, index) => {
      sampleSegment(left, route[index + 1], spacingNm).forEach((point) => {
        points.push({ ...point, unit: unit.name, leg: index + 1, domain: 'surface' });
      });
    });
  }
  for (const unit of scenario.units.filter((candidate) => candidate.domain === 'ground')) {
    points.push({ ...unit.position, unit: unit.name, leg: 0, domain: 'ground' });
  }
  if (points.length <= 512) return points;
  const stride = Math.ceil(points.length / 512);
  return points.filter((_point, index) => index % stride === 0).slice(0, 512);
}
