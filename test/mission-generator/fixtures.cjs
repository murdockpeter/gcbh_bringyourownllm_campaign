'use strict';

function baseUnit(overrides = {}) {
  return {
    unit_name: 'Test Unit', platform_class: 'Test Ship', status: 'operational', mission_capable: true,
    structural_integrity_pct: 90, speed_limit_kts: 0, readiness_pct: 80, crew_fatigue_pct: 20,
    fuel_pct: 75, ammo_pct: 50, current_location: 'Test area', damage: [],
    repair: { emergency_hours_remaining: 0, pier_side_hours_required: 0, full_reconstitution_days: 0, port_required: false },
    logistics: { daily_upkeep_points: 1 },
    ...overrides,
  };
}

function baseState() {
  return {
    campaign_id: 'test', campaign_name: 'Test Campaign', version: 1, current_time_local: '2026-05-22T12:00:00+04:00', turn: 2,
    sides: {
      blue: { units: [baseUnit({ unit_name: 'Blue Escort' })] },
      red: { units: [baseUnit({ unit_name: 'Red Raider' })] },
    },
  };
}

function baseSeed(overrides = {}) {
  return {
    schema_version: 1, scenario_id: 'test_001', scenario_name: 'Test Mission', theater_id: 'hormuz_mvp',
    date_time: '2026-05-22T14:00:00+04:00', playable_side: 'blue', archetype: 'convoy_escort',
    premise: 'A test force must cross the operating area.',
    placement: {
      surface_starts: { blue: [{ lat: 25.5, lon: 57.8 }], red: [{ lat: 26.4, lon: 56.4 }] },
      surface_routes: { blue: [{ lat: 25.8, lon: 57.1 }], red: [{ lat: 25.8, lon: 57.1 }] },
      air_boxes: {
        blue: { south: 25, north: 26, west: 57, east: 58, altitude: 8000 },
        red: { south: 26, north: 27, west: 56, east: 57, altitude: 8000 },
      },
      ground_positions: {},
    },
    ...overrides,
  };
}

function plannedUnit(overrides = {}) {
  return {
    ...baseUnit(), side: 'blue', domain: 'ship', role: 'surface_combatant',
    platform: { domain: 'ship', maxSpeedKts: 30 }, speed: 20, fuelFraction: 0.75,
    launchers: [{ launcherId: 0, item: 'Test Missile', quantity: 2 }], magazines: [],
    loadoutSetup: 'Test Setup', tasks: ['Ship1', 'AutoAttack', 'Nav'], sorties: 0,
    persistence: {}, position: { lat: 25.5, lon: 57.8, altitude: 0 }, route: [], heading: 285, navLoop: false,
    ...overrides,
  };
}

module.exports = { baseUnit, baseState, baseSeed, plannedUnit };
