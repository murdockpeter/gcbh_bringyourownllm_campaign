export const ACTIVE_UNIT_COLOR = '#f4a24c';

export function routeVisualStyle(allianceColor, selected = false) {
  return {
    strokeColor: selected ? ACTIVE_UNIT_COLOR : allianceColor,
    strokeOpacity: selected ? 1 : 0.85,
    strokeWeight: selected ? 4 : 2,
    zIndex: selected ? 220 : 20,
  };
}

export function waypointVisualStyle(allianceColor, selected = false) {
  const color = selected ? ACTIVE_UNIT_COLOR : allianceColor;
  return {
    color,
    fillColor: selected ? '#2a1806' : '#071019',
    fillOpacity: selected ? 1 : 0.85,
    strokeWeight: selected ? 2.5 : 1.5,
    scale: selected ? 7.5 : 6,
    zIndex: selected ? 230 : undefined,
  };
}
