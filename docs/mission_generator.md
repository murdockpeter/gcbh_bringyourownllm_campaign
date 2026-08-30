# Mission Generator v2

Mission Generator v2 creates a playable GCB Horizon Python scenario from persistent campaign state and a structured mission seed. It also creates a JSON manifest explaining unit selection, exclusions, state mappings, loadouts, placements, objectives, random decisions, balance scoring, and validation results.

## Requirements

- Node.js 24 or newer
- A local GCB Horizon database (schema versions 2 through 4)
- A theater definition in `theaters/`
- The real-world coastline dataset used by `mission-map`

The default database path is:

```text
%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\Database\database.db
```

Pass `--database` to use a different database. The database is opened read-only and is never copied into the repository.

## Generate

```powershell
npm run generate -- `
  --state campaign/campaign_state_mvp.json `
  --seed campaign/next_scenario_seed_mvp.json `
  --rng-seed 20260822 `
  --output scenarios/generated_mission_v2.py `
  --manifest scenarios/generated_mission_v2.manifest.json
```

Add `--choose-loadouts` to pause before generation and pick platform-wide aircraft loadouts from numbered lists. The menu includes every date-valid database setup plus the seed's custom presets, shows the stores in each choice, saves the selections back to the seed, and then continues generation. Press Enter or choose `0` to retain the current selection or database default.

The effective RNG seed is resolved in this order:

1. `--rng-seed`
2. `rng_seed` in the scenario seed
3. a stable hash of the normalized campaign state and scenario seed

Repeated generation with the same normalized inputs, game database, and effective seed produces byte-identical scenario and manifest files.

## State mapping

The generator applies campaign state as follows:

| Campaign field | Generation effect |
|---|---|
| `status`, `mission_capable` | Destroyed and mission-incapable units are excluded |
| `structural_integrity_pct` | Units below 30% are excluded; other damage contributes to balance and provenance |
| `speed_limit_kts` | Caps generated mission speed when greater than zero |
| `fuel_pct` | Emitted through `SetFuelFraction` |
| `ammo_pct` | Scales database loadout quantities with deterministic rounding |
| `readiness_pct` | Affects roster ranking and balance |
| `crew_fatigue_pct` | Reduces roster ranking and effective strength |
| `repair` | Active repair windows can prevent selection |
| `sorties_available_next_12h` | Prevents unavailable aircraft from being tasked and records sortie capacity |

Subsystem damage that the scenario API cannot express is retained in the manifest and affects selection/balance rather than being silently discarded.

## Seed contract

`schemas/scenario_seed.schema.json` documents the version 1 contract. Unknown top-level fields are rejected. The seed controls:

- scenario identity, theater, date/time, playable side, and archetype;
- operational premise, side intent, and escalation limits;
- force caps and explicit include/exclude requirements;
- explicit in-scenario or documented off-map aviation recovery support;
- protected and designated target sets and quantities;
- independent named destruction groups when one mission requires separate thresholds, such as suppressing three coastal nodes while neutralizing two pickets;
- surface starts/routes, aircraft operating boxes/tracks, and ground positions;
- named loadout selections, mission-specific loadout presets, and database-validated launcher overrides;
- bounded variation for timing, sea state, reserve slots, contact visibility, positional jitter, surface-route variants, and air-route variants.
- per-unit presence directives (`active`, `reserve`, `staged`, or `maintenance`), host platforms, tasks, starts, and routes for story-critical formations.
- executable continuity assertions for required selections and exclusions, participation states, forbidden tasks, exact launcher totals, force counts, and unique surface waypoints.

Supported archetypes are:

- `convoy_escort`
- `withdrawal`
- `corridor_opening`
- `interception`
- `limited_strike`
- `reconnaissance`
- `recovery`

Archetypes provide role requirements, default objective targets, tactical framing, and briefing language. Seeds supply theater-specific geometry and may narrow the target set.

## Database behavior

Platforms are resolved from the `ship`, `air`, `simpleair`, `ground`, and `sub` tables. Dated setups and launcher/magazine contents come from `platform_setup`, `launcher_loadout`, and `magazine_loadout`.

The database's own dated default loadout remains authoritative when the seed makes no choice. A seed can select a date-valid database `SetupName` or a mission-specific named preset through `loadout_selections`. A named-unit selection takes precedence over a platform-class selection. Existing `loadout_overrides` remain the highest-priority escape hatch and are authoritative for exact launcher state.

```json
{
  "loadout_selections": {
    "F/A-18F": "AW2",
    "Tiger 1": "SM1",
    "F-15E": "standoff strike"
  },
  "loadout_presets": {
    "F-15E": {
      "standoff strike": [
        { "launcherId": 0, "item": "GBU-39 SDB", "quantity": 8 },
        { "launcherId": 1, "item": "AIM-120D", "quantity": 2 },
        { "launcherId": 2, "item": "AIM-9X", "quantity": 2 }
      ]
    }
  }
}
```

Selection precedence is: named-unit `loadout_overrides`, platform-class `loadout_overrides`, named-unit `loadout_selections`, platform-class `loadout_selections`, then the deterministic database default. Every custom preset and override is checked against `platform_launcher`, `launcher_configuration`, and `equipment_group` before generation. When a database setup assigns several weapon groups to one simulator launcher index, the generator deterministically selects the highest-quantity group because `SetUnitLauncherItem` can emit only one active child class per launcher.

For aircraft emitted as `staged` or `maintenance`, the generator also builds an aviation-store catalog on their declared carrier or airbase. It includes every date-valid database loadout plus every scenario preset known for that aircraft class. The host receives, for each store type, enough inventory to give every hosted aircraft one complete copy of whichever catalog loadout uses the most of that store; host `ammo_pct` scales the final quantity. The selected loadout is still applied to the aircraft at scenario start, while the alternate stores allow the player to change a reserve aircraft's loadout in the flight-deck interface. The manifest records the catalog and resulting host inventory.

“All database loadouts” is literal. If the game database defines special or nuclear configurations as date-valid for an aircraft, their stores are included. Campaign authors who do not want those options should use a platform with an appropriately constrained database catalog until an exclusion policy is added.

## Quality gates

Generation completes in memory before either output is promoted. The generated scenario must:

- parse as scenario version `0.2.1` with latitude/longitude coordinates;
- contain unique unit names;
- use no `TimeGoal`;
- select the requested theater;
- pass safe-water and real-coastline validation;
- keep ground nodes on land; and
- give every combat aircraft with `AutoAttack` a launcher loadout.

An unsatisfied state, roster, objective, database, or geography constraint raises a coded diagnostic and produces no scenario or manifest.

Run the external audit again with:

```powershell
npm run audit:generated -- scenarios/generated_mission_v2.py
```

## Manifest

`schemas/generation_manifest.schema.json` documents the stable manifest envelope. It includes:

- input hashes and effective RNG seed;
- every labeled random draw;
- selected units and carried-forward campaign state;
- allocated versus available campaign logistics and aviation support decisions;
- applied speed, fuel, loadout, sortie, task, position, and route values;
- rejected units and reasons;
- goal trees and thresholds;
- explainable balance components and warnings;
- parser/geography audit findings; and
- a hash of the generated scenario.

The manifest intentionally excludes generation timestamps and machine-specific absolute paths so it remains reproducible.

## Tests

```powershell
npm run check
npm test
```

The generator tests cover input validation, deterministic RNG, availability, roles, logistics, all seven archetypes, objectives, placement failures, balance, rendering, live database integration, three end-to-end archetype fixtures, deterministic reruns, and audit-clean output. Database integration tests skip only when the local game database is not installed.

## Known boundaries

- Campaign ammunition is an abstract percentage, not exact launcher history; the deterministic scaling rule and result are recorded in the manifest.
- A scenario may override a named unit's loadout when the campaign has exact launcher-history evidence. Staged and maintenance aircraft are emitted on their declared carrier or airfield instead of being forced airborne.
- Host aviation magazines are stocked only for aircraft actually emitted on that host; off-map and already-airborne aircraft do not add rearm inventory.
- The generator does not mutate campaign state or ingest battle logs.
- Free-form LLM briefing generation is outside this rules-based pipeline.
- A theater without an explicit theater definition and placement geometry is rejected.
- A manual in-game load remains the final compatibility smoke test because the repository cannot execute the GCB Horizon runtime API directly.
