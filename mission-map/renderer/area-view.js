export function scenariosForArea(scenarios, theaterId = '') {
  return theaterId ? scenarios.filter((scenario) => scenario.theaterId === theaterId) : scenarios;
}

export function preferredAreaScenario(scenarios, currentPath = '') {
  return scenarios.find((scenario) => scenario.path === currentPath)
    || scenarios.find((scenario) => scenario.name.startsWith('operation_'))
    || scenarios[0] || null;
}

export function operationalBounds(theater) {
  const bounds = theater?.coverage_bounds;
  return bounds && ['west', 'south', 'east', 'north'].every((key) => Number.isFinite(bounds[key]))
    ? { west: bounds.west, south: bounds.south, east: bounds.east, north: bounds.north } : null;
}
