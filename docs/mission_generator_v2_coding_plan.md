# Mission Generator v2 Coding Plan

**Ticket:** [Mission Generator v2: state-driven, varied, validated missions](https://trello.com/c/oMu5ORv3/3-mission-generator-v2-state-driven-varied-validated-missions)

**Target:** Fully implemented, reviewed, and merged to `main` on August 22, 2026

**Runtime:** Node.js 24 (no new runtime dependencies)

**Status:** Implementation in progress on `feat/mission-generator-v2`

## 1. Outcome

Replace `tools/generate_operation_resolute_passage.cjs`, which hard-codes one scenario, with a reusable command-line generator that:

- consumes campaign state and a structured scenario seed;
- carries campaign losses, damage, fuel, ammunition, readiness, fatigue, repair, and logistics into the mission;
- selects a mission archetype and produces tactically distinct but deterministic variants;
- validates platform classes and loadouts against the local GCB Horizon SQLite database;
- constrains placement and routes using the theater mask and real-world coastline data;
- emits both a playable Python scenario and an explainable JSON manifest; and
- fails before writing output when it cannot produce a valid mission.

The existing Resolute Passage generator remains available as a reference until the replacement reproduces its essential scenario structure. It is not deleted in the first implementation pass.

## 2. Definition of Done

The ticket is done only when all of the following are true:

1. A CLI accepts `--state`, `--seed`, `--database`, `--output`, `--manifest`, and optional `--rng-seed` arguments.
2. The same normalized inputs and RNG seed produce byte-identical scenario and manifest files.
3. Destroyed or unavailable units are excluded unless the scenario seed contains an explicit, validated override.
4. Damage, speed limits, fuel, ammunition, fatigue/readiness, repair state, and sortie limits affect selection or emitted unit state and are explained in the manifest.
5. All seven ticket archetypes are recognized: convoy escort, withdrawal, corridor opening, interception, limited strike, reconnaissance, and recovery.
6. At least three archetypes have end-to-end fixtures proving distinct rosters, goals, briefings, and tactical layouts.
7. Generated objectives use only `ProtectGoal`, `DestroyGoal`, and `CompoundGoal`.
8. Platform classes, launcher items, launcher compatibility, and magazine items are checked against the local game database.
9. Generated surface starts and routes pass the existing theater-mask and real-coastline audit with zero errors.
10. Unit names are unique, coordinates use version `0.2.1` latitude/longitude order, playable-side briefings are present, and aircraft have viable recovery/tasking.
11. Unsatisfiable inputs produce an actionable error report and leave no partial scenario or manifest behind.
12. Automated tests and the targeted scenario audit pass on the feature branch and again after merge.
13. One generated scenario is loaded in GCB Horizon for a manual smoke test before merge.

## 3. Baseline and Constraints

- Existing mission-map tests: **21 passing**.
- `operation_resolute_passage.py`, `operation_sable_reprisal.py`, `operation_silver_current.py`, and `operation_ember_wake.py` currently audit with zero errors.
- The repository-wide audit is already red because legacy Gate Latch and Iron Shelter contain 49 known errors. Those legacy repairs are not part of this ticket. The merge gate is zero audit errors for every newly generated fixture and no regression in currently clean scenarios.
- The local game database exists at the documented `%USERPROFILE%` path, reports schema version 4, and is accessed read-only. The adapter supports compatible schema versions 2 through 4.
- Node 24's built-in `node:sqlite` API avoids a native or third-party SQLite dependency.
- Campaign ammunition is currently an abstract percentage. The generator must document its conversion to discrete launcher quantities rather than pretending exact inventory history exists.
- Generation is rules-based. Free-form LLM prose, automatic battle-log ingestion, campaign-state mutation, and support for theaters without a theater definition are separate follow-up work.

## 4. Architecture

```text
campaign state + scenario seed + RNG seed + game database
                         |
                         v
              validate and normalize inputs
                         |
                         v
        eligibility -> roster -> logistics/loadouts
                         |
                         v
       archetype -> objectives -> placement/routes
                         |
                         v
          balance and quality-gate evaluation
                         |
              +----------+----------+
              |                     |
              v                     v
       Python renderer        JSON manifest
              |                     |
              +----------+----------+
                         |
                         v
           parse + geography/loadout audit
                         |
                         v
              atomic output promotion
```

Core design rules:

- Keep calculation modules pure wherever possible; filesystem, database, and process concerns stay at the edges.
- Normalize all source formats into one internal mission model before rendering.
- Record every random draw and material rule decision in the manifest.
- Validate before output promotion: write temporary files, audit them, then rename them into place.
- Reuse `mission-map/src/scenario-parser.cjs`, `mission-map/src/theater-selector.cjs`, and `mission-map/renderer/geometry.js` rather than creating competing validators.

## 5. Planned File Layout

```text
package.json                                  # root test/generate scripts and Node >=24 contract
tools/generate_campaign_mission.cjs           # CLI entry point
tools/mission-generator/
  errors.cjs                                  # typed diagnostics and exit-code mapping
  inputs.cjs                                  # JSON loading, schema checks, normalization
  rng.cjs                                     # deterministic seeded PRNG and draw log
  database.cjs                                # read-only node:sqlite catalog adapter
  state.cjs                                   # campaign-state indexing and eligibility
  roster.cjs                                  # role/force selection
  logistics.cjs                               # fuel, ammo, damage, repair, sortie mapping
  archetypes.cjs                              # seven archetype definitions and dispatch
  objectives.cjs                              # Protect/Destroy/Compound goal model
  placement.cjs                               # starts, formations, patrols, reserves, routes
  balance.cjs                                 # explainable difficulty estimate and guardrails
  renderer.cjs                                # normalized mission model -> Python 0.2.1
  manifest.cjs                                # provenance and decision report
  validate-output.cjs                         # parser, database, geography, and mission gates
  generate.cjs                                # orchestration and atomic writes
campaign/next_scenario_seed_mvp.json           # first structured seed
schemas/scenario_seed.schema.json              # documented seed contract
schemas/generation_manifest.schema.json        # stable output contract
test/mission-generator/
  fixtures/                                   # small campaign branches and seeds
  inputs.test.cjs
  rng.test.cjs
  state.test.cjs
  database.test.cjs
  logistics.test.cjs
  archetypes.test.cjs
  objectives.test.cjs
  placement.test.cjs
  balance.test.cjs
  renderer.test.cjs
  generate.test.cjs
```

Implementation may combine very small modules, but responsibilities and test seams should remain intact.

## 6. Input Contracts

### Campaign state

Continue accepting the existing `campaign_state_mvp.json` structure. Normalize each unit into:

- stable identity: side, unit name, platform class;
- availability: status, mission-capable flag, structural integrity, readiness, repair state;
- operating limits: speed limit, fuel, ammunition, fatigue, sorties available;
- location and role hints; and
- logistics burden and side-level resource pools.

Reject duplicate unit identities, invalid percentages, unknown statuses, malformed repair fields, and missing side/state metadata. Preserve warnings for optional fields that can safely default.

### Scenario seed

The new seed schema contains:

- schema version, scenario ID/name, theater, date/time, playable side, and optional RNG seed;
- archetype, premise, operational intent, escalation constraints, and desired duration;
- required/protected/eligible roles and explicit include/exclude overrides;
- geography anchors, route direction, operating areas, and minimum clearances;
- force and logistics budgets;
- objective stakes, thresholds, and optional-objective policy; and
- variation ranges for timing, reserves, weather, axes, patrols, and uncertainty.

Unknown fields are rejected in the first schema version to catch misspellings. Any override that resurrects an unavailable unit must include a reason recorded in the manifest.

## 7. Determinism and Provenance

- Implement a small, tested seeded PRNG with no dependency on `Math.random()`.
- Canonicalize normalized JSON before hashing it.
- Resolve the effective seed in this order: CLI override, seed file, stable hash of normalized state plus scenario seed.
- Sort database queries and candidate lists before random selection.
- Record input hashes, effective seed, generator version, database schema version, selected/rejected units, loadout calculations, random draws, objectives, placement decisions, balance factors, warnings, and audit results.
- Exclude timestamps and absolute machine-specific paths from deterministic content. If operational metadata is needed, place it in a clearly non-reproducible CLI log rather than the manifest.

## 8. State-to-Mission Rules

### Availability

- Exclude `destroyed`, `mission_capable: false`, and units still inside a required repair window.
- Treat structural integrity below 30% as unavailable by default.
- Use readiness, fatigue, and sortie capacity to rank eligible units and cap air sorties.
- Allow seed-level required units only when they remain physically eligible; contradictory requirements fail with a diagnostic.

### Damage and speed

- Cap emitted speed at the lowest of platform mission speed, campaign speed limit, and archetype/formational limit.
- Structural damage and readiness contribute to the balance score and manifest even when the scenario API cannot express individual subsystem damage directly.
- Never silently convert an unavailable unit into a healthy replacement.

### Fuel and ammunition

- Emit `SetFuelFraction` from `fuel_pct` where the scenario API supports it.
- Choose a database-valid role loadout, then scale expendable quantities by `ammo_pct`, launcher capacity, and side ordnance budget using deterministic rounding.
- Preserve defensive minimums only when inventory permits; otherwise downgrade the role or reject the candidate.
- Never load an item that is absent from the item tables or incompatible with the launcher.

### Repair, fatigue, and sorties

- Repair windows gate availability.
- Fatigue and readiness alter selection weight, reserve timing, and sortie caps; they do not directly invent unsupported simulator attributes.
- Basing, tanker, carrier compatibility, runway, recovery, and maintenance capacity must support every generated aircraft package.

## 9. Archetype and Objective Composition

Every archetype defines required roles, layout strategy, legal variation, primary stakes, and goal composition:

| Archetype | Core player problem | Typical goal structure |
|---|---|---|
| Convoy escort | Preserve logistics while crossing a threat area | Protect convoy + destroy blocking force |
| Withdrawal | Extract damaged/high-value units under pressure | Protect withdrawing assets + limited attrition goal |
| Corridor opening | Suppress a bounded kill chain and clear transit | Compound surface/shore destruction + protected transit force |
| Interception | Stop a hostile package before it reaches a defended area | Destroy named/role targets + protect defended asset |
| Limited strike | Neutralize designated nodes within escalation limits | Destroy designated nodes; optional force-protection goal |
| Reconnaissance | Preserve sensors while classifying or exposing threats | Protect reconnaissance assets + destroy only emergent threats |
| Recovery | Retrieve or cover stranded/damaged forces | Protect recovery unit and recovered asset + suppress pursuers |

Goal thresholds are derived from stakes and force feasibility, then checked so neither side begins in an already-won or impossible state. Optional goals affect score/briefing but cannot contradict the primary campaign intent. `TimeGoal` is never emitted.

## 10. Placement, Routes, and Tactical Variation

- Select starts and routes from theater anchors and safe-water polygons, with the real coastline as the final authority.
- Generate formations from role-aware spacing rules instead of copying one coordinate line.
- Keep surface routes at least the seed's required clearance from land and inside valid water where the mask is authoritative.
- Place ground units on land and within the declared operating area.
- Give aircraft valid patrol/strike tracks, compatible altitude/speed, and a recovery base or carrier.
- Vary only within explicit seed ranges: start offsets, approach axis, patrol geometry, reserve timing, sea state, and package selection.
- Bound retries. If constrained placement cannot succeed after the configured attempt limit, return the best diagnostics instead of producing a suspect scenario.

## 11. Balance Model

Use an explainable heuristic, not a claim of simulation accuracy. Score each side from:

- surviving force capability and role coverage;
- readiness, fatigue, damage, fuel, ammunition, and sortie availability;
- sensor and battle-management support;
- weapon reach and defensive depth;
- geography, initiative, reserve timing, and route exposure; and
- objective burden and protected-asset vulnerability.

Emit component scores, the final ratio, and warnings for extreme mismatches. Balance warnings do not automatically add units; roster changes must remain within campaign and seed constraints.

## 12. Implementation Sequence

### Slice 0 — Branch and baseline

1. Create `feat/mission-generator-v2` from current `main`.
2. Record current test and audit results in the PR description.
3. Add the root package scripts without changing existing mission-map behavior.

**Gate:** existing 21 tests still pass; known legacy audit failures are documented.

### Slice 1 — Contracts, errors, RNG, and manifest skeleton

1. Add seed and manifest schemas.
2. Implement strict input validation and normalization.
3. Implement deterministic RNG, canonical hashing, diagnostics, and initial manifest.
4. Add unit tests for malformed inputs and repeated generation seeds.

**Gate:** normalized inputs and RNG draws are deterministic and snapshot-tested.

### Slice 2 — Campaign state, database, roster, and logistics

1. Index campaign units and apply availability/repair rules.
2. Add the read-only SQLite catalog adapter and schema-version check.
3. Resolve role-capable platforms and legal launcher/magazine items.
4. Apply fuel, ammunition, speed, fatigue/readiness, sortie, basing, and logistics constraints.
5. Record accepted and rejected candidates with reasons.

**Gate:** fixtures prove unavailable units never leak into output and impossible loadouts fail clearly.

### Slice 3 — Archetypes, objectives, and briefing

1. Implement the seven archetype definitions.
2. Build reusable objective and briefing composers.
3. Enforce escalation constraints and objective feasibility.
4. Add distinct end-to-end fixtures for convoy escort, withdrawal, and limited strike; add unit coverage for the other four archetypes.

**Gate:** no generated source contains `TimeGoal`; goal trees and briefings match the chosen archetype.

### Slice 4 — Placement, routing, rendering, and balance

1. Implement constrained starts, formations, patrols, routes, and reserves.
2. Reuse theater selection and geometry validators.
3. Render version `0.2.1` Python with unique names, alliance setup, tasks, sensors, loadouts, fuel, goals, and briefings.
4. Add balance scoring and warnings.
5. Write to temporary files, parse/audit, then atomically promote outputs.

**Gate:** all generated fixtures parse and audit with zero errors and are byte-identical on rerun.

### Slice 5 — Migration, documentation, and merge

1. Express Resolute Passage as the first structured seed and generate a comparison candidate without overwriting the hand-verified scenario.
2. Document CLI examples, state mappings, manifest fields, diagnostics, and known limitations.
3. Run the full automated suite, syntax checks, targeted audits, and deterministic reruns.
4. Load one generated scenario in GCB Horizon and record the smoke-test result.
5. Review the diff, remove temporary output, commit in logical slices, open/update the PR, and merge only after every gate passes.

**Gate:** clean working tree after merge, `main` contains the implementation, and the Trello checklist is complete.

## 13. Test Matrix

| Area | Required coverage |
|---|---|
| Inputs | valid MVP state, missing required fields, bad percentages, duplicate units, unknown fields |
| RNG | same seed/same output, different seed/allowed variation, stable candidate ordering |
| Availability | destroyed, mission-incapable, repair-gated, low-integrity, explicit overrides |
| Logistics | speed caps, fuel fractions, deterministic ammo rounding, depleted inventory, sortie caps |
| Database | missing DB, wrong schema version, unknown platform/item, incompatible launcher, legal loadout |
| Archetypes | all seven recognized; required roles and legal variations enforced |
| Objectives | only approved goal types, feasible thresholds, no pre-satisfied or impossible goals |
| Geography | safe starts, land-based ground units, clear surface routes, bounded placement failure |
| Aviation | carrier/runway compatibility, tanker needs, recovery path, maintenance/sortie capacity |
| Rendering | valid Python structure, unique names, lat/lon convention, briefings, tasks, goals |
| Balance | component accounting, extreme-ratio warning, no unauthorized force injection |
| End to end | three archetype fixtures, zero audit errors, atomic failure, deterministic manifest/output |

## 14. Verification Commands

The implementation will expose root scripts equivalent to:

```powershell
npm test
npm run check
npm run generate -- --state campaign/campaign_state_mvp.json --seed campaign/next_scenario_seed_mvp.json --rng-seed 20260822 --output scenarios/generated_mission.py --manifest scenarios/generated_mission.manifest.json
npm run audit:generated -- --scenario scenarios/generated_mission.py
git diff --check
git status --short
```

The final verification record must include:

- automated test totals and failures (expected: zero);
- syntax-check result;
- targeted audit results for every generated fixture (expected: zero errors);
- deterministic file-hash comparison;
- manual GCB Horizon load result; and
- the final merge commit on `main`.

## 15. Commit and Review Plan

Use small reviewable commits:

1. `build: add generator scripts and input contracts`
2. `feat: add deterministic campaign state and database planning`
3. `feat: add mission archetypes objectives and briefings`
4. `feat: add constrained placement rendering and manifests`
5. `test: add generator fixtures audits and end-to-end coverage`
6. `docs: document mission generator workflow`

Before merge, inspect the complete diff for accidental scenario rewrites, local database paths, generated temporary files, credentials, and unrelated user changes. Do not commit the local GCBH database or Google Maps settings.

## 16. Risks and Cut Decisions

| Risk | Mitigation / decision |
|---|---|
| Ticket breadth threatens same-day completion | Implement one compositional engine; archetypes are data/rules, not seven separate generators. Merge only with every Definition of Done item satisfied. |
| Existing abstract ammo cannot reconstruct exact magazines | Use documented deterministic scaling and manifest the approximation. Do not claim exact persistence. |
| Legacy repository audit is already failing | Gate newly generated and currently clean scenarios; track legacy repair separately. |
| Database differs across game versions | Check schema version and fail with the queried class/item and corrective guidance. |
| Geography search becomes expensive or non-terminating | Pre-index coastline data, use bounded candidates/retries, and surface diagnostics. |
| Simulator APIs cannot express all campaign damage | Apply supported limits, use selection/balance effects for the rest, and state the mapping in the manifest. |
| Generated Python loads syntactically but fails in game | Require one manual GCB Horizon smoke load before merge. |
| Requirement changes during implementation | Update the seed/schema and this plan first; do not hide scope changes inside renderer code. |

## 17. Merge Rule

“Fully merged today” means merged only after the tests, targeted audits, deterministic rerun, review, and manual game-load smoke test are complete. If any gate fails, the branch remains unmerged and the ticket remains in progress with the exact failing gate recorded; schedule pressure does not lower the acceptance criteria.
