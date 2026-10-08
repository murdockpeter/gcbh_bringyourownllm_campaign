# Operation Baltic Shield - First Contact

## Starting situation

Fictional alternate timeline: **15 June 2026, 07:30 Baltic local time**, following ten days of warning, maritime incidents and precautionary deployments. Reciprocal weapons fire began overnight. No general land invasion has begun. Both alliances are hostile at scenario start; NATO is playable.

A NATO supply vessel is moving north off Latvia with two frigates. Russian forward corvettes and a limited raid package attempt to disrupt the supply corridor and Latvian forward aviation. Allied shore air defenses and radars support the air battle; a Russian coastal missile battery and air-defense sector protect the southern approaches. Estonia's air base is a second campaign-critical node whose survival matters beyond this mission.

This force is designed to be plausible after warning and modest reinforcement, rather than an exact contemporary intelligence ORBAT. National ownership, actual deployments and aircraft variants are not asserted. The scenario represents the air-maritime/coastal component of combined arms. It does not simulate infantry, armored maneuver or territorial occupation.

## Order of battle

| NATO component | Quantity | Game representation | Purpose |
|---|---:|---|---|
| Air-defense frigate | 1 | Sachsen FFGHM | Escort air defense and command |
| ASW frigate | 1 | Brandenburg FFGHM | Escort and future ASW continuity |
| Fleet replenishment vessel | 1 | Henry J Kaiser | Protected sustainment asset |
| CAP fighters | 4 | Typhoon | Two maritime CAP and two northern CAP aircraft |
| SEAD aircraft | 2 | Tornado ECR (Germany) | Player-directed anti-radiation strike |
| Precision-strike aircraft | 2 | F-16C/D Block 50 | Player-directed conventional strike |
| Maritime patrol | 1 | P-8 MPA | Surface reconnaissance; limited anti-ship and ASW weapons |
| Airborne early warning | 1 | E-3C | Air picture support |
| Tanker | 1 | KC-135R | Refueling option; no automatic rendezvous scripted |
| Forward air bases | 2 | Airbase | Amari and Lielvarde geographic recovery nodes |
| Allied SAM detachments | 2 | Patriot PAC-2 / PAC-3 | Fictional reinforcing air-defense nodes |
| Shore radar nodes | 2 | Generic radar classes | Local air surveillance |
| **NATO total** | **20** | | |

| Russian component | Quantity | Game representation | Purpose |
|---|---:|---|---|
| Forward corvettes | 2 | Pr 20380 Steregushchiy | Contest the supply corridor |
| Supporting frigate | 1 | Pr 11540 Yastreb | Support the surface force and withdrawal |
| Fighter cover | 4 | Su-27 | Cover the limited raid |
| Maritime-strike aircraft | 2 | Su-24M | Database-compatible Kh-59MK missile loadout |
| Land-strike aircraft | 2 | Su-24M | Kh-29T / KAB-500L precision-strike loadout |
| Recovery airfield | 1 | Airstrip (Russia) | Generic Kaliningrad recovery node |
| SAM sector | 1 | S-300PMU-2 | Abstract local air-defense element |
| Point defense | 1 | Pantsir-S1 | Defend the southern coastal sector |
| Coastal missile element | 1 | K-300P Bastion-P | Two P-800 Oniks ready rounds |
| Coastal radar | 1 | Generic Radar Post 170 | Surface/air surveillance support |
| **Russian total** | **16** | | |

The NATO frigate roles follow the [German Navy's description of the Sachsen/Brandenburg force](https://www.bundeswehr.de/en/organization/navy/structure/flotilla-2/2-frigate-squadron). Frigates and maritime patrol aircraft are consistent with the regional presence described in [NATO's Baltic Sentry announcement](https://www.nato.int/en/news-and-events/articles/news/2025/01/14/nato-launches-baltic-sentry-to-increase-critical-infrastructure-security). Neither source establishes this fictional force's deployment.

Russian ship project names were found in the installed database, correcting the earlier search based only on Western class names. The Su-27 and Su-24 choices are legacy game representations; they do not stand in silently for Su-30SM or a complete modern Russian air force. The Kh-59MK loadout is accepted by the game database and is a scenario abstraction rather than a verified unit-specific weapons certification. Patriot placements, the Russian battery and radar coordinates are fictional operating locations on validated land, not actual deployed sites. Each ground platform is a game node, not a literal full regiment or an exact count of real launch vehicles.

## Player mission

All three victory conditions must be met:

1. Preserve **Baltic Sustainment 1, Amari Air Base and Lielvarde Air Base**.
2. Destroy at least **two of the four Fencer strike aircraft**.
3. Destroy at least **one of the two forward Russian corvettes**.

Russia's opposing goal is destruction of any one of the three protected assets. The supply vessel's survival is the escort objective; reaching a geographic arrival box is not implemented. Four hours is the planning window, not a hard runtime timeout. The game can reach a result earlier or continue longer.

The coast battery, radar, SAM and point-defense nodes are available for selective suppression when necessary. They are not mandatory victory targets, which leaves a useful follow-on coastal mission. The Russian airfield is not a NATO target under the briefing's commander intent. Written targeting limits are not engine-enforced whitelists.

## Initial player checklist

- Check the supply ship's screen and the southern maritime contacts first. Corvettes start close enough for an early missile engagement once detected.
- Keep maritime CAP over the escort and decide whether northern CAP should reinforce Latvia. The initial pressure is concentrated on the convoy and Latvian airfield.
- Protect the AEW, tanker and maritime patrol aircraft. Their routes are operating tracks, not automatically guaranteed safe or beyond enemy weapon reach.
- Raven SEAD, Falcon precision-strike and Seeker MPA have no `AutoAttack` task at start. Issue attack orders when needed. Removing or replacing their looping Nav task may be necessary when assigning a new mission.
- Use Raven's AGM-88B only against designated emitting threats. Falcon carries laser-guided bombs, so check illumination/designation behavior before committing it. No scripted joint laser-designation sequence is supplied.
- Keep recoverable aviation alive. Combat aircraft are already airborne; no automatic launch waves or timed reinforcements are scripted. Airfield recovery capacity and large-support-aircraft suitability need the first in-game check; national support recovery is off map.
- Record losses, ammunition expenditure, fuel, facility damage and the game result for manual campaign-state reconciliation.

All scripted aviation starts airborne. The technical loadouts are conventional, individually database-validated and explicit where dated setups were missing. The coastal battery's inconsistent database default was replaced with P-800 Oniks. Its ready-round override does not add a magazine of reloads. No hosted-aircraft all-loadout catalog is stocked in this scenario.

## Campaign mission variety

These are proposed branches, not scenarios already generated or timed events in the opener.

| Follow-on mission | Trigger or purpose | Different player problem |
|---|---|---|
| Defensive counter-air / base recovery | Raid reaches a forward airfield | Keep surviving fighters operational; transfer support |
| Emergency escort / withdrawal | Supply ship or frigate damaged | Extract a slow force under air cover |
| Coastal suppression | Coastal battery/radar survives and blocks sustainment | Reconnaissance, SEAD and limited precision strike |
| Maritime interception | Corvette survives or withdraws | Locate and intercept it before regrouping |
| ASW corridor clearance | Introduce a confirmed submarine threat after depth review | Use MPA, frigate sensors and suitable helicopters |
| Combat rescue / recovery support | Aircraft or vessel lost | Protect a separately authored recovery force |
| Reinforcement escort | Supply ship survives and stocks permit reinforcement | Protect follow-on lift under a different threat mix |
| Reconnaissance / battle-damage assessment | Shore attacks occur | Preserve sensors and establish what remains active |
| Northern sector defense | Crisis moves towards Gulf of Finland | New geometry, dispersed bases and air interception |

Avoid making every turn a destroy-everything battle. Retain named survivors, carry losses and resource expenditure forward, and bring reinforcements only after credible preparation/transit time. The opener intentionally has no submarine or minefield: those require depth/bathymetry checks and dedicated mission mechanics. Rescue units, helicopters and neutral traffic can be introduced in their relevant missions rather than forced into this first combat turn.

## Generate, inspect and play

```powershell
npm run generate:baltic-shield
npm run audit:generated -- scenarios/operation_baltic_shield.py
```

Authoritative inputs: `campaign/campaign_state_baltic_shield.json` and `campaign/scenario_seed_baltic_shield.json`. Output: `scenarios/operation_baltic_shield.py`; provenance: `scenarios/operation_baltic_shield.manifest.json`.

The generated mission is copied into `%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\UserScenarios\My_Scenarios\operation_baltic_shield.py`, which supplies the game's **My Scenarios** list. Select **Operation Baltic Shield - First Contact** there after leaving and reopening scenario selection, or restarting the game if it retains a cached list. The initial copy to the Steam install's `scenarios/Workshop` did not make it available in My Scenarios; the user-data copy corrects that installation mistake. Regenerating in the workspace does not automatically update the playable copy. Automated coastline, loadout, objective, continuity and repeatability checks passed. The balance heuristic reports 0.875 (NATO/Russia effective strength), with no balance warning; this is not a playtest or a prediction of fairness.

First in-game checks: scenario loads, both alliances and all units appear, missile/aircraft AI acts, guided weapons work, recoveries are possible, and victory/failure thresholds behave as intended. The repository cannot execute the simulator. The SVP is an assumed shallow-water design profile, not measured hydrography. Ships use offshore validated masks; those masks do not check simulator seabed depth.
