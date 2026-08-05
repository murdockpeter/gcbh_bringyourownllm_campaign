# GCBH Dynamic Campaign Context: Strait of Hormuz Seed

## Purpose

This workspace note captures enough local game context to start writing the first small scenario in a larger Indian Ocean / Strait of Hormuz operation for **Global Conflict Blue: Horizon**.

The target game install inspected for this note is:

`C:\Program Files (x86)\Steam\steamapps\common\Global Conflict Blue Horizon`

## What The Game Uses For Scenarios

Scenarios are plain Python files.

Observed stock locations:

- `scenarios\Standalone\*.py`
- `scenarios\Tutorials\*.py`
- `scenarios\Workshop\` appears to be the custom-content location and is currently empty
- `scenarios\_Templates\Blank2.py` is the cleanest base template

Tutorials can also use sidecar XML files:

- `scenarios\Tutorials\Air_Air_Tutorial.xml`

For our campaign opener, the simplest path is:

1. Author a Python scenario file first.
2. Avoid tutorial XML unless we explicitly want guided steps.
3. Place the custom draft under the workspace first, then copy or mirror it into the game `Workshop` folder when ready to test.

## Core Scenario Structure

The stock template and shipped scenarios use two main functions:

- `ScenarioInfo()`
- `CreateScenario(SM)`

Key scenario manager patterns observed:

- `SM.SetScenarioInfo(info)` or separate setters like `SetScenarioName`, `SetScenarioDescription`
- `SM.CreateAlliance(...)`
- `SM.AddAllianceCountry(...)`
- `SM.SetAlliancePlayable(...)`
- `SM.SetAllianceRelationship(...)`
- `SM.SetUserAlliance(...)`
- `SM.SetDateTime(...)`
- `SM.SetStartTheater(lon, lat)`
- `SM.SetSeaState(...)`
- `SM.SetSVP(...)`
- `SM.SetSimpleBriefing(...)`
- `SM.GetDefaultUnit()`
- `SM.AddUnitToAlliance(unit, alliance_id)`
- `SM.SetUnitLauncherItem(...)`
- `SM.AddToUnitMagazine(...)`
- `SM.AddUnitToFlightDeck(...)`
- `SM.SetFlightDeckUnitLoadout(...)`
- `SM.SetAllianceGoal(...)`
- `SM.SetAllianceROEByType(...)`

Typical unit-side scripting pattern:

- `UI = SM.GetUnitInterface(unit.unitName)`
- `UI.AddTask('Aircraft1', ...)`, `UI.AddTask('Ship1', ...)`, `UI.AddTask('Ground1', ...)`
- optional: `UI.AddTask('AutoAttack', ...)`, `UI.AddTask('Nav', ...)`, `UI.AddTask('PointDefense', ...)`
- optional routeing with `UI.add_waypoint_advanced(lat, lon, alt, speed)`

## Data Model Findings

The game ships a SQLite database here:

- `database\database.db`

Relevant tables confirmed:

- `ship`
- `air`
- `simpleair`
- `ground`
- `platform_launcher`
- `launcher_loadout`
- `platform_names`

Important detail:

- Some valid aircraft classes used by stock scenarios are in `simpleair`, not only `air`.
- That means scenario authoring should rely on verified class names from stock scenarios and direct DB lookups, not assumptions.

## Verified Platform Classes Useful For Hormuz

These were confirmed locally from the database and/or stock scenarios.

### Blue / coalition candidates

Surface:

- `Arleigh Burke IIA DDGHM`
- `Ticonderoga CG Baseline 4`
- `Cyclone PBFM`
- `Oliver Hazard Perry FF`
- `Type 45 DDG`
- `Fort Victoria AOR`

Aircraft:

- `F/A-18E`
- `F/A-18F`
- `F-15E`
- `F-16C/D Block 50`
- `Typhoon`
- `KC-135R` from `simpleair`
- `E-2C` from `simpleair`
- `E-737 AEW&C` from `simpleair`
- `P-8 MPA` from `simpleair`
- `SH-60B` from `simpleair`

Ground / support:

- `Airbase`
- `Airstrip`
- `Airstrip(USA)`
- `Generic Radar Post 170`
- `Generic Mobile Radar Post 170`
- `MIM-104 Patriot PAC-2`
- `MIM-104 Patriot PAC-3`

### Red / Iranian-style candidates

Surface:

- `Kaman FACM`

Ground / coastal defense:

- `K-300P Bastion-P`
- `Pantsir-S1`
- `S-300PMU-2`
- `S-400 Triumf`

Note:

- The database is not region-complete. Some Iranian or Gulf-state orders of battle are missing or represented indirectly.
- For a believable GCBH scenario, it is reasonable to use a generic Red alliance with a mix of locally plausible classes, as the stock scenarios already do this with `Blue` and `Red` alignments.

## Verified Example Naming Pool

`platform_names` contains example names we can reuse.

Examples:

- `Arleigh Burke IIA DDGHM`: `USS Dewey`, `USS Jason Dunham`, `USS Mason`, `USS Truxtun`
- `Cyclone PBFM`: `USS Firebolt`, `USS Tempest`, `USS Typhoon`
- `Type 45 DDG`: `HMS Diamond`, `HMS Defender`, `HMS Duncan`
- `Kaman FACM`: `Peykan`, `Joshan`, `Falakhon`, `Khanjar`

Using existing names is safer than inventing unit names that may clash with the tone of the stock content.

## What The Built-In AI Tasks Suggest

Confirmed task scripts under `scripts\tasks\` include:

- `aircraft1.py`
- `ship1.py`
- `ground1.py`
- `auto_attack.py`
- `air_refuel.py`
- `ship_attack.py`
- `ship_defense.py`
- `asw_patrol.py`

Behavior implications from the scripts read:

- `Aircraft1` adds basic fuel recovery logic and idle behavior.
- `Ship1` adds defensive behavior and host-aircraft refuel support.
- Stock scenarios routinely layer `AutoAttack`, `Nav`, `PointDefense`, and platform-domain tasks together.

That supports a first mission centered on:

- a small escort or interception problem
- modest autonomous red behavior
- limited blue micromanagement requirements

## Recommended First Scenario Scope

Do not start the campaign with a carrier battle or full theater strike.

The right first scenario is a **tight, 45-90 minute opening action** with:

- one playable side only
- 6 to 14 total combat units
- one clear objective
- one escalation twist
- room for a follow-on scenario outcome

## Recommended Opening Scenario Concept

Working title:

- `Operation Gate Latch`

Narrative purpose:

- open the larger campaign with a limited maritime security crisis instead of immediate general war
- establish coalition presence east of the Strait of Hormuz
- force the player to identify hostile intent before a larger escalation

Scenario premise:

- A coalition escort group is moving a high-value tanker or logistics vessel through the Gulf of Oman toward the Strait of Hormuz.
- Iranian fast attack craft and a concealed coastal anti-ship missile battery are posturing near the choke point.
- The player must keep the escorted vessel alive, classify the threat, and neutralize only the units that cross the threshold to hostile action.

Why this is the right opener:

- small battlespace
- clear geography
- immediate tension
- reusable surviving units for later scenarios
- easy branching based on losses, time, and whether the coastal battery is found

## Recommended Geography

Use the eastern approaches to the Strait of Hormuz, not the inner Persian Gulf, for the first mission.

Recommended center:

- around `56.5 E, 26.3 N`

Useful sub-areas:

- Gulf of Oman staging area east of Musandam
- northbound / westbound shipping lane toward Hormuz
- Iranian side for hidden coastal threat positions
- Omani side for coalition radar / air support framing

Why east of the strait first:

- gives maneuver room
- reduces map congestion
- allows later scenarios to move west into the choke point itself
- makes escalation feel progressive across the campaign

## Recommended Force Package For Scenario 1

### Blue

- 1 `Arleigh Burke IIA DDGHM`
- 1 `Cyclone PBFM`
- 1 civilian or low-value escort stand-in if available, otherwise a renamed auxiliary placeholder
- 2 `F/A-18F` or 2 `Typhoon` on station or quick reaction
- optional 1 `KC-135R` or `E-2C` off-map support flavor if the scenario needs air persistence

### Red

- 2 to 4 `Kaman FACM`
- 1 `K-300P Bastion-P` hidden inland
- 1 `Pantsir-S1` protecting the missile battery
- optional radar cueing with `Generic Radar Post 170`

## Recommended Player Objective

Primary:

- escort the valuable ship through the approach lane

Secondary:

- identify and destroy the coastal missile battery before it scores a hit

Failure conditions:

- escorted ship destroyed
- destroyer destroyed
- scenario timeout after the convoy fails to clear the threat area

## Campaign Hook For Follow-On Scenarios

This opener should feed later branching:

- if blue loses only the patrol craft, next mission is a retaliatory coastal strike
- if the escorted vessel is damaged but survives, next mission is emergency withdrawal and air cover
- if the Bastion battery survives, next mission is SEAD / maritime strike inside the strait
- if red FACs escape, later missions can reuse surviving named boats

## Practical Authoring Rules For The First Draft

- Use `Blank2.py` as the starting template, not a complex stock scenario.
- Keep only one playable side.
- Use a stock thumbnail first; visuals can wait.
- Prefer `SetScenarioInfo(info)` over mixed setters for consistency.
- Start with fixed unit placement and no randomization.
- Use verified class names only.
- Limit custom scripting to standard tasks unless the stock behaviors prove insufficient.

## Next Concrete Step

The next implementation pass should create:

1. a workspace scenario draft Python file
2. a small force list with exact unit names
3. initial coordinates for each unit near `56.5 E, 26.3 N`
4. basic blue and red goals
5. simple ship and aircraft tasks only

That is enough to produce the first playable mission before adding polish, branching, or a full campaign state model.
