# Operation Resolute Passage

## After Action Report — 23 August 2026 Playthrough

### Report status

This report reconstructs the completed combat session recorded in `20260823140729_Operation_Resolute_Passage.txt.acmi` and its brief saved-game continuation. It distinguishes confirmed combat effects from likely scenario or simulation artifacts. It does not modify canonical campaign state.

## 1. Executive assessment

BLUE achieved a decisive air-to-air victory and protected the entire six-ship logistics force during the recorded period, but did not accomplish the overall mission. All six RED combat aircraft—two Su-24M Fencers and four MiG-29 Fulcrums—were destroyed by AIM-120D fire between approximately 14:04:57 and 14:07:38. RED's S-300 fired nine 48N6E2 missiles without a confirmed hit; eight were logged as misses and one remained airborne when the session was saved.

The tactical success was offset by the loss of Wildcat 2 and moderate damage to Wildcat 1. Both Strike Eagles entered the gun engagement envelope of the surviving FACs while at approximately 7,600 metres. Khanjar's 76 mm fire destroyed Wildcat 2; Falakhon's 76 mm fire damaged Wildcat 1 to approximately 62 percent remaining health. Wildcat 2's aircrew ejected, but the logs do not establish recovery.

The game awarded the RED-surface destruction subgoal because six of nine listed combatants were lost. That result should not be treated as six legitimate combat kills. None appears in the weapon-damage report. Four ships sank at essentially the same coordinate, while Tsunami 1 reached zero health only ten seconds after scenario start. The evidence strongly indicates route convergence, collision, grounding, or another scenario/simulation artifact.

No coastal node was damaged or destroyed. The convoy had not completed its westbound passage when the session ended. The correct operational assessment is therefore:

- **Air battle:** decisive BLUE victory.
- **Convoy protection during recorded action:** successful; all six auxiliaries survived undamaged.
- **Surface battle:** nominal objective passed, but the result is contaminated by non-combat losses.
- **Coastal kill chain:** intact.
- **Corridor opening:** not demonstrated.
- **Overall mission:** not accomplished when play stopped.

## 2. Evidence reviewed

- Primary Tacview recording: `20260823140729_Operation_Resolute_Passage.txt.acmi`
- Saved-game continuation: `20260823145934_Operation_Resolute_Passage.txt.acmi`
- GC:BH session log: `Logs/log-1.txt`
- GC:BH continuation log: `Logs/log.txt`
- Damage report: `Logs/damage_summary.csv`
- Goal report: `Logs/goal_status.txt`
- Final simulator state: `Logs/unit_state.xml`
- User-provided Tacview screenshot at scenario time 14:11:03
- Scenario source: `scenarios/operation_resolute_passage.py`

Tacview and the GC:BH text log differ by several seconds on some damage timestamps. The sequence, shooters, targets, weapons, and outcomes agree. Timeline times below use the Tacview reference clock unless otherwise noted.

## 3. Mission and initial forces

BLUE's mission was to escort six auxiliaries westward through Hormuz, destroy at least six of nine RED surface combatants, and neutralize at least three of five designated coastal kill-chain nodes. The scenario began with 54 assets:

- **BLUE, 30 assets:** six auxiliaries; eight surface escorts; two MCM vessels; one carrier; one recovery base; two F/A-18F fighters; eight F-15Es divided among Lancer, Viper, and Wildcat flights; two P-8 MPAs; one E-2D; and one KC-135R.
- **RED, 24 assets:** five Kaman FACs; two Moudge frigates; two Tsunami missile boats; three Bastion batteries; three Pantsir systems; one S-300 site; one radar post; one airstrip; four MiG-29s; and two Su-24Ms.

The coalition's political authority remained limited to opening and holding the corridor and striking the designated coastal kill chain. It did not authorize a general attack on Iran.

## 4. Chronology of the action

### 14:00:00–14:04:50 — Initial movement and long-range SAM pressure

The convoy and escorts proceeded generally west-northwest while BLUE aviation established its operating geometry. The S-300 Site North began engaging early. Its first two recorded 48N6E2 shots targeted Broadarrow. Subsequent missiles targeted Viper and Tiger aircraft.

Tsunami 1 reached zero health at 14:00:10 without a recorded weapon impact. Tsunami 2 reached zero health at approximately 14:03:42, also without a recorded weapon impact. These early losses were not caused by documented BLUE weapons.

### 14:04:52–14:07:38 — BLUE wins the air battle

Tiger and Viper flights launched a coordinated 22-missile AIM-120D salvo series. The resulting engagement destroyed the entire RED airborne force:

| Approx. time | RED loss | Credited BLUE action |
|---|---|---|
| 14:04:57 | Fencer 1, Su-24M | Hit by Tiger 1 and Viper 1; killed by Tiger 2 |
| 14:05:25 | Fencer 2, Su-24M | Killed by Viper 2 |
| 14:06:02 | Fulcrum 4, MiG-29 | Killed by Viper 1 |
| 14:06:28 | Fulcrum 3, MiG-29 | Killed by Viper 1 |
| 14:06:59 | Fulcrum 2, MiG-29 | Killed by Tiger 1 |
| 14:07:38 | Fulcrum 1, MiG-29 | Hit by Tiger 1; killed by Viper 2 |

Fulcrum 1 launched the only recorded RED air-to-air weapon, an R-73 against Viper 1. It missed. RED's intended coordinated fighter/strike attack therefore collapsed before either Su-24 could attack the convoy.

BLUE expended 22 AIM-120Ds for nine confirmed damaging impacts and six kills. The missile hit rate was approximately 41 percent and the shot-to-kill rate approximately 27 percent. The simultaneous assignments caused some overkill—especially against Fencer 1—but ensured that no RED attacker penetrated toward the logistics formation.

### 14:05:33–14:09:58 — RED surface losses accumulate

IRIS Sahand, Zolfaghar, Scimitar, and Dagger successively reached zero health. All four stopped and sank at approximately 26.4049 N, 56.4880 E. No BLUE surface, air-to-surface, or anti-ship weapon impact was recorded against them, and none appears in `damage_summary.csv`.

Together with the two Tsunami losses, these six units caused the game to mark the surface-destruction goal complete. Because the losses lack weapon attribution and four occupy nearly identical sink positions, they are assessed as probable navigation/route-convergence or collision losses. This is an inference from the logs, not an explicitly labeled simulator event.

Khanjar, Falakhon, and IRIS Dena remained operational.

### 14:10:59–14:11:33 — Wildcat flight enters the FAC gun engagement

Khanjar and Falakhon opened high-angle fire with 76 mm HE-MOM rounds against Wildcat 2 and Wildcat 1. IRIS Dena subsequently fired 40 mm HE-T at Wildcat 1. The Strike Eagles were still at approximately 7,599 metres altitude, but their horizontal separation from the FACs had closed to roughly 7–13 kilometres.

At approximately 14:11:08 Tacview time, Khanjar hit Wildcat 2 from an estimated 14.8-kilometre slant range, reducing it to about 52 percent health. Falakhon hit Wildcat 1 from roughly 15.4 kilometres slant range, leaving it at approximately 62 percent health. Continued Khanjar fire reduced Wildcat 2 to near-zero health and delivered the fatal hit from approximately 10.6 kilometres slant range. GC:BH reported moderate damage, then heavy damage, destruction, and ejection.

Wildcat 1 survived and continued southwest at the save point. IRIS Dena's 55 recorded 40 mm rounds missed it.

### 14:12:17 onward — Save and termination

The primary recording ended after 744.56 seconds of scenario time, at approximately 14:12:25. The saved game was briefly reloaded. The continuation recording preserved Wildcat 1 at 62 percent health, the four sunken RED surface units, and one 48N6E2 still in flight; no new combat result occurred before the simulator closed.

## 5. Strike Eagle loss — interpretation of the supplied Tacview image

The screenshot freezes the engagement at 14:11:03, during the opening seconds of the FAC barrage. The viewpoint looks across the Strait toward Wildcat flight and the larger BLUE air package. Wildcat 2 is prominent above and ahead of the other aircraft, with Wildcat 1, Tiger, Viper, Broadarrow, Trident, and Lancer elements spread behind it. The curved yellow traces climbing from the surface are the most important feature: they show the 76 mm shells rising in a dense ballistic stream toward the two Strike Eagles.

The image makes clear that this was not a SAM kill or a MiG kill. RED aviation had already been destroyed. Wildcat 2 was caught by naval gunfire from Khanjar while crossing close to the surviving surface group. Tacview records Wildcat 2 near 7.6 kilometres altitude and heading roughly southwest during the engagement. Khanjar fired 39 rounds in several high-angle strings; three rounds are credited in the GC:BH damage summary. One caused moderate damage, follow-on fire caused heavy damage, and the final registered impact destroyed the aircraft. Falakhon simultaneously fired 24 rounds at Wildcat 1 and scored one damaging hit.

Operationally, the picture captures a failure to separate the shore-strike package from an unsuppressed surface threat. The Wildcats were not low, but they were horizontally close enough for the simulator's naval guns to engage them. The surviving FACs were known hostile units and had not been neutralized or masked before the strike aircraft crossed their engagement zone. The air package had defeated the sophisticated fighter and SAM threats, then accepted an avoidable exposure to comparatively simple gunfire.

The engagement also deserves a simulator-realism review. Repeated effective 76 mm fire against fast jets at approximately 25,000 feet and 10–15 kilometres slant range is mechanically possible in this run, but its lethality and accuracy should be checked against intended GC:BH weapon behavior. The tactical lesson remains valid regardless: do not route valuable strike aircraft over an intact surface gun group.

## 6. Loss and damage accounting

### BLUE

| Unit | Result | Cause | Campaign confidence |
|---|---|---|---|
| Wildcat 2, F-15E | Destroyed; ejection reported | Three credited 76 mm HE-MOM hits from Khanjar | High; aircrew recovery unknown |
| Wildcat 1, F-15E | Moderate damage; about 62% health remaining | One 76 mm HE-MOM hit from Falakhon | High |
| Six logistics ships | Undamaged and afloat | No recorded hits | High for recorded period |
| All other BLUE assets | No recorded damage | — | High for recorded period |

### RED — confirmed combat losses

| Unit | Result | Cause |
|---|---|---|
| Fencer 1 | Destroyed | Three AIM-120D hits; Tiger/Viper engagement |
| Fencer 2 | Destroyed | AIM-120D from Viper 2 |
| Fulcrum 1 | Destroyed | AIM-120D hits from Tiger 1 and Viper 2 |
| Fulcrum 2 | Destroyed | AIM-120D from Tiger 1 |
| Fulcrum 3 | Destroyed | AIM-120D from Viper 1 |
| Fulcrum 4 | Destroyed | AIM-120D from Viper 1 |

### RED — probable non-combat or artifact losses

| Unit | Zero-health time | Evidence |
|---|---:|---|
| Tsunami 1 | 14:00:10 | No weapon event; failed almost immediately |
| Tsunami 2 | 14:03:42 | No weapon event or damage-summary entry |
| IRIS Sahand | 14:05:33 | No weapon event; sank at shared convergence coordinate |
| Zolfaghar | 14:06:23 | Same shared coordinate |
| Scimitar | 14:08:04 | Same shared coordinate |
| Dagger | 14:09:58 | Same shared coordinate |

### RED survivors of immediate campaign significance

- Khanjar and Falakhon remained combat-effective and demonstrated a lethal gun threat.
- IRIS Dena remained afloat and fired 55 rounds at Wildcat 1 without a hit.
- All three Bastion batteries remained intact.
- All three Pantsir systems remained intact.
- S-300 Site North and Coastwatch 1 remained intact.
- Bandar Abbas Strip remained intact, although its assigned combat aircraft were destroyed.

## 7. Weapon employment summary

| Side / shooter | Weapon | Rounds or missiles | Recorded result |
|---|---|---:|---|
| Tiger 1 | AIM-120D | 5 | One kill; two additional damaging contributions |
| Tiger 2 | AIM-120D | 6 | One kill |
| Viper 1 | AIM-120D | 5 | Two kills; one additional hit |
| Viper 2 | AIM-120D | 6 | Two kills |
| S-300 Site North | 48N6E2 | 9 | Eight misses; one unresolved/in flight at save |
| Fulcrum 1 | R-73 | 1 | Miss against Viper 1 |
| Khanjar | 76 mm HE-MOM | 39 | Wildcat 2 destroyed |
| Falakhon | 76 mm HE-MOM | 24 | Wildcat 1 damaged |
| IRIS Dena | 40 mm HE-T | 55 | No hits |

No BLUE anti-ship missile, bomb, or other air-to-surface release appears in the Tacview weapon inventory. This agrees with the lack of damage to the coastal network and reinforces the conclusion that the six RED ship losses were not BLUE weapon kills.

## 8. Objective assessment

| Objective | Game status | Evidence-based assessment |
|---|---|---|
| Preserve at least five of six logistics ships | Accomplished | All six were intact at termination |
| Destroy at least six of nine surface combatants | Accomplished by game | Six were lost, but apparently through artifacts rather than BLUE combat action |
| Destroy at least three of five coastal nodes | Not accomplished | No target was damaged or destroyed |
| Compound BLUE mission | Not accomplished | Shore objective failed; transit was incomplete |

The displayed score of 100 should not be used as the campaign result. The goal file explicitly marks the compound mission unaccomplished, and the nominal surface success is not operationally trustworthy.

## 9. What went well

- BLUE achieved complete air superiority before RED strike aircraft could threaten the convoy.
- Viper and Tiger flights coordinated effectively and survived the air battle.
- The single RED R-73 shot missed, and all resolved S-300 engagements missed.
- The convoy remained undamaged.
- The carrier, tanker, AEW aircraft, MPAs, escorts, and MCM force remained available.
- The Tacview recording provides enough fidelity to distinguish actual weapon kills from misleading objective credit.

## 10. What requires correction

### Tactical execution

- Wildcat flight crossed too close to unsuppressed FACs.
- Surface threat suppression and strike routing were not sufficiently coordinated.
- BLUE expended 22 AIM-120Ds against six aircraft. The result was decisive, but target assignment produced avoidable duplicate shots.
- The coastal strike never produced a weapon release or target effect.
- The convoy had not yet demonstrated safe passage through the decisive corridor.

### Scenario construction

- RED surface routes appear to funnel several units through one exact point, producing probable collision or navigation losses.
- Tsunami 1 fails within ten seconds and should be checked for spawn safety, class behavior, and nearby collision geometry.
- Surface-goal credit currently accepts non-combat losses, which can create a false victory signal.
- Naval-gun performance against high-altitude fast jets should be reviewed for intended realism.
- A save/reload preserved projectiles already in flight. This is expected continuity, but it confirms that campaign assessment should combine both Tacview segments.

## 11. Recommendations for the next attempt

1. Repair RED surface starts and routes so each ship has deconflicted lanes and staggered waypoints.
2. Replay the scenario before treating any RED surface loss as canonical.
3. Hold Wildcat and Lancer outside the FAC gun envelope until the surface picture is classified and the intended corridor is suppressed.
4. Assign explicit shooter/target pairs to Tiger and Viper flights to reduce AIM-120D overkill.
5. Preserve at least one CAP element between surviving hostile aircraft and the convoy rather than allowing every fighter to collapse onto the same target set.
6. Use a deliberate sequence: establish air superiority, suppress or bypass the S-300, neutralize designated shore nodes, clear the surface corridor, then advance the convoy.
7. Confirm Wildcat 1's recovery and Wildcat 2 aircrew status before applying campaign persistence.
8. Do not update campaign state from the six surface losses until the route/collision issue is resolved.

## 12. Proposed campaign interpretation — not yet applied

If this playthrough is accepted as a completed campaign action, the defensible persistent facts are:

- Wildcat 2 destroyed; aircrew ejected, recovery unresolved.
- Wildcat 1 damaged to approximately 62 percent health and requires recovery/repair assessment.
- All four RED MiG-29s destroyed.
- Both RED Su-24Ms destroyed.
- BLUE spent 22 AIM-120Ds across Tiger and Viper flights.
- RED expended at least nine 48N6E2 missiles, one R-73, 63 rounds of 76 mm ammunition, and 55 rounds of 40 mm ammunition.
- All six BLUE logistics ships and every BLUE surface vessel survived undamaged through the recorded period.
- The RED coastal kill chain survived intact.
- Khanjar, Falakhon, and IRIS Dena remained operational.
- The status of Tsunami 1, Tsunami 2, IRIS Sahand, Zolfaghar, Scimitar, and Dagger should remain **disputed/non-canonical pending scenario repair and replay**.
- The corridor was not confirmed open and the sealift had not completed transit.

## 13. Final judgment

Operation Resolute Passage produced a compelling air battle and a vivid tactical reversal. BLUE destroyed the entire RED air package without allowing an attack on the convoy, but then lost a Strike Eagle to the very surface force it had not credibly defeated. The mission ended with the logistics force intact, air superiority established, and the coastal kill chain untouched.

The session should be recorded as a **partial tactical success with an unresolved operational outcome**, not a campaign victory. Its strongest campaign lesson is that standoff discipline must apply after the air battle as rigorously as during it. Its strongest development lesson is that Tacview-aware validation is necessary: route-driven self-destruction can currently satisfy objectives and distort both the AAR and the next campaign state.
