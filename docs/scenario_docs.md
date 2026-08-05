# Scenario Interface Documentation

Scenarios are Python `.py` files placed under `%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\UserScenarios`. The engine calls two functions in each file: `ScenarioInfo()` and `CreateScenario(SM)`.

---

## File Structure

```python
from math import *
from random import *

def ScenarioInfo():
    d = dict()
    d['description'] = "Scenario description text"
    d['name']        = 'My Scenario'
    d['author']      = 'Author Name'
    d['thumb']       = 'thumbnail.png'      # filename in scenarios/Images/
    d['playableSides'] = 'Blue,Red'         # comma-separated alliance names
    d['date']        = 'January 2025'
    d['unitCount']   = 10                   # approximate, informational only
    return d

def CreateScenario(SM):
    # SM is a ScenarioInterface object
    info = ScenarioInfo()
    SM.SetScenarioName(info['name'])
    SM.SetScenarioDescription(info['description'])
    SM.SetScenarioAuthor(info['author'])
    SM.SetScenarioThumbnail(info['thumb'])
    # ... rest of setup
```

---

## Querying the Database

The game database is a SQLite file at `%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\Database\database.db`.

### Best tool: Python sqlite3 (command line)

Run ad-hoc queries directly without opening any app:

```powershell
python3 -c "
import sqlite3, os
conn = sqlite3.connect(os.path.expandvars(r'%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\Database\database.db'))
c = conn.cursor()
c.execute(\"SELECT DatabaseClass, targetFlags FROM missile WHERE DatabaseClass LIKE '%Exocet%'\")
for row in c.fetchall(): print(row)
conn.close()
"
```

**Do not modify the database. Use only SELECT or other statements that do not change the database.**

This is the fastest way to verify weapon capabilities, check platform names, or explore loadout configs before writing scenario code.

### dbeditor GUI

Build and run the `dbeditor` project in Visual Studio. Use it for browsing and editing entries. Best for multi-table navigation and making changes to the database.

### Key tables to query when building scenarios

| Question | Table(s) |
|---|---|
| Does this platform exist? | `platform_setup` — check `DatabaseClass` |
| What launchers does it have? | `platform_launcher` WHERE `DatabaseClass = '...'` |
| What is the default loadout? | `launcher_loadout` WHERE `DatabaseClass = '<platform>-L'` |
| Can this weapon hit ships? | `missile.targetFlags & 0x0001` |
| Is this platform available in year X? | `platform_setup.Year` ≤ X AND (`FinalYear` = 0 OR `FinalYear` ≥ X) |
| What sensors does it carry? | `platform_sensor` WHERE `DatabaseClass = '...'` |

---

## ScenarioInterface (SM)

### Scenario Metadata

```python
SM.SetScenarioName(name)
SM.SetScenarioDescription(text)
SM.SetScenarioAuthor(author)
SM.SetScenarioThumbnail(filename)         # image file in scenarios/Images/
SM.SetScenarioInfo(dict)                  # dict of arbitrary key/value metadata
SM.SetScenarioLocked(bool)               # prevent in-game editing
SM.SetSimpleBriefing(alliance_id, text)  # briefing text shown before play
SM.IsUsingNATONames()                    # returns bool
SM.GetDisplayName(class_name)            # returns display name string for platform class
```

For `SetSimpleBriefing`, keep briefing text under ~4000 characters. Use triple-quoted strings for multi-line content.

### Time and Environment

```python
SM.SetDateTime(year, month, day, hour, minute, second)
SM.SetDateTimeByString('MM/DD/YYYY')
SM.GetScenarioDateAsString()             # returns 'MM/DD/YYYY' string
SM.SetSeaState(1)                        # sea state 1–8, affects sonar
SM.SetSVP('depth,speed,depth,speed,...') # sound velocity profile CSV pairs (depth_m, speed_mps)
SM.SetSonarTemplate(id)
```

### Alliances

```python
SM.CreateAlliance(id, name)                       # id is integer, e.g. 1, 2, 3
SM.AddAllianceCountry(id, country_name)           # associate country name with alliance
SM.SetAllianceDefaultCountry(id, country_name)   # set default country for alliance
SM.SetAlliancePlayable(id, bool)                  # whether player can select this side
SM.SetAllianceRelationship(a_id, b_id, rel)       # rel: 'Hostile', 'Neutral', 'Friendly'
SM.GetAllianceRelationship(a_id, b_id)            # returns int
SM.SetUserAlliance(id)                            # default player side

# ROE values: 0=WEAPONS_HOLD, 1=WEAPONS_TIGHT, 2=WEAPONS_FREE
SM.SetAllianceROE(id, roe)                        # same ROE for all target types
SM.SetAllianceROEByType(id, air, surface, sub, land)  # per-target-type ROE
```

### Unit Creation

```python
unit = SM.GetDefaultUnit()    # returns a ScenarioUnit with default values
unit.className = 'SSN 688 Los Angeles Improved'  # must match database entry
unit.unitName  = 'USS Albany'                    # unique name within scenario
unit.SetPosition(lat_deg, lon_deg, alt_m)        # lat first; alt_m negative for underwater
unit.heading   = 90.0   # degrees true
unit.speed     = 5.0    # knots
unit.throttle  = 0.3    # throttle fraction 0-1 (aircraft only; ignored if < 0.3)
unit.cost      = 900000000.0  # used for scoring
SM.AddUnitToAlliance(unit, alliance_id)
```

`AddUnitToAlliance` automatically adds a permanent base AI task based on unit type:
- Air → `Aircraft1`
- Sub → `Submarine1`
- Surface ship → `Ship1`
- Airfield / ground / ground vehicle → `Ground1`

### Launcher and Magazine Setup

```python
# Set initial weapon loaded in a specific launcher slot
SM.SetUnitLauncherItem(unit_name, launcher_idx, item_class, quantity)
# quantity=0 clears the launcher

# Add items to the unit's magazine (reserve ammo)
SM.AddToUnitMagazine(unit_name, item_class, quantity)
```

Launcher indices are 0-based and correspond to the platform's database definition. Use `SetUnitLauncherItem` for pre-loaded tubes/rails and `AddToUnitMagazine` for reload stock.

#### Finding the right launcher index

```sql
-- What launchers does the platform have?
SELECT LauncherId, Description, Capacity
FROM platform_launcher
WHERE DatabaseClass = 'Typhoon'
ORDER BY LauncherId;

-- What is loaded by default?
SELECT ll.LauncherId, ll.Item, ll.Quantity
FROM launcher_loadout ll
JOIN platform_setup ps ON ll.DatabaseClass = ps.LauncherLoadout
WHERE ps.DatabaseClass = 'Typhoon'
ORDER BY ll.LauncherId;
```

`launcher_loadout.DatabaseClass` is a loadout config name (e.g. `'Typhoon-L'`), not the platform class. The link is via `platform_setup.LauncherLoadout`.

### Weapon Target Types (`targetFlags` bitmask)

| Value  | Target type  |
|--------|-------------|
| 0x0001 | Surface (ship) |
| 0x0002 | Air |
| 0x0004 | Land |
| 0x0008 | Missile |
| 0x0010 | Subsurface |

Always query before assigning a weapon to confirm it can hit the intended target type:

```python
python3 -c "
import sqlite3, os
conn = sqlite3.connect(os.path.expandvars(r'%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\Database\database.db'))
c = conn.cursor()
c.execute(\"SELECT DatabaseClass, targetFlags FROM missile WHERE DatabaseClass LIKE '%ASRAAM%'\")
for row in c.fetchall():
    f = row[1]
    targets = [n for mask,n in [(1,'Surface'),(2,'Air'),(4,'Land'),(8,'Missile'),(16,'Sub')] if f & mask]
    print(row[0], '->', targets)
conn.close()
"
```

**Common pitfalls:**
- ASRAAM, Sidewinder, MICA IR, Meteor — Air only (0x0002). Cannot engage ships.
- AM-39 Exocet, BAe Sea Eagle, Harpoon — Surface (0x0001). Anti-ship only.
- Some missiles carry multiple flags (e.g. MICA RF can be air + missile) — always verify.

### Unit Tasks

```python
# Add a named task to a unit's Brain
SM.AddUnitTask(unit_name, task_name, priority, attributes)
# attributes: 0=regular, 1=TEMPORARY, 2=HIDDEN, 3=PERMANENT|HIDDEN
```

### Flight Deck (Carriers and Airfields)

```python
# Add aircraft to a parent platform's flight deck
# loc_code: 1=HANGAR, 2=ALERT15, 3=ALERT5
SM.AddUnitToFlightDeck(parent_name, aircraft_class, aircraft_name, loc_code)

# Set pre-loaded stores on a flight deck aircraft
# loadout string format: "N ItemClass;N ItemClass;" — N is quantity
SM.SetFlightDeckUnitLoadout(parent_name, aircraft_name, '2 Kh-29T;4 R-77;30 Flare-1;')
```

### Visibility

```python
SM.SetUnitAlwaysVisibleState(unit_name, True)   # unit appears on all alliance sensor maps
```

### Goals

```python
# Create goals, then assign to alliance
SM.SetAllianceGoal(alliance_id, goal)

# DestroyGoal — passes when quantity targets are destroyed
g = SM.DestroyGoal('')
g.AddTarget('Unit Name')   # can call multiple times for multiple targets
g.SetQuantity(1)           # how many targets must be destroyed

# ProtectGoal — passes when quantity targets survive to scenario end
g = SM.ProtectGoal('')
g.AddTarget('Unit Name')
g.SetQuantity(1)

# TimeGoal — passes at pass_timeout, fails at fail_timeout (seconds from scenario start)
g = SM.TimeGoal()
g.SetPassTimeout(3600.0)       # 0.0 means never passes by time
g.SetFailTimeout(1000000.0)    # large number means never fails by time

# CompoundGoal — combines child goals with AND logic (type=0)
g = SM.CompoundGoal(0)
g.AddGoal(child_goal_1)
g.AddGoal(child_goal_2)
# compound passes when ALL children pass; fails when ANY child fails

# AreaGoal — passes/fails based on unit presence in geographic area
g = SM.AreaGoal()
```

### Randomization

```python
SM.SetIncludeProbability(unit_name, probability)  # 0.0–1.0
SM.IncludeUnit(probability)                       # returns True/False probabilistically
SM.AddRandomBox(unit_name, lat1_deg, lon1_deg, lat2_deg, lon2_deg)
# randomly positions unit within the box defined by two lat/lon corners on each scenario load

coord = SM.GetRandomDatum(lat_deg, lon_deg, min_alt_m, max_alt_m, rand_offset_deg)
# returns Coordinate object (coord.lon_deg, coord.lat_deg, coord.alt_m)
# rand_offset_deg: 1 deg ≈ 60 nmi

name = SM.GetRandomPlatformName(db_class, reference_name)
# returns a real-world name for db_class not already used, or reference_name+N
```

### Database Queries

```python
SM.SetFilterByYear(bool_state)               # enable/disable filtering platforms by scenario date
SM.GetFilterByYear()                         # returns bool
SM.SetFilterByCountry(bool_state)            # enable/disable filtering by active side's country
SM.GetFilterByCountry()                      # returns bool
platform_list = SM.GetPlatformListByClass(class_type)  # returns StringArray
results = SM.QueryDatabase(table, databaseClass, fields)  # returns StringTable
SM.LoadDatabaseMod(mod_file_path)
SM.RestoreDefaultDatabase()
```

### Scenario Edit / Scripting Utilities

```python
UI = SM.GetUnitInterface(unit_name)    # returns PlatformInterface (see below)
id = SM.GetUnitIdByName(unit_name)     # returns long, -1 if not found
name = SM.GetUnitNameById(id)          # returns string
SM.DuplicateUnitTasking(unit_name_1, unit_name_2)  # copy waypoints/tasks to unit 2
SM.SaveGame(file_path)                 # saves current state to .py file
SM.SetPerfectScore(score)
SM.AllianceExists(alliance_id)         # returns bool

# Air group helpers (used by scenario edit tools)
SM.SetAirGroupName(name)
SM.GetAirGroupName()
SM.GetAirUnitId()
SM.SetAirGroupCount(n)
SM.SetMagazineAddCount(n)
```

### Map and Briefing Events

```python
SM.ConsoleText(text)
SM.ChannelMessage(message, channel, alliance)
SM.MapText(text, lat_deg, lon_deg, duration, effect)
SM.ClearEvents()
SM.HookPlatform(unit_name)
SM.Pause()
SM.Resume()
SM.Set3DMode(mode_code)
SM.SetBriefingMode(bool)
SM.SetEventTime(t)
SM.PlayAudio(audio_name, seek_time)
SM.PlayEffect(effect_name)
SM.PauseAudio()
SM.SeekAudio(seek_time)
SM.SendCommand(command_string)
```

---

## PlatformInterface (UI)

Obtained via `UI = SM.GetUnitInterface(unit_name)` or within task scripts via `self`.

### Navigation

```python
UI.GetLongitude()          # degrees
UI.GetLatitude()           # degrees
UI.GetAltitude()           # meters (negative underground/underwater)
UI.GetSpeed()              # knots
UI.GetHeading()            # degrees true
UI.GetThrottle()           # fraction 0–1
UI.SetSpeed(kts)
UI.SetAltitude(m)
UI.SetHeading(deg)
UI.SetThrottle(fraction)
UI.SetSpeedToMax()
UI.HasThrottle()
UI.GetMaxSpeed()
UI.GetMaxAltitude()
UI.GetCruiseAltitude()
UI.GetTerrainElevation(lat_deg, lon_deg)   # meters MSL
```

### Waypoints

Waypoints are processed in order. The Nav task must be added for waypoints to have effect.

```python
# add_waypoint_advanced is the primary form used in saved scenarios
UI.add_waypoint_advanced(lat_deg, lon_deg, alt_m, speed_kts)
# alt_m=0 and speed_kts=0 use default altitude/speed

UI.add_waypoint(lat_deg, lon_deg)          # simplified, no alt/speed
UI.clear_waypoints()
UI.DeleteNavWaypoint(index)
UI.InsertNavWaypoint(index, lat_deg, lon_deg)
UI.SetNavLoopState(True)                   # loop back to first waypoint when done
UI.SetNavWaypointTasks(index, 'task1,task2')  # tasks to run at waypoint
UI.SetCurrentWaypoint(index)
UI.current_waypoint()                      # returns Coordinate
```

### Tasks

Tasks run in parallel; priority controls which task "wins" when conflicts arise (higher priority wins). Attributes control persistence.

```python
# attributes: 0=regular, 1=TEMPORARY, 2=HIDDEN, 3=PERMANENT|HIDDEN
UI.AddTask(task_name, priority=1.0, attributes=0)
UI.ClearTasks()
UI.DeleteTask(task_name)
UI.TaskExists(task_name)    # returns bool
UI.task_list()              # returns StringArray of current task names
UI.SetTaskRun(task_name, bool)
```

**Built-in task names:**

| Task Name | Description |
|---|---|
| `Nav` | Follow waypoints |
| `Loiter` | Stay at current position |
| `AutoAttack` | Automatically engage detected targets |
| `PointDefense` | Fire defensive weapons against inbound missiles |
| `Aircraft1` | Base aircraft behavior (low fuel → land/refuel) |
| `AirEvade` | Evade inbound missiles, deploy countermeasures |
| `AirRefuel` | Air-to-air refueling |
| `LandFixedWing` | Fixed-wing landing approach |
| `LandHelicopter` | Helicopter landing approach |
| `Ship1` | Base ship behavior |
| `ShipDefense` | Ship defensive behaviors |
| `Submarine1` | Base submarine behavior (cavitation avoidance) |
| `SubmarineEvade` | Sub evasion maneuvers |
| `Ground1` | Base ground unit behavior |
| `GroundDefense` | Ground unit defensive behaviors |
| `ASWPatrol` | ASW patrol behavior |

### Sensors

```python
UI.GetSensorCount()
UI.SetSensorState(index, 1)     # 1=on, 0=off
UI.GetSensorState(index)
UI.SetAllSensorState(1)
UI.GetSensorInfo(index)         # returns SensorInfo (.isActive, .type, .IsPassive())
```

### Tracks (Sensor Picture)

```python
UI.GetFirstTrack()                    # returns TrackIterator
UI.GetClosestAirTrack()               # returns TrackIterator
UI.GetClosestSurfaceTrack()
UI.GetClosestMissileTrack()
UI.GetClosestInboundMissileTrack()
UI.GetClosestTrack()
UI.GetTrackList()                     # returns TrackList of all contacts
UI.GetFriendlyTrackList()
UI.GetTrackById(id)                   # returns Track/tcSensorMapTrack
```

**Track fields:** `.lat_deg`, `.lon_deg`, `.alt_m`, `.Speed`, `.Heading_rad`, `.ID`, `.Classification`, `.Affiliation`

**Track methods:** `.IsAir()`, `.IsSurface()`, `.IsSub()`, `.IsMissile()`, `.IsTorpedo()`, `.IsGround()`, `.IsBearingOnly()`, `.IsValid()`, `.IsDestroyed()`, `.IsInbound()`, `.RangeToKm(lat_deg, lon_deg)`, `.BearingToRad(lat_deg, lon_deg)`, `.PredictAhead(seconds)`

### Weapons

```python
UI.GetTarget()                        # returns target track ID
UI.SetTarget(track_id)
UI.GetLauncherCount()
UI.GetLauncherInfo(index)             # returns LauncherInfo
UI.GetBestLauncher(track_id)          # returns LauncherInfo for best weapon vs target
UI.IsTargetInRange(track_id)
UI.Launch(launcher_idx, track_id)
UI.GetLauncherQuantity(launcher_idx)
UI.GetMagazineQuantity(item_class)
UI.AddItemToMagazine(item_class, quantity)
UI.LoadLauncher(launcher_idx, item_class)
UI.UnloadLauncher(launcher_idx)
```

**LauncherInfo fields:** `.index`, `.quantity`, `.range_km`, `.min_range_km`, `.max_range_km`, `.target_flags` (1=surface, 2=air, 4=land), `.IsValid()`, `.GetChildClass()`

### Formation

```python
UI.SetFormationLeader(leader_id)
UI.SetFormationMode(mode)             # 1=loose, 2=tight
UI.SetFormationPosition(range_km, span_km, bearing_rad, span_rad)
UI.SetFormationAltitudeOffset(m)
UI.SetFormationUseNorthBearing(bool)
UI.IsInFormation()
UI.IsFormationLeader()
UI.GetFormationLeader()               # returns id
```

### Type Checks

```python
UI.IsAir()
UI.IsSurface()
UI.IsSub()
UI.IsGround()
UI.IsHelo()
UI.IsFixed()            # fixed-wing aircraft
UI.IsGroundVehicle()
UI.IsValid()            # false if unit not found or destroyed
```

### Submarine Interface

```python
sub = UI.GetSubInterface()
sub.GetMaxDepth()
sub.IsDieselElectric()
sub.IsSnorkeling()
sub.SetSnorkelState(bool)
sub.GoToPeriscopeDepth()
sub.IsAtPeriscopeDepth()
sub.IsPeriscopeRaised()
sub.RaisePeriscope()
sub.LowerPeriscope()
sub.RaiseRadarMast()
sub.LowerRadarMast()
sub.GetCavitatingSpeed(depth_m)       # max quiet speed at given depth
sub.GetBatteryFraction()
```

### Flight Ops (Carriers and Airfields)

```python
FP = UI.GetFlightOpsInfo()            # returns FlightPortInterface (see below)
UI.HasFlightOps()                     # check before calling GetFlightOpsInfo()
```

### Blackboard

Inter-task shared state keyed by string.

```python
BB = UI.GetBlackboardInterface()
BB.Write(key, value_string)
BB.WriteGlobal(key, value_string)     # visible to all tasks on platform
BB.Read(key)                          # returns value string, '' if missing
BB.KeyExists(key)
BB.Erase(key)
BB.ReadAuthor(key)                    # task id that wrote this key
BB.ReadPriority(key)                  # priority of writing task
```

### Miscellaneous

```python
UI.GetPlatformId()
UI.GetPlatformName()
UI.GetPlatformClass()
UI.GetPlatformAlliance()
UI.GetTime()                          # scenario time in seconds
UI.LookupFriendlyId(unit_name)        # returns id of friendly unit by name
UI.LookupFriendlyName(id)             # returns name of friendly unit by id
UI.GetROE()                           # returns ROE mode int for this alliance
UI.SetAlwaysVisible(bool)
UI.SetFuelFraction(0.0–1.0)
UI.GetFuelCapacity()
UI.GetCost()
UI.SetCost(value)
UI.DisplayMessage(text)
UI.SendCommand(command_string)
UI.GetRangeToPoint(lat_deg, lon_deg)  # km
UI.GetHeadingToPoint(lat_deg, lon_deg)  # degrees true
UI.user_idle_time()                   # seconds since player last interacted
```

---

## FlightPortInterface (FP)

Obtained via `FP = UI.GetFlightOpsInfo()`.

### Mission Management

```python
mission_id = FP.AddGroupedMission()
FP.AddAircraftToMission(mission_id, aircraft_name)

# Mission types: 'ASW-Patrol', 'Strike', 'CAP', 'AEW'
FP.SetMissionType(mission_id, type_string)

# Launch time: 'HH:MM:SS+Nm' where N is minutes offset from scenario start
FP.SetMissionLaunchTime(mission_id, '03:19:00+0m')

FP.SetMissionDatum(mission_id, lat_deg, lon_deg)   # 0,0 for no fixed datum
FP.SetMissionLandingTarget(mission_id, unit_name)  # '' for home base
FP.SetMissionSorties(mission_id, n)                # 0 = unlimited

# Target flags: 1=surface, 2=air, 4=land, 8=sub
FP.SetMissionTargetFlags(mission_id, flags)

# Patrol area as comma-separated lat_deg,lon_deg vertex pairs (degrees)
FP.SetMissionPatrolAreaDeg(mission_id, '28.38,-78.14,...,')
FP.SetMissionPatrolAnchor(mission_id, unit_name, mode)   # anchor patrol to moving platform
```

### Simple Auto-Missions

These create a one-waypoint mission for a single aircraft type. Call on FP of the parent ship/airfield.

```python
FP.AddCAPMission(lat_deg, lon_deg)    # CAP patrol point
FP.AddAEWMission(lat_deg, lon_deg)    # AEW patrol point
FP.AddASWMission(lat_deg, lon_deg)    # ASW patrol point
FP.AddAttackMission(target_id)        # attack specific target
```

### Mission Waypoints

All mission waypoint coordinates use **(lat_deg, lon_deg)** — latitude first, in degrees.

```python
FP.AddMissionWaypoint(mission_id, lat_deg, lon_deg)
FP.AddMissionWaypointAdvanced(mission_id, lat_deg, lon_deg, alt_m, speed_kts)
FP.EditMissionWaypoint(mission_id, idx, lat_deg, lon_deg)
FP.EditMissionWaypointAdvanced(mission_id, idx, lat_deg, lon_deg, alt_m, speed_kts)
FP.InsertMissionWaypoint(mission_id, idx, lat_deg, lon_deg)
FP.DeleteMissionWaypoint(mission_id, idx)
FP.ClearMissionWaypoints(mission_id)
FP.GetMissionWaypointCount(mission_id)
FP.SetMissionWaypointTasks(mission_id, wp_index, 'task1,task2')
FP.AddMissionWaypointTask(mission_id, wp_index, task)
FP.RemoveMissionWaypointTask(mission_id, wp_index, task)
```

**Waypoint task strings:** `'WaitForGroup'`, `'ASWPatrol,EngageAll'`, `'GroundStrike'`, `'Land'`

### Mission Grouping

```python
# group_id: arbitrary integer for grouping (use large random int or platform ID)
# aircraft_list: comma-separated names, e.g. 'Fish 1,Fish 2'
# count: aircraft active per sortie
FP.SetMissionGroup(mission_id, group_id, aircraft_list_str, count)
FP.SetAllGroupActiveQuantity(mission_id, quantity)
```

### Direct Launch

```python
FP.Launch(runway_number)           # launch aircraft on specified runway
FP.LaunchID(aircraft_id)           # launch specific aircraft by ID
FP.SetDestination(unit_index, dest_code)  # dest_code: 0=hangar, 1=ready, 2=runway/launch
FP.GetUnitCount()
FP.GetUnitName(index)
FP.GetUnitID(index)
FP.GetUnitStatus(index)            # returns FlightUnitStatus
FP.GetUnitLocation(index)
FP.GetUnitGoalLocation(index)
FP.GetUnitPlatformInterface(index) # returns PlatformInterface for that aircraft
```

---

## ScriptedTask (Unit Behavior Scripts)

Task scripts live in `scripts/tasks/` and are loaded at startup by `scripts/unit_tasks.py`. Each task class must be registered in `unit_tasks.py`'s `module_list`.

```python
from platform_interface import ScriptedTask

class MyTask(ScriptedTask):
    def __init__(self):
        ScriptedTask.__init__(self)

    def start(self):
        # called once when task is added to a platform
        self.SetUpdateInterval(30.0)   # call update() every 30 sim-seconds

    def update(self):
        # called at SetUpdateInterval rate
        pass
```

`ScriptedTask` inherits all `PlatformInterface` methods, so `self.GetSpeed()`, `self.AddTask(...)`, etc. are available directly.

### Task Lifecycle

```python
self.SetUpdateInterval(seconds)
self.EndTask()               # remove this task from the platform
self.SetTaskAttributes(attrs)  # change attributes (see AddTask flags)
```

### Named Locks (for exclusive behavior)

Locks prevent two tasks from issuing conflicting commands simultaneously.

```python
if self.AcquireLock('connection'):   # returns True if lock was free
    self.SetSpeed(20.0)
    self.ReleaseLock('connection')

self.IsLocked('connection')          # True if any task holds this lock
self.GetLockOwner('connection')      # task name that holds it
```

### Blackboard (within tasks)

Same API as `UI.GetBlackboardInterface()` but accessed directly:

```python
self.Write(key, value)
self.WriteGlobal(key, value)
self.Read(key)
self.KeyExists(key)
self.Erase(key)
```

---

## Coordinate Object

Returned by `SM.GetRandomDatum()` and `UI.current_waypoint()`.

```python
coord.lat_deg
coord.lon_deg
coord.alt_m
coord.valid         # bool
coord.RangeTo(other_coord)   # km
```

---

## Coordinate Convention

- All Python scenario interface methods use **(lat_deg, lon_deg)** — latitude first, in degrees. This applies to `unit.SetPosition`, `add_waypoint_advanced`, `SM.GetRandomDatum`, `SM.AddRandomBox`, `FP.SetMissionPatrolAreaDeg`, and all other coordinate-taking methods.
- **`FP.SetMissionPatrolArea`** (legacy) takes `lon_rad,lat_rad` pairs — do not use in new scenarios; use `FP.SetMissionPatrolAreaDeg` instead.
- Negative altitude = underwater (submarines) or below ground. Use terrain elevation to place ground units correctly.
- `unit.className` must exactly match the `DatabaseClass` field in `database/database.db`.
- Unit names must be unique within a scenario.
- All code runs inside the `blue` namespace Python interpreter. Standard Python libraries (`math`, `random`) are available.

---

## Checklist Before Saving

- [ ] All `SetPosition` calls use `(lat_deg, lon_deg, alt_m)` order
- [ ] Version header `# Scenario version: 0.2.1` is present
- [ ] At least one goal is set per alliance (or at least one global goal)
- [ ] Anti-ship weapons verified with `targetFlags & 0x0001`
- [ ] Air-to-air missiles not assigned to ship launchers
- [ ] `SetUserAlliance` called once
- [ ] All `DatabaseClass` strings verified against `platform_setup.DatabaseClass`
- [ ] All weapon/item strings verified against the `item` table
