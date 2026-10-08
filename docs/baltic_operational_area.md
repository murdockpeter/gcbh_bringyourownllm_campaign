# Baltic operational area: Latvia and Estonia

Prepared 8 October 2026. Operational geography and generator readiness are established. A fictional opening combat situation is now authored in `docs/operation_baltic_shield_briefing.md`; later campaign branches remain open for discussion.

## Area and scale

The theater `baltic_latvia_estonia` covers **18-30 E, 54.5-60.3 N**, centered for planning on **24 E, 57.4 N**. Latvia and Estonia are the focus, with Lithuanian support, eastern Gotland approaches, Kaliningrad and the Gulf of Finland towards Kronstadt in the wider envelope.

| Coverage comparison | Width at middle latitude | North-south distance |
|---|---:|---:|
| Hormuz | 351 nm | 348 nm |
| Baltic | 388 nm | 348 nm |

Distances are great-circle edge distances rounded to the nearest nautical mile. Baltic coverage is about 10% wider and the same height. This compares full coverage envelopes, not approved maneuver water. Copying longitude degrees would produce a much narrower area at Baltic latitudes.

Six conservative water masks cover the eastern Baltic, waters west of the Estonian islands, western Irbe approaches, an offshore Irbe passage, the Gulf of Riga and the central Gulf of Finland. Four route templates pass both water-mask and real-coastline validation at 1 nm clearance. All masks were additionally sampled on a 0.01-degree grid with no sampled land points. Sampling is not a geometric proof or a navigation chart.

The eastern Baltic and Irbe templates use overlapping masks. Riga and Gulf of Finland patrol pockets are separate: a direct route between pockets is not approved. Harbors, Muhu/Vainameri passages, shoals and eastern Gulf of Finland transits need additional work.

## Files and use

| File | Purpose |
|---|---|
| `theaters/baltic_latvia_estonia.json` | Automatically discovered coverage and water masks |
| `campaign/baltic_operational_area.json` | Reusable routes, land references, air boxes, platform catalog and planning decisions |
| `campaign/campaign_state_baltic_setup.json` | Synthetic turn-zero state independent of Hormuz history |
| `campaign/scenario_seed_baltic_setup.json` | Three-unit technical test with NATO/Russia alliance definitions |
| `scenarios/baltic_setup_validation.py` | Generated technical fixture, not the campaign opener |
| `scenarios/baltic_setup_validation.manifest.json` | Selection, loadout, placement, balance and audit provenance |

```powershell
npm run generate:baltic-setup
npm run audit:generated -- scenarios/baltic_setup_validation.py
```

Open the fixture in Mission Map to inspect the area. Theater JSON is discovered automatically. The operational catalog is a planning resource, not a generator input contract: copy selected geometry into actual mission seeds. The fixture's June 2026 date and units are arbitrary technical choices.

## How the current generator works

1. **Normalize inputs:** `inputs.cjs` validates persistent campaign state and the version-one mission seed. Unknown seed fields fail. Normalized inputs are hashed.
2. **Resolve variation:** a repeatable RNG comes from the CLI seed, seed-file value or normalized-input hash. Supplied limits govern timing, weather, reserves, visibility, jitter and route variants.
3. **Index availability:** `state.cjs` resolves platforms in the installed read-only SQLite database. Destroyed, incapable, critically damaged and repair-bound units are excluded. Roles are inferred from unit/class names.
4. **Select forces:** `roster.cjs` obeys caps, required/excluded units and objective targets. Readiness, fatigue and integrity rank optional units. Missing required assets cause failure.
5. **Apply logistics:** `logistics.cjs` allocates abstract resources, caps speed, emits fuel fractions and scales ammunition. Exact overrides precede named presets and dated database defaults. Aviation needs recovery support. Hosted aircraft may receive alternative-loadout stores.
6. **Build objectives:** seven archetypes provide defaults; seeds can supply protect/destroy targets and independent destruction groups. Compound/protect/destroy goals are emitted without a `TimeGoal`.
7. **Place and task:** exact unit directives override side-wide starts, tracks and boxes. Aircraft can be airborne or hosted. Standard AI tasks and patrol loops are emitted. The generator consumes routes; it does not autonomously plan them.
8. **Check continuity and balance:** assertions enforce participation, losses, tasks, launcher totals and force counts. Balance is a heuristic, not a battle prediction.
9. **Validate output:** the rendered Python must parse with current coordinates, select the correct theater, have unique names, place ships/routes inside safe water and clear of land, keep ground units on land and give combat aircraft loadouts.
10. **Write artifacts:** successful generation writes Python plus a deterministic manifest. Identical normalized inputs, RNG and database reproduce identical artifacts. The generator does not ingest battle results or advance campaign state: after-action reconciliation remains manual.

See `docs/mission_generator.md` and `tools/mission-generator/generate.cjs` for the full input contract and orchestration.

## Database readiness

The installed database was queried read-only. The catalog records platform presence, domain, date-valid 2026 setups and default launcher counts. Database availability does not establish service status, national ownership or actual regional deployment.

Surface candidates include Sachsen, Brandenburg, Type 45, Arleigh Burke IIA, Fort Victoria and `Pr 20380 Steregushchiy`. Air candidates include Typhoon, Gripen E, P-8, Su-27, Su-24M and MiG-29. Generic airfields, radar posts, Bastion, Pantsir and S-400 exist. Gotland is a submarine candidate needing separate depth and route review.

A name-family search did not find Visby, Hamina, Buyan, Karakurt, Neustrashimyy, Sovremenny, Udaloy or Kilo. This is not an exhaustive absence claim; project designations or alternative spellings may exist. Do not silently substitute unrelated platforms. Aircraft variants and dated loadouts still require a historical decision.

## Changes and limits for a realistic buildup

The renderer previously hard-coded USA/UK and Iran memberships. Seeds may now supply optional `alliances.blue` and `alliances.red`, each with `name` and `countries`. The fixture uses NATO (Germany/UK for the test vessels) and Russia. Existing Hormuz seeds retain their rendering. Check additional country tokens in-game when expanding nationalities.

The generator still sets both alliances **Hostile** and emits the existing ROE values. Briefing escalation constraints do not enforce political authorization or change hostility over time. Reconnaissance also supplies combat goals. A noncombat buildup requires a reviewed extension for relationships, ROE, incident triggers and noncombat objectives, or deliberately authored early scenarios. The technical fixture does not implement those mechanics.

Other boundaries:

- Role inference does not recognize `Airbase` as a base or `S-400 Triumf` as air defense without suitable naming. Names containing `Air Base` and `SAM` respectively address this heuristic until roles become configurable.
- Sea state and SVP are mission inputs. The inherited generic SVP is not a Baltic seasonal measurement. Ice, mines and shallow-water behavior remain undecided.
- Coastline polygons are not harbor charts, bathymetry or the game's terrain. Land-reference coordinates are approximate geographic anchors, not exact facility or naval berth placements.
- Hosted-aircraft store catalogs include every date-valid database configuration. Conventional-only aviation stores need an explicit policy before staging aircraft.
- Neutral traffic, infrastructure damage, disputed attribution and reinforcement arrival schedules are not automatically simulated by theater files.
- Manual game loading remains necessary to verify runtime API compatibility.

## Context for the next discussion

[NATO's January 2025 Baltic Sentry announcement](https://www.nato.int/en/news-and-events/articles/news/2025/01/14/nato-launches-baltic-sentry-to-increase-critical-infrastructure-security) supports infrastructure protection and maritime surveillance as regional starting context. It does not establish responsibility for every incident or imply immediately hostile forces.

[NATO's Baltic Air Policing description](https://ac.nato.int/missions/air-policing/baltics) provides allied air-policing context. The catalog includes Amari, Lielvarde and Siauliai reference locations without asserting which contingent is deployed on our eventual date. Geographic validation uses the repository's [Natural Earth land dataset](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_10m_land.geojson).

Next choose date/season, the initiating incident, initial forces, reinforcement lead times, civilian traffic, attribution uncertainty and the threshold for changing ROE. Those choices can then become campaign state and an opening mission. The setup does not place coastal weapons or strike assets at real facilities.
