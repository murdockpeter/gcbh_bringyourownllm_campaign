import {
  buildLandIndex,
  googleElevationSamples,
  validateAircraftLoadouts,
  validateMission,
  validateRealWorld,
} from './geometry.js';
import { allianceSide, visibleFindings, visibleUnits } from './side-filter.js';

const elements = Object.fromEntries([
  'scenario-select', 'browse-button', 'reload-button', 'watch-status', 'settings-button',
  'mission-name', 'mission-meta', 'mission-description', 'unit-count', 'unit-list',
  'map', 'map-placeholder', 'placeholder-key-button', 'toggle-mask', 'toggle-land', 'toggle-routes',
  'toggle-satellite', 'side-filter', 'coordinate-order', 'coordinate-reason', 'clearance-select',
  'validate-button', 'elevation-button', 'fix-button', 'edit-mode-button',
  'manual-actions', 'save-manual-button', 'discard-edits-button', 'edit-status',
  'finding-count', 'finding-list',
  'land-data-status', 'mask-data-status',
  'settings-dialog', 'settings-form', 'api-key', 'settings-message', 'save-key-button',
].map((id) => [id.replaceAll('-', '_'), document.getElementById(id)]));

const state = {
  scenario: null,
  theater: null,
  landGeoJson: null,
  landIndex: null,
  selectedPath: '',
  map: null,
  mapsReady: false,
  overlays: [],
  maskOverlays: [],
  landOverlays: [],
  routeOverlays: [],
  findingOverlays: [],
  markersByUnit: new Map(),
  findings: [],
  localFindings: [],
  autoFixEdits: [],
  editMode: false,
  pendingEdits: new Map(),
  saving: false,
};

function escapeHtml(value) {
  const node = document.createElement('div');
  node.textContent = String(value ?? '');
  return node.innerHTML;
}

function allianceColor(unit) {
  if (allianceSide(unit.allianceName, unit.allianceId) === 'blue') return '#4aa9ff';
  if (allianceSide(unit.allianceName, unit.allianceId) === 'red') return '#ef5a61';
  return '#f4a24c';
}

function selectedSide() {
  return elements.side_filter.value || 'all';
}

function displayedFindings() {
  return visibleFindings(state.findings, state.scenario?.units, selectedSide());
}

function showSettings() {
  elements.settings_message.textContent = '';
  elements.api_key.value = '';
  elements.settings_dialog.showModal();
}

function collectFixEdits(findings) {
  const edits = new Map();
  for (const finding of findings) {
    if (finding.source !== 'Real coastline' || !finding.edit || !finding.suggestion) continue;
    if (!Number.isInteger(finding.edit.sourceLine)) continue;
    const key = String(finding.edit.sourceLine);
    if (!edits.has(key)) {
      edits.set(key, {
        ...finding.edit,
        lat: finding.suggestion.lat,
        lng: finding.suggestion.lng,
      });
    }
  }
  return [...edits.values()];
}

function setEditStatus(message = '', tone = '') {
  elements.edit_status.textContent = message;
  elements.edit_status.className = `edit-status${tone ? ` ${tone}` : ''}`;
}

function updateEditControls() {
  const pendingCount = state.pendingEdits.size;
  const fixCount = state.autoFixEdits.length;
  elements.fix_button.textContent = `Fix scenario (${fixCount})`;
  elements.fix_button.disabled = state.saving || fixCount === 0 || pendingCount > 0;
  elements.edit_mode_button.textContent = state.editMode ? 'Stop dragging coordinates' : 'Edit coordinates manually';
  elements.edit_mode_button.disabled = state.saving || !state.mapsReady;
  elements.manual_actions.hidden = !state.editMode && pendingCount === 0;
  elements.save_manual_button.textContent = `Save manual edits (${pendingCount})`;
  elements.save_manual_button.disabled = state.saving || pendingCount === 0;
  elements.discard_edits_button.disabled = state.saving || pendingCount === 0;
}

function setFindings(findings) {
  state.findings = findings;
  state.autoFixEdits = collectFixEdits(findings);
  updateEditControls();
  renderFindings();
}

function renderFindings({ refreshMapMarkers = true } = {}) {
  const findings = displayedFindings();
  elements.finding_count.textContent = state.findings.length === findings.length
    ? findings.length
    : `${findings.length}/${state.findings.length}`;
  if (state.map && refreshMapMarkers) renderFindingMarkers();
  if (findings.length === 0) {
    elements.finding_list.innerHTML = '<div class="empty-state">No findings for the selected comparison.</div>';
    return;
  }
  elements.finding_list.innerHTML = findings.map((finding) => {
    const severityColor = finding.severity === 'error' ? '#ef5a61'
      : finding.severity === 'warning' ? '#f4a24c' : '#25c7d9';
    const focusPoint = finding.suggestion || finding.point;
    const suggestion = finding.suggestion
      ? `<small>Candidate safe coordinate: ${finding.suggestion.lat.toFixed(6)}, ${finding.suggestion.lng.toFixed(6)}${finding.edit ? ' Â· automatic fix available' : ''}</small>`
      : '';
    return `<button class="finding" data-lat="${focusPoint?.lat ?? ''}" data-lng="${focusPoint?.lng ?? ''}" style="--severity:${severityColor}">
      <strong>${escapeHtml(finding.severity)} · ${escapeHtml(finding.source || 'Audit')} · ${escapeHtml(finding.unit || 'Mission')}</strong>
      <span>${escapeHtml(finding.message)}</span>
      ${suggestion}
    </button>`;
  }).join('');
  elements.finding_list.querySelectorAll('.finding').forEach((findingElement) => {
    findingElement.addEventListener('click', () => {
      if (!state.map || !findingElement.dataset.lat) return;
      state.map.panTo({ lat: Number(findingElement.dataset.lat), lng: Number(findingElement.dataset.lng) });
      state.map.setZoom(Math.max(state.map.getZoom() || 8, 11));
    });
  });
}

function renderMissionDetails() {
  const { scenario } = state;
  const units = visibleUnits(scenario.units, selectedSide());
  elements.mission_name.textContent = scenario.info.name;
  const date = scenario.info.dateLabel || scenario.dateTime.slice(0, 3).join('-');
  elements.mission_meta.textContent = [date, scenario.info.playableSides.join(' / '), scenario.fileName].filter(Boolean).join(' · ');
  elements.mission_description.textContent = scenario.info.description || 'No scenario description.';
  elements.unit_count.textContent = units.length === scenario.units.length
    ? units.length
    : `${units.length}/${scenario.units.length}`;
  elements.coordinate_order.textContent = scenario.coordinateConvention.order === 'lng-lat'
    ? 'LONGITUDE → LATITUDE'
    : 'LATITUDE → LONGITUDE';
  elements.coordinate_reason.textContent = scenario.coordinateConvention.reason;

  elements.unit_list.innerHTML = units.map((unit, index) => `
    <button class="unit-card" data-unit-index="${index}" style="--alliance-color:${allianceColor(unit)}">
      <strong>${escapeHtml(unit.name)}</strong>
      <span>${escapeHtml(unit.className)}</span>
      <span>${escapeHtml(unit.allianceName)} · ${unit.position.lat.toFixed(4)}, ${unit.position.lng.toFixed(4)} · ${unit.waypoints.length} WP</span>
    </button>
  `).join('');
  elements.unit_list.querySelectorAll('.unit-card').forEach((card) => {
    card.addEventListener('click', () => focusUnit(units[Number(card.dataset.unitIndex)]));
  });
}

function clearMap() {
  state.overlays.forEach((overlay) => overlay.setMap?.(null));
  state.overlays = [];
  state.maskOverlays = [];
  state.landOverlays = [];
  state.routeOverlays = [];
  state.findingOverlays = [];
  state.markersByUnit.clear();
}

function stageManualEdit(kind, target, coordinate) {
  target.lat = coordinate.lat;
  target.lng = coordinate.lng;
  const edit = {
    kind,
    sourceLine: target.sourceLine,
    lat: coordinate.lat,
    lng: coordinate.lng,
  };
  state.pendingEdits.set(`${kind}:${target.sourceLine}`, edit);
  setEditStatus(`${state.pendingEdits.size} unsaved coordinate edit${state.pendingEdits.size === 1 ? '' : 's'}.`, 'active');
  renderMissionDetails();
  runLocalValidation();
  renderMap();
  updateEditControls();
}

function renderFindingMarkers() {
  state.findingOverlays.forEach((overlay) => overlay.setMap(null));
  state.findingOverlays = [];
  if (!state.map || !globalThis.google?.maps?.Marker) return;
  for (const finding of displayedFindings()) {
    if (finding.point) {
      const color = finding.severity === 'error' ? '#ff3f4c'
        : finding.severity === 'warning' ? '#ffad42' : '#25c7d9';
      const marker = new google.maps.Marker({
        position: finding.point,
        map: state.map,
        title: `${finding.source || 'Audit'}: ${finding.message}`,
        label: { text: '!', color: '#ffffff', fontSize: '10px', fontWeight: '900' },
        icon: {
          path: google.maps.SymbolPath.CIRCLE,
          fillColor: color,
          fillOpacity: 1,
          strokeColor: '#ffffff',
          strokeWeight: 1,
          scale: 7,
        },
        zIndex: 500,
      });
      state.overlays.push(marker);
      state.findingOverlays.push(marker);
    }
    if (finding.suggestion) {
      const marker = new google.maps.Marker({
        position: finding.suggestion,
        map: state.map,
        title: `Candidate safe coordinate for ${finding.unit}`,
        label: { text: '✓', color: '#04130b', fontSize: '10px', fontWeight: '900' },
        icon: {
          path: google.maps.SymbolPath.CIRCLE,
          fillColor: '#65e59b',
          fillOpacity: 1,
          strokeColor: '#ffffff',
          strokeWeight: 1,
          scale: 7,
        },
        zIndex: 510,
      });
      state.overlays.push(marker);
      state.findingOverlays.push(marker);
    }
  }
}

function focusUnit(unit) {
  if (!state.map) return;
  state.map.panTo(unit.position);
  state.map.setZoom(Math.max(state.map.getZoom() || 8, 10));
  const marker = state.markersByUnit.get(unit.name);
  if (marker) google.maps.event.trigger(marker, 'click');
}

function renderMap() {
  if (!state.mapsReady || !state.scenario) return;
  const priorCenter = state.map.getCenter()?.toJSON();
  const priorZoom = state.map.getZoom();
  clearMap();
  const bounds = new google.maps.LatLngBounds();
  const infoWindow = new google.maps.InfoWindow();

  const scenarioPoints = state.scenario.units.flatMap((unit) => [unit.position, ...unit.waypoints]);
  const areaBounds = scenarioPoints.reduce((value, point) => ({
    west: Math.min(value.west, point.lng), south: Math.min(value.south, point.lat),
    east: Math.max(value.east, point.lng), north: Math.max(value.north, point.lat),
  }), { west: Infinity, south: Infinity, east: -Infinity, north: -Infinity });
  for (const { rings, bounds: landBounds } of state.landIndex?.polygons || []) {
    const visible = landBounds.west <= areaBounds.east + 1 && landBounds.east >= areaBounds.west - 1
      && landBounds.south <= areaBounds.north + 1 && landBounds.north >= areaBounds.south - 1;
    if (visible) {
      const polygon = new google.maps.Polygon({
        paths: rings.map((ring) => ring.map(([lng, lat]) => ({ lat, lng }))),
        strokeColor: '#ff7657',
        strokeOpacity: 0.8,
        strokeWeight: 1.1,
        fillColor: '#ff7657',
        fillOpacity: 0.025,
        clickable: false,
        map: elements.toggle_land.checked ? state.map : null,
      });
      state.overlays.push(polygon);
      state.landOverlays.push(polygon);
    }
  }

  (state.theater?.safe_water_polygons || []).forEach((area) => {
    const polygon = new google.maps.Polygon({
      paths: area.points.map(([lng, lat]) => ({ lat, lng })),
      strokeColor: '#25c7d9',
      strokeOpacity: 0.65,
      strokeWeight: 1.5,
      fillColor: '#25c7d9',
      fillOpacity: 0.10,
      clickable: false,
      map: elements.toggle_mask.checked ? state.map : null,
    });
    state.overlays.push(polygon);
    state.maskOverlays.push(polygon);
  });

  visibleUnits(state.scenario.units, selectedSide()).forEach((unit) => {
    bounds.extend(unit.position);
    const color = allianceColor(unit);
    const marker = new google.maps.Marker({
      position: unit.position,
      map: state.map,
      title: unit.name,
      label: { text: unit.name.slice(0, 2).toUpperCase(), color: '#ffffff', fontSize: '9px', fontWeight: '700' },
      icon: {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: color,
        fillOpacity: 0.95,
        strokeColor: '#eaf7fb',
        strokeWeight: 1,
        scale: 9,
      },
      draggable: state.editMode,
      zIndex: state.editMode ? 300 : undefined,
    });
    marker.addListener('click', () => {
      infoWindow.setContent(`<div style="color:#10202a;min-width:190px"><strong>${escapeHtml(unit.name)}</strong><br>${escapeHtml(unit.className)}<br><small>${unit.position.lat.toFixed(5)}, ${unit.position.lng.toFixed(5)} · ${unit.speed ?? 0} kt</small></div>`);
      infoWindow.open({ map: state.map, anchor: marker });
    });
    marker.addListener('dragend', (event) => {
      if (!state.editMode || !event.latLng) return;
      stageManualEdit('position', unit.position, event.latLng.toJSON());
    });
    state.overlays.push(marker);
    state.markersByUnit.set(unit.name, marker);

    if (unit.waypoints.length) {
      const route = [unit.position, ...unit.waypoints];
      route.forEach((point) => bounds.extend(point));
      const polyline = new google.maps.Polyline({
        path: route,
        geodesic: true,
        strokeColor: color,
        strokeOpacity: 0.85,
        strokeWeight: 2,
        map: elements.toggle_routes.checked ? state.map : null,
      });
      state.overlays.push(polyline);
      state.routeOverlays.push(polyline);
      unit.waypoints.forEach((waypoint, index) => {
        const waypointMarker = new google.maps.Marker({
          position: waypoint,
          map: elements.toggle_routes.checked ? state.map : null,
          title: `${unit.name} waypoint ${index + 1}`,
          label: { text: String(index + 1), color: color, fontSize: '9px', fontWeight: '800' },
          icon: {
            path: google.maps.SymbolPath.CIRCLE,
            fillColor: '#071019',
            fillOpacity: 0.85,
            strokeColor: color,
            strokeWeight: 1.5,
            scale: 6,
          },
          draggable: state.editMode,
          zIndex: state.editMode ? 310 : undefined,
        });
        waypointMarker.addListener('dragend', (event) => {
          if (!state.editMode || !event.latLng) return;
          stageManualEdit('waypoint', waypoint, event.latLng.toJSON());
        });
        state.overlays.push(waypointMarker);
        state.routeOverlays.push(waypointMarker);
      });
    }
  });

  if (state.editMode && priorCenter && Number.isFinite(priorZoom)) {
    state.map.setCenter(priorCenter);
    state.map.setZoom(priorZoom);
  } else if (!bounds.isEmpty()) {
    state.map.fitBounds(bounds, 48);
  }
  renderFindingMarkers();
}

async function loadGoogleMaps(key) {
  if (!key || state.mapsReady) return;
  await new Promise((resolve, reject) => {
    let settled = false;
    const finish = (callback, value) => {
      if (settled) return;
      settled = true;
      clearTimeout(timeout);
      callback(value);
    };
    globalThis.__missionMapGoogleReady = () => finish(resolve);
    globalThis.gm_authFailure = () => finish(
      reject,
      new Error('Google rejected the API key. Verify billing, Maps JavaScript API, referrer restrictions, and key rotation.'),
    );
    const script = document.createElement('script');
    script.src = `https://maps.googleapis.com/maps/api/js?key=${encodeURIComponent(key)}&loading=async&v=weekly&libraries=marker&callback=__missionMapGoogleReady`;
    script.async = true;
    script.onerror = () => finish(reject, new Error('Google Maps could not be downloaded. Check the network connection and content restrictions.'));
    const timeout = setTimeout(
      () => finish(reject, new Error('Google Maps did not initialize within 15 seconds. Verify the API key configuration.')),
      15_000,
    );
    document.head.appendChild(script);
  });
  let MapClass;
  if (globalThis.google?.maps?.importLibrary) {
    const mapsLibrary = await google.maps.importLibrary('maps');
    await google.maps.importLibrary('marker');
    MapClass = mapsLibrary.Map;
  } else if (typeof globalThis.google?.maps?.Map === 'function') {
    MapClass = google.maps.Map;
  } else {
    throw new Error('Google returned an incomplete Maps API. Confirm Maps JavaScript API is enabled for this key and project.');
  }
  state.map = new MapClass(elements.map, {
    center: state.scenario?.theaterCenter || { lat: 26.2, lng: 56.8 },
    zoom: 8,
    mapTypeId: 'terrain',
    mapTypeControl: false,
    streetViewControl: false,
    fullscreenControl: false,
    clickableIcons: false,
    backgroundColor: '#071019',
  });
  state.mapsReady = true;
  elements.map_placeholder.hidden = true;
  updateEditControls();
  renderMap();
}

async function loadScenario(filePath, { quiet = false } = {}) {
  if (!filePath) return;
  try {
    const result = await window.missionMap.loadScenario(filePath);
    state.scenario = result.scenario;
    state.theater = result.theater;
    elements.toggle_mask.disabled = !state.theater;
    elements.toggle_mask.checked = Boolean(state.theater);
    elements.mask_data_status.textContent = state.theater
      ? `${state.theater.name} mask active`
      : 'No regional GCBH mask; global coastline checks remain active';
    state.selectedPath = filePath;
    state.pendingEdits.clear();
    state.editMode = false;
    renderMissionDetails();
    runLocalValidation();
    renderMap();
    if (!quiet) elements.watch_status.textContent = 'LIVE';
  } catch (error) {
    setFindings([{ severity: 'error', unit: 'Parser', message: error.message }]);
  }
}

async function saveEdits(edits, label) {
  if (!state.selectedPath || !edits.length || state.saving) return;
  state.saving = true;
  updateEditControls();
  setEditStatus(`${label}: saving ${edits.length} edit${edits.length === 1 ? '' : 's'}â€¦`, 'active');
  try {
    const result = await window.missionMap.saveScenarioEdits(state.selectedPath, edits);
    await loadScenario(state.selectedPath, { quiet: true });
    const errorCount = state.localFindings.filter((finding) => finding.severity === 'error').length;
    const backupName = result.backupPath.split(/[\\/]/).pop();
    setEditStatus(
      `Saved ${result.editCount} edit${result.editCount === 1 ? '' : 's'}; backup ${backupName}. Re-check found ${errorCount} error${errorCount === 1 ? '' : 's'} and ${state.autoFixEdits.length} additional automatic fix${state.autoFixEdits.length === 1 ? '' : 'es'}.`,
      errorCount ? 'active' : 'success',
    );
  } catch (error) {
    setEditStatus(`Save failed: ${error.message || error}`, 'error');
  } finally {
    state.saving = false;
    updateEditControls();
  }
}

function runLocalValidation() {
  if (!state.scenario) return;
  const clearance = Number(elements.clearance_select.value);
  const findings = state.theater
    ? validateMission(state.scenario, state.theater, clearance)
      .map((finding) => ({ source: 'GCBH mask', ...finding }))
    : [];
  findings.push(...validateAircraftLoadouts(state.scenario));
  if (state.landIndex) {
    findings.push(...validateRealWorld(state.scenario, state.theater, state.landIndex, clearance));
  } else {
    findings.push({ severity: 'error', source: 'Real coastline', unit: 'Dataset', message: 'Real-world land data failed to load.' });
  }
  if (state.scenario.coordinateConvention.order === 'lng-lat') {
    findings.unshift({
      severity: 'warning',
      source: 'Scenario format',
      unit: 'Scenario format',
      message: 'Legacy longitude/latitude SetPosition order detected. GCBH v0.2.1 uses latitude/longitude.',
      point: state.scenario.theaterCenter,
    });
  }
  state.localFindings = findings;
  setFindings(findings);
}

async function runElevationValidation() {
  if (!state.mapsReady) {
    setFindings([{ severity: 'warning', unit: 'Google comparison', message: 'Configure Google Maps and enable Elevation API first.' }]);
    return;
  }
  const samples = googleElevationSamples(state.scenario, state.theater, 1);
  if (!samples.length) {
    setFindings([{ severity: 'info', unit: 'Google comparison', message: 'No surface routes found to sample.' }]);
    return;
  }
  elements.elevation_button.disabled = true;
  elements.elevation_button.textContent = `Sampling ${samples.length} points…`;
  try {
    const ElevationService = google.maps.importLibrary
      ? (await google.maps.importLibrary('elevation')).ElevationService
      : google.maps.ElevationService;
    if (typeof ElevationService !== 'function') {
      throw new Error('Elevation API is unavailable for this key/project.');
    }
    const service = new ElevationService();
    const response = await service.getElevationForLocations({
      locations: samples.map(({ lat, lng }) => ({ lat, lng })),
    });
    const results = Array.isArray(response) ? response : response.results;
    const conflicts = results
      .map((result, index) => ({ result, sample: samples[index] }))
      .filter(({ result, sample }) => (
        sample.domain === 'surface' ? result.elevation > 2 : result.elevation < -2
      ));
    const googleFindings = conflicts.slice(0, 30).map(({ result, sample }) => ({
      source: 'Google elevation',
      severity: 'error',
      unit: sample.unit,
      message: sample.domain === 'surface'
        ? `Elevation is ${result.elevation.toFixed(1)} m on route leg ${sample.leg}; ship route intersects land.`
        : `Elevation is ${result.elevation.toFixed(1)} m; ground unit may be offshore.`,
      point: { lat: result.location.lat(), lng: result.location.lng() },
    }));
    if (conflicts.length > 30) {
      googleFindings.push({
        source: 'Google elevation', severity: 'warning', unit: 'Comparison',
        message: `${conflicts.length - 30} additional conflicting elevation samples omitted.`,
      });
    }
    if (!googleFindings.length) {
      googleFindings.push({
        source: 'Google elevation', severity: 'info', unit: 'Comparison',
        message: `${samples.length} samples agree with their surface/ground placement.`,
      });
    }
    setFindings([...state.localFindings, ...googleFindings]);
  } catch (error) {
    setFindings([{ severity: 'error', unit: 'Google comparison', message: `Elevation request failed: ${error.message || error}` }]);
  } finally {
    elements.elevation_button.disabled = false;
    elements.elevation_button.textContent = 'Check Google elevation';
  }
}

async function initialize() {
  setFindings([]);
  const scenarios = await window.missionMap.listScenarios();
  try {
    const response = await fetch('/data/global-land.geojson');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.landGeoJson = await response.json();
    state.landIndex = buildLandIndex(state.landGeoJson);
    elements.land_data_status.textContent = `${state.landIndex.polygons.length} polygons ready`;
  } catch (error) {
    elements.land_data_status.textContent = `Unavailable: ${error.message}`;
  }
  elements.scenario_select.innerHTML = scenarios.map((scenario) => `<option value="${escapeHtml(scenario.path)}">${escapeHtml(scenario.name)}</option>`).join('');
  if (scenarios.length) {
    await loadScenario(scenarios[0].path);
    elements.scenario_select.value = scenarios[0].path;
  }
  const key = await window.missionMap.getMapsKey();
  if (key) {
    try {
      await loadGoogleMaps(key);
    } catch (error) {
      setFindings([{ severity: 'error', unit: 'Google Maps', message: error.message }]);
    }
  }
}

elements.scenario_select.addEventListener('change', () => loadScenario(elements.scenario_select.value));
elements.browse_button.addEventListener('click', async () => {
  const filePath = await window.missionMap.chooseScenario();
  if (!filePath) return;
  if (![...elements.scenario_select.options].some((option) => option.value === filePath)) {
    elements.scenario_select.add(new Option(filePath.split(/[\\/]/).pop(), filePath));
  }
  elements.scenario_select.value = filePath;
  await loadScenario(filePath);
});
elements.reload_button.addEventListener('click', () => loadScenario(state.selectedPath));
elements.settings_button.addEventListener('click', showSettings);
elements.placeholder_key_button.addEventListener('click', showSettings);
elements.validate_button.addEventListener('click', runLocalValidation);
elements.clearance_select.addEventListener('change', runLocalValidation);
elements.elevation_button.addEventListener('click', runElevationValidation);
elements.fix_button.addEventListener('click', () => saveEdits(state.autoFixEdits, 'Automatic fix'));
elements.edit_mode_button.addEventListener('click', () => {
  state.editMode = !state.editMode;
  setEditStatus(
    state.editMode
      ? 'Drag a unit start or numbered waypoint, then save or discard the staged edits.'
      : state.pendingEdits.size
        ? `${state.pendingEdits.size} edit${state.pendingEdits.size === 1 ? '' : 's'} remain staged. Save or discard them.`
        : '',
    state.editMode || state.pendingEdits.size ? 'active' : '',
  );
  updateEditControls();
  renderMap();
});
elements.save_manual_button.addEventListener('click', () => saveEdits([...state.pendingEdits.values()], 'Manual edit'));
elements.discard_edits_button.addEventListener('click', async () => {
  const discarded = state.pendingEdits.size;
  await loadScenario(state.selectedPath, { quiet: true });
  setEditStatus(`Discarded ${discarded} unsaved edit${discarded === 1 ? '' : 's'} and restored the saved scenario.`, 'success');
  updateEditControls();
});
elements.toggle_mask.addEventListener('change', () => state.maskOverlays.forEach((overlay) => overlay.setMap(elements.toggle_mask.checked ? state.map : null)));
elements.toggle_land.addEventListener('change', () => state.landOverlays.forEach((overlay) => overlay.setMap(elements.toggle_land.checked ? state.map : null)));
elements.toggle_routes.addEventListener('change', () => state.routeOverlays.forEach((overlay) => overlay.setMap(elements.toggle_routes.checked ? state.map : null)));
elements.toggle_satellite.addEventListener('change', () => state.map?.setMapTypeId(elements.toggle_satellite.checked ? 'hybrid' : 'terrain'));
elements.side_filter.addEventListener('change', () => {
  renderMissionDetails();
  renderMap();
  renderFindings({ refreshMapMarkers: false });
});
elements.settings_form.addEventListener('submit', async (event) => {
  const submitter = event.submitter;
  if (submitter?.value === 'cancel') return;
  event.preventDefault();
  const result = await window.missionMap.setMapsKey(elements.api_key.value);
  if (!result.saved) {
    elements.settings_message.textContent = result.error;
    return;
  }
  elements.settings_message.textContent = 'Saved with OS-backed encryption. Restarting map view…';
  setTimeout(() => window.location.reload(), 400);
});

window.missionMap.onScenarioChanged((filePath) => {
  if (filePath !== state.selectedPath || state.saving) return;
  elements.watch_status.textContent = 'UPDATING';
  loadScenario(filePath, { quiet: true }).finally(() => {
    elements.watch_status.textContent = 'LIVE';
  });
});

initialize();
