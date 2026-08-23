# GCB Horizon Bring-Your-Own-LLM Campaign

Scenario-development workspace and supporting desktop tools for a dynamic Global Conflict Blue: Horizon campaign centered on the Strait of Hormuz.

## Contents

- `scenarios/` — playable Python scenario drafts using the current latitude/longitude coordinate convention.
- `mission-map/` — Electron map, coastline validator, scenario repair workflow, and automated tests.
- `campaign/` — campaign state and design notes.
- `theaters/` — conservative navigable-water masks.
- `docs/` — database, scenario-interface, and route-validation references.
- `tools/` — scenario validation and coordinate-modernization utilities.

## Test and run

```powershell
cd mission-map
npm install
npm test
npm run audit:scenarios
npm start
```

Google Maps credentials are configured at runtime and stored outside the repository using Electron's operating-system-backed encryption. Do not commit API keys or a local GCB Horizon database.

## Generate a campaign mission

Mission Generator v2 turns persistent campaign state and a structured scenario seed into a validated GCB Horizon Python scenario plus a deterministic JSON manifest.

```powershell
npm install
npm run generate -- --state campaign/campaign_state_mvp.json --seed campaign/next_scenario_seed_mvp.json --rng-seed 20260822 --output scenarios/generated_mission_v2.py --manifest scenarios/generated_mission_v2.manifest.json
npm run audit:generated -- scenarios/generated_mission_v2.py
npm test
```

Node.js 24 or newer and the local GCB Horizon database are required. See `docs/mission_generator.md` for the input contract, state mappings, validation behavior, and troubleshooting.
