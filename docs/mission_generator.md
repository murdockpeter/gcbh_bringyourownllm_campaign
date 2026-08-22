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
- surface starts/routes, aircraft operating boxes/tracks, and ground positions;
- database-validated loadout overrides for platforms without a dated setup; and
- bounded variation for timing, sea state, reserve slots, contact visibility, positional jitter, surface-route variants, and air-route variants.

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

The database's own dated default loadout is authoritative. When a setup assigns several weapon groups to one simulator launcher index, the generator deterministically selects the highest-quantity group because `SetUnitLauncherItem` can emit only one active child class per launcher. Seed-level loadout overrides are required when a platform has no dated setup, and every override launcher/item pair is checked against `platform_launcher`, `launcher_configuration`, and `equipment_group` before generation.

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
- The generator does not mutate campaign state or ingest battle logs.
- Free-form LLM briefing generation is outside this rules-based pipeline.
- A theater without an explicit theater definition and placement geometry is rejected.
- A manual in-game load remains the final compatibility smoke test because the repository cannot execute the GCB Horizon runtime API directly.
