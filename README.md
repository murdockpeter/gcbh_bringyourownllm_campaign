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
