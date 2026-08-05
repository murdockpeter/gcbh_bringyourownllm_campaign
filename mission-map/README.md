# GCBH Mission Map

Electron desktop companion for visualizing and validating Global Conflict Blue: Horizon scenario coordinates.

## Features

- Reads the workspace's Python scenario files without executing them.
- Recognizes surface units from `Ship1` tasking, so newly added ship classes do not need to be hard-coded into the app.
- Watches the selected scenario and refreshes after it is saved.
- Detects legacy `longitude, latitude` and scenario v0.2.1 `latitude, longitude` `SetPosition` formats.
- Plots units, alliances, and routes on Google terrain or satellite maps.
- Overlays the project's conservative GCBH safe-water polygons.
- Uses Natural Earth 1:10m land and minor-island polygons for offline point-on-land, exact route/coast intersection, and distance-to-land checks.
- Highlights disagreements where the GCBH mask labels real-world land as safe.
- Suggests candidate water coordinates for invalid starts and route crossings when a mask-safe detour can be found.
- Applies validated green candidates with **Fix scenario**, writes a timestamped copy under `scenarios/_backups`, reloads the saved file, and immediately reruns every local check.
- Provides a manual edit mode: drag any unit start or numbered waypoint, then explicitly save or discard the staged coordinate changes.
- Samples each surface route every 0.5 nautical miles for local mask validation.
- Optionally checks up to 512 route samples with Google Elevation API.
- Stores the Google Maps key using Electron's OS-backed `safeStorage`; it is never written to this repository.

## API-key setup

The key previously pasted into chat must be revoked. Create a replacement key in a Google Cloud project with billing enabled.

Enable:

1. Maps JavaScript API
2. Elevation API (optional, required only for the Google elevation check)

Restrict the key to those APIs and use the website/referrer restriction:

```text
http://127.0.0.1:43117/*
```

Set conservative daily quotas and a billing alert. The app asks for the replacement key at runtime and encrypts it through the operating system.

## Run

```powershell
cd mission-map
npm install
npm test
npm start
```

Run the same layered preflight without opening Electron:

```powershell
npm run audit:scenarios
npm run audit:scenarios -- ..\scenarios\operation_gate_latch.py
```

The command exits nonzero when it finds mask or real-world placement errors, making it suitable for a future build/CI gate.

## Coordinate repair workflow

1. Run the full local comparison and review the red incidents and green candidate markers.
2. Use **Fix scenario** to apply all currently listed automatic candidates, or choose **Edit coordinates manually** and drag individual unit/waypoint markers.
3. Manual changes remain in memory until **Save manual edits** is selected. **Discard edits** reloads the current file from disk.
4. Every save creates a timestamped backup beside the scenarios in `_backups`, reloads the updated Python source, and reports remaining errors and additional fix candidates.

Automatic repair only changes structured `SetPosition` or `UI.add_waypoint_advanced` coordinates. A crossing whose destination is valid receives an inserted detour waypoint; an invalid destination waypoint is moved. Source lines are verified again at save time, so an externally changed file is rejected instead of being overwritten blindly.

The application automatically lists files under the workspace `scenarios` directory. **Browse…** can open a scenario elsewhere.

## Comparison semantics

The cyan polygons are not a real coastline. They are the project's conservative prediction of water that should be navigable in GCBH. Google Elevation is a separate real-world check:

- positive elevation above 2 m is reported as a possible land intersection;
- zero or negative elevation is treated as no detected land;
- coastal interpolation can produce false positives or false negatives.

The map and both validators should be reviewed together before changing scenario coordinates.

The orange/red coastline overlay is generated from the public-domain [Natural Earth 1:10m land dataset](https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-land/) and its minor-islands companion. Regenerate the clipped campaign data with:

```powershell
npm run data:coastline
```

Natural Earth is appropriate for regional mission planning but is not harbor-chart resolution. The Google elevation corroboration remains useful for borderline coastal positions.

## Security model

- The renderer is sandboxed.
- Node integration is disabled.
- Context isolation is enabled.
- The preload bridge exposes scenario selection/loading, structured coordinate edits, and encrypted key settings. Edits are accepted only for the scenario currently being watched.
- Renderer files are served only from a fixed loopback HTTP origin so Google referrer restrictions can be applied.
- External navigation and new windows are blocked.
