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

export function unitMarkerVisualStyle(allianceColor, selected = false) {
  return {
    fillColor: selected ? ACTIVE_UNIT_COLOR : allianceColor,
    fillOpacity: 0.95,
    strokeColor: selected ? '#fff0dc' : '#eaf7fb',
    strokeWeight: selected ? 2.5 : 1,
    scale: selected ? 11 : 9,
    zIndex: selected ? 240 : undefined,
  };
}
