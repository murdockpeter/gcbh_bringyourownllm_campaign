# Route Validation

## Purpose

This project now includes a preflight validator for ship start positions and ship waypoint legs in the Hormuz theater.

It is designed to catch:

- ship spawns that start on land
- ship waypoints that fall on land
- ship route segments that cross unsafe coastal space between valid points

## Files

- [validate_scenario_routes.ps1](/C:/Users/Peter%20G.%20Robbins/Documents/claudeprojects/gcbh_dynamic_campaign/tools/validate_scenario_routes.ps1:1)
- [hormuz_mvp.json](/C:/Users/Peter%20G.%20Robbins/Documents/claudeprojects/gcbh_dynamic_campaign/theaters/hormuz_mvp.json:1)

## How It Works

This is a conservative theater-specific safe-water mask, not a full decoded terrain engine.

For now it uses:

- a hand-authored safe-water polygon set for the Strait of Hormuz / Gulf of Oman
- parsing of `unit.SetPosition(...)` for known surface-ship classes
- parsing of `UI.add_waypoint_advanced(...)` for those same units
- line sampling along each ship leg to catch route crossings

## Command

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\validate_scenario_routes.ps1 -ScenarioPath .\scenarios\operation_ember_wake.py
```

## Current Workflow

Before copying a new scenario into the game:

1. Generate or edit the scenario file in the workspace.
2. Run the validator against it.
3. Fix any reported starts or waypoints.
4. Only then copy it into `scenarios\Workshop`.

## Limits

- It only validates surface classes listed in the theater JSON.
- It is intentionally conservative, so some legal in-game water positions may still be flagged if they are too close to shore.
- It currently only knows the Hormuz campaign area.

## Next Upgrade

The obvious next step is to wire scenario generation through this validator so bad points get snapped automatically before the file is written.
