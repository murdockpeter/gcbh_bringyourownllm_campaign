# Campaign MVP Notes

## Intent

This campaign layer is external to the GCBH scenario files.

For now it does four jobs:

1. preserves a persistent order of battle
2. tracks unit condition between scenarios
3. tracks simple logistics and repair pressure
4. gives each follow-on mission a concrete starting state

## How To Use It

After each scenario, manually update `campaign_state_mvp.json`.

For each unit, update at minimum:

- `status`
- `structural_integrity_pct`
- `fuel_pct`
- `ammo_pct`
- `current_location`
- `repair`

If a unit is unavailable for the next mission, set:

- `mission_capable` to `false`
- `status` to `damaged`, `under_repair`, or `destroyed`

## MVP Conventions

`structural_integrity_pct`

- `85-100`: fully operational
- `60-84`: damaged but still fieldable
- `30-59`: crippled, emergency use only
- `0-29`: combat ineffective or destroyed

`readiness_pct`

- combines crew state, system health, and command confidence
- use this to decide if a unit should appear in the next scenario even if it physically survives

`ammo_pct`

- abstracted readiness, not exact launcher accounting
- the scenario files can still represent specific loadouts and partial depletion where useful

`daily_upkeep_points`

- simple burden metric for future campaign balancing
- higher values mean the platform is harder to sustain through repeated scenarios

## Follow-On Logic After Scenario 1

The assumed outcome used for Scenario 2 is:

- Blue survives the opening gauntlet
- `RFA Fort Victoria` is damaged badly enough to break the westbound timetable
- `USS Mason` remains combat capable
- `USS Tempest` remains usable but tired and partially depleted
- `Peykan` is sunk
- `Joshan` is damaged and out of the next immediate fight
- `Khanjar` remains available
- `Falakhon` is committed from reserve
- `Bastion 1` remains a live coastal threat

## Scenario 2 Operational Logic

Blue:

- pull the damaged ship east
- form a tighter defensive screen
- accept reinforcement and repair support
- avoid losing the campaign logistics backbone

Red:

- attack before Blue consolidates
- force a second hit on the damaged auxiliary
- keep the coalition from re-entering the Strait on schedule

## Goal Design Rule

Use only:

- `ProtectGoal`
- `DestroyGoal`
- `CompoundGoal`

Do not use:

- `TimeGoal`

Reason:

- the campaign should resolve around force survival, force destruction, and preservation of key assets
- timed goals in GCBH create failure states that do not map cleanly to the campaign logic we are building

## Near-Term Next Step

If Scenario 2 loads and plays correctly, the next useful upgrade is a small tool that reads the JSON state and emits the next scenario draft with:

- available units only
- reduced speed for damaged hulls
- partially depleted magazines
- date and location carried forward automatically

## Canonical Outcome After Operation Silver Current

The `silver_current_004` game logs, rather than the earlier planning assumption, now drive campaign turn 4:

- all three BLUE logistics ships survived
- `USS Tempest`, `HMS Diamond`, both Tiger aircraft, and `Broadarrow` were lost
- `USS Mason` survived with heavy damage and must withdraw at reduced speed
- both Iranian Phantom aircraft were lost
- all three Iranian FACs and every coastal node survived
- neither side completed its scenario objectives before the session was ended

## Scenario 4 Operational Logic

`Operation Sable Reprisal` is a bounded escalation. BLUE receives one fresh destroyer, replacement CAP, and a recovery base at Al Dhafra, but does not replace every loss. Its authority is limited to defending the withdrawal and striking designated nodes that directly supported the attacks.

Iran exploits the damaged screen with MiG-29 cover and a two-aircraft Su-24 anti-shipping package. The surviving FACs remain dangerous but are not mandatory BLUE targets, reducing the incentive to repeat the close-range fight that caused the Silver Current losses.

Because the game removed `AutoAttack` from player-controlled aircraft in the logged run, the briefing explicitly requires manual positive-control target designation for the Lancer strike package.

## Multiplayer Replay Branch and Scenario 5

The August 9 replay of `silver_current_004` replaces the earlier solo-loss outcome for campaign continuity. The replay ended before a formal victory, but all fifteen BLUE platforms survived without reported damage. Phantom 1, Phantom 2, and Shamshir were destroyed. The two remaining FACs and every coastal node survived.

`Operation Resolute Passage` doubles each side's original Silver Current order of battle: 30 BLUE assets and 24 RED assets. The reason for returning to Hormuz is logistical rather than symbolic. Six auxiliaries carry bulk aviation fuel, missile-defense reloads, repair modules, and medical stores required by the forward force in Bahrain; airlift cannot deliver those commodities at the necessary scale before contingency stocks are exhausted.

The carrier remains outside the Strait while the convoy, mine-countermeasure ships, and escorts proceed west through a real-coastline-checked traffic corridor. Iran responds with an exclusion zone, local frigate and missile-boat reinforcements, four MiG-29s, two Su-24s, and the surviving coastal kill chain. The authority remains corridor opening and protection, not a general attack on Iran.
