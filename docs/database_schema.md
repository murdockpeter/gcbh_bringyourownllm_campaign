# Database Schema

GCBlue simulation engine database. Uses SQLite.
Schema version: 2 (stored in `version` table).
Default location for player database is `%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\Database\database.db`

To connect from Python, use `os.path.expandvars` to resolve the environment variable:
```python
import sqlite3, os
conn = sqlite3.connect(os.path.expandvars(r'%USERPROFILE%\AppData\LocalLow\Wardstone Games\GCB Horizon\Database\database.db'))
```
---

## Key Relationships

```
platform (air / simpleair / ship / sub / ground)
  ├─ platform_launcher  ──→  launcher_configuration  (what each launcher can carry)
  │     LauncherId (0-based index used by SetUnitLauncherItem)
  ├─ platform_magazine  ──→  stores  (magazine/storage classes)
  └─ platform_setup  (named loadout configs, filtered by year)
        ├─ LauncherLoadout  ──→  launcher_loadout.DatabaseClass  (default items per launcher)
        ├─ MagazineLoadout  ──→  magazine_loadout.DatabaseClass  (default items per magazine)
        └─ AirComplement   ──→  air_complement.DatabaseClass    (embarked aircraft)
```

**Loadout query pattern** — given a platform class and year, find its default weapons:
```sql
-- Step 1: find applicable setup
SELECT * FROM platform_setup
WHERE DatabaseClass = 'F-16C' AND InitialYear <= 1995 AND FinalYear >= 1995;

-- Step 2: get launcher defaults (LauncherLoadout value from above)
SELECT pl.LauncherId, pl.Description, ll.Item, ll.Quantity
FROM platform_launcher pl
LEFT JOIN launcher_loadout ll
  ON ll.DatabaseClass = 'F-16C Block 50 (1991)-L' AND ll.LauncherId = pl.LauncherId
WHERE pl.DatabaseClass = 'F-16C'
ORDER BY pl.LauncherId;

-- Step 3: see what else each launcher can carry
SELECT lc.*
FROM platform_launcher pl
JOIN launcher_configuration lc ON lc.DatabaseClass = pl.LauncherClass
WHERE pl.DatabaseClass = 'F-16C' AND pl.LauncherId = 1;
```

---

## Version

| Column | Type | Description |
|--------|------|-------------|
| Attribute | TEXT | Attribute name |
| Value | NUMERIC | Attribute value (Version=2 for current schema) |

---

## Platform Tables

### air

High-performance fixed-wing jet aircraft.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name (used as foreign key everywhere) |
| DisplayClass | TEXT | User-facing name (may differ from DatabaseClass) |
| ModelClassId | INTEGER | 3D model category — see enum at bottom |
| ClassificationId | INTEGER | Sensor/IFF classification — see enum at bottom |
| Weight_kg | NUMERIC | Empty weight |
| Volume_m3 | numeric | Physical volume |
| ObjectBounds | TEXT | Bounding box string |
| InitialYear | NUMERIC | Year introduced |
| FinalYear | NUMERIC | Year retired (2999 = indefinite) |
| Country | TEXT | Operator nation |
| Subtype | TEXT | Platform subtype string |
| Author | TEXT | Database entry author |
| Description | TEXT | Free-text description |
| Notes | TEXT | Additional notes |
| Sources | TEXT | Reference sources |
| MaxSpeed_kts | numeric | Maximum level flight speed |
| Accel_ktsps | numeric | Acceleration rate (kts/s) |
| TurnRate_degps | numeric | Maximum sustained turn rate |
| FuelCapacity_kg | numeric | Internal fuel capacity |
| FuelRate_kgps | numeric | Fuel burn rate at cruise |
| Toughness | numeric | Structural hit points |
| DamageEffect | TEXT | References damage_effect.DatabaseClass |
| AirSignatureModel | TEXT | References radiation_pattern or air_signature |
| RCS_dBsm | REAL | Radar cross-section |
| OpticalCrossSection_dBsm | REAL | Optical signature |
| IRSignatureMW_dB | REAL | IR signature (medium wave) |
| IRSignatureLW_dB | REAL | IR signature (long wave) |
| EffectiveHeight_m | REAL | Height used for terrain masking |
| TS | numeric | Target strength (acoustic) |
| TS_Model | TEXT | Acoustic target strength model |
| AcousticModel | TEXT | Acoustic noise model reference |
| SL_Model | TEXT | Source level model |
| MaxTakeoffWeight_kg | numeric | Maximum takeoff weight |
| MaxAltitude_m | numeric | Service ceiling |
| ClimbRate_mps | numeric | Maximum climb rate |
| Gmax | numeric | Maximum g-load |
| MinimumRunway_m | numeric | Minimum runway length required |
| IsCarrierCompatible | numeric | 1 if can operate from carriers |
| OutFuelPods | numeric | 1 if can transfer fuel to other aircraft |
| FuelOut_kgps | numeric | Fuel transfer rate (tanker) |
| FuelIn_kgps | numeric | Fuel receive rate (receiver) |
| MaintenanceMin_s | numeric | Minimum turnaround time |
| MaintenanceMax_s | numeric | Maximum turnaround time |
| EngineModel | TEXT | References air_engine.DatabaseClass |
| NumEngines | INTEGER | Number of engines |
| Cdpsub | numeric | Subsonic drag coefficient |
| Cdptran | numeric | Transonic drag coefficient |
| Cdpsup | NUMERIC | Supersonic drag coefficient |
| Mcm | numeric | Critical Mach number |
| Msupm | numeric | Supersonic Mach number |
| WingArea_m2 | REAL | Wing reference area |
| Wingspan_m | REAL | Wingspan |
| WingEfficiency | REAL | Oswald efficiency factor |
| MaxCL | REAL | Maximum lift coefficient |

### simpleair

Slower aircraft — helicopters and propeller-driven fixed-wing. Shares most columns with `air` but omits the advanced aerodynamic model.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name |
| DisplayClass | TEXT | User-facing name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | numeric | Empty weight |
| Volume_m3 | numeric | Physical volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Year introduced |
| FinalYear | numeric | Year retired |
| Country | TEXT | Operator nation |
| Subtype | TEXT | Platform subtype |
| Author | TEXT | Entry author |
| Description | TEXT | Description |
| Notes | TEXT | Notes |
| Sources | TEXT | Sources |
| MaxSpeed_kts | NUMERIC | Maximum speed |
| Accel_ktsps | numeric | Acceleration |
| TurnRate_degps | numeric | Turn rate |
| FuelCapacity_kg | numeric | Fuel capacity |
| FuelRate_kgps | REAL | Fuel burn rate |
| Toughness | numeric | Hit points |
| DamageEffect | REAL | References damage_effect |
| AirSignatureModel | TEXT | Signature model |
| RCS_dBsm | REAL | Radar cross-section |
| OpticalCrossSection_dBsm | REAL | Optical signature |
| IRSignatureMW_dB | REAL | IR signature MW |
| IRSignatureLW_dB | REAL | IR signature LW |
| EffectiveHeight_m | numeric | Terrain masking height |
| TS | numeric | Acoustic target strength |
| TS_Model | TEXT | Acoustic model |
| AcousticModel | TEXT | Noise model |
| SL_Model | TEXT | Source level model |
| MaxTakeoffWeight_kg | numeric | Max takeoff weight |
| MaxAltitude_m | numeric | Service ceiling |
| ClimbRate_mps | numeric | Climb rate |
| Gmax | numeric | Max g-load |
| MinimumRunway_m | numeric | Min runway (0 for helos) |
| IsCarrierCompatible | INTEGER | 1 if carrier-capable |
| OutFuelPods | INTEGER | 1 if tanker-capable |
| FuelOut_kgps | REAL | Fuel transfer rate |
| FuelIn_kgps | REAL | Fuel receive rate |
| MaintenanceMin_s | REAL | Min turnaround |
| MaintenanceMax_s | REAL | Max turnaround |

### ship

Surface combatants and vessels.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name |
| DisplayClass | TEXT | User-facing name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | numeric | Displacement (kg) |
| Volume_m3 | NUMERIC | Volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Commissioned year |
| FinalYear | numeric | Decommissioned year |
| Country | TEXT | Operator |
| Subtype | TEXT | Ship subtype |
| Author | TEXT | Entry author |
| Description | TEXT | Description |
| Notes | TEXT | Notes |
| Sources | TEXT | Sources |
| MaxSpeed_kts | numeric | Flank speed |
| Accel_ktsps | numeric | Acceleration |
| TurnRate_degps | numeric | Turn rate |
| FuelCapacity_kg | numeric | Fuel capacity |
| FuelRate_kgps | REAL | Fuel consumption |
| Toughness | numeric | Hit points |
| DamageEffect | TEXT | References damage_effect |
| Draft_m | REAL | Draft (for shallow water) |
| Length_m | REAL | Length overall |
| Beam_m | REAL | Beam |
| PowerType | TEXT | Propulsion type string |
| TotalPropulsion_kW | REAL | Total installed power |
| FlightportClass | TEXT | References flightport (if carrier/helo deck) |
| AirSignatureModel | TEXT | Signature model |
| RCS_dBsm | REAL | Radar cross-section |
| OpticalCrossSection_dBsm | REAL | Optical signature |
| IRSignatureMW_dB | REAL | IR signature MW |
| IRSignatureLW_dB | REAL | IR signature LW |
| EffectiveHeight_m | REAL | Mast height for detection |
| TS | numeric | Acoustic target strength |
| TS_Model | TEXT | Acoustic model |
| AcousticModel | TEXT | Noise model |
| SL_Model | TEXT | Source level model |

### sub

Submarines.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name |
| DisplayClass | TEXT | User-facing name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | numeric | Displacement |
| Volume_m3 | numeric | Volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Year introduced |
| FinalYear | numeric | Year retired |
| Country | TEXT | Operator |
| Subtype | TEXT | Subtype |
| Author | TEXT | Entry author |
| Description | TEXT | Description |
| Notes | TEXT | Notes |
| Sources | TEXT | Sources |
| MaxSpeed_kts | numeric | Submerged max speed |
| Accel_ktsps | numeric | Acceleration |
| TurnRate_degps | numeric | Turn rate |
| FuelCapacity_kg | numeric | Fuel/reactor energy |
| FuelRate_kgps | REAL | Fuel rate (diesel) |
| Toughness | numeric | Hit points |
| DamageEffect | TEXT | References damage_effect |
| Draft_m | REAL | Draft |
| SurfaceSpeed_kts | REAL | Surface speed (less than submerged for SSN) |
| AirSignatureModel | TEXT | Signature model |
| RCS_dBsm | REAL | Surfaced RCS |
| OpticalCrossSection_dBsm | REAL | Optical signature |
| IRSignatureMW_dB | REAL | IR signature MW |
| IRSignatureLW_dB | REAL | IR signature LW |
| EffectiveHeight_m | REAL | Surfaced height |
| TS | numeric | Acoustic target strength |
| TS_Model | TEXT | Acoustic model |
| AcousticModel | TEXT | Noise model |
| SL_Model | TEXT | Source level model |
| MaxDepth_m | numeric | Crush depth |
| IsDieselElectric | INTEGER | 1 for SSK, 0 for SSN |
| BatteryCapacity_kJ | numeric | Battery capacity (SSK) |
| BatteryRate_kW | REAL | Battery drain rate |
| BatteryCharge_kW | REAL | Battery charge rate (snorkeling) |

### ground

Ground-based systems: air defense, radars, vehicles.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name |
| DisplayClass | TEXT | User-facing name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | numeric | Weight |
| Volume_m3 | numeric | Volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Year introduced |
| FinalYear | numeric | Year retired |
| Country | TEXT | Operator |
| Subtype | TEXT | Subtype |
| Author | TEXT | Entry author |
| Description | TEXT | Description |
| Notes | TEXT | Notes |
| Sources | TEXT | Sources |
| MaxSpeed_kts | NUMERIC | Speed (vehicles) |
| Accel_ktsps | numeric | Acceleration |
| TurnRate_degps | numeric | Turn rate |
| FuelCapacity_kg | numeric | Fuel capacity |
| FuelRate_kgps | numeric | Fuel rate |
| Toughness | numeric | Hit points |
| DamageEffect | TEXT | References damage_effect |
| FlightportClass | TEXT | References flightport (airfields) |
| AirSignatureModel | TEXT | Signature model |
| RCS_dBsm | REAL | Radar cross-section |
| OpticalCrossSection_dBsm | REAL | Optical signature |
| IRSignatureMW_dB | REAL | IR signature MW |
| IRSignatureLW_dB | REAL | IR signature LW |
| EffectiveHeight_m | REAL | Height |

---

## Launcher & Loadout Tables

These are the key tables for scenario generation. See the relationship diagram at the top.

### platform_launcher

Maps launchers to platforms. One row per launcher per platform. **`LauncherId` is the 0-based index used by `SM.SetUnitLauncherItem(unitName, LauncherId, item, qty)`.**

**Primary Key:** (none — composite DatabaseClass + LauncherId)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Platform class name |
| LauncherClass | TEXT | Launcher type — references launcher_configuration.DatabaseClass |
| LauncherId | numeric | 0-based launcher index on this platform |
| Description | TEXT | Human-readable label (e.g., "Torpedo tube 1", "VLS cell") |
| LocalName | TEXT | Platform-specific launcher name prefix |
| FiringArc_deg | numeric | Field of fire in degrees |
| Az | numeric | Azimuth mounting angle (deg) |
| El | numeric | Elevation mounting angle (deg) |
| FireControlSensor | TEXT | Primary FCS sensor class |
| FireControlSensor2 | TEXT | Secondary FCS sensor class (optional) |
| IsReloadable | numeric | 1 = can reload from magazine; 0 = expendable |
| x | NUMERIC | Position offset right of platform center (m) |
| y | NUMERIC | Position offset forward of platform center (m) |
| z | NUMERIC | Position offset up from platform center (m) |

### launcher_configuration

Defines what each launcher type can carry. A launcher may accept multiple weapon classes (one row per compatible item).

**Primary Key:** (none — composite DatabaseClass + ChildClass)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Launcher type name (matches platform_launcher.LauncherClass) |
| ChildClass | TEXT | Compatible weapon/item class name |
| EquipmentGroup | TEXT | If set, expands to all members of this equipment_group instead of a fixed class |
| ChildCapacity | numeric | Maximum quantity this launcher can hold |
| LoadTime_s | numeric | Time to load one unit (seconds) |
| CycleTime_s | numeric | Firing cycle time / rate of fire (seconds) |

### launcher_loadout

Default weapon assignments per launcher for a named loadout configuration. `DatabaseClass` here is the loadout config name (e.g., `"F-16C Block 50 (1991)-L"`), **not** the platform class — it is referenced by `platform_setup.LauncherLoadout`.

**Primary Key:** (none — composite DatabaseClass + LauncherId)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Loadout configuration name (referenced by platform_setup.LauncherLoadout) |
| LauncherId | numeric | Launcher index (matches platform_launcher.LauncherId) |
| Item | TEXT | Default weapon class for this launcher (NULL = empty) |
| Quantity | numeric | Default quantity |

### platform_magazine

Maps magazine/storage classes to platforms. One row per magazine per platform.

**Primary Key:** (none — composite DatabaseClass + MagazineId)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Platform class name |
| MagazineClass | TEXT | Storage type — references stores.DatabaseClass |
| MagazineId | numeric | 0-based magazine index on this platform |

### magazine_loadout

Default contents for each magazine in a named loadout configuration. `DatabaseClass` is the loadout config name referenced by `platform_setup.MagazineLoadout`.

**Primary Key:** (none)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Loadout configuration name (referenced by platform_setup.MagazineLoadout) |
| MagazineId | numeric | Magazine index (matches platform_magazine.MagazineId) |
| Item | TEXT | Default item class (may reference equipment_group for flexible selection) |
| Quantity | numeric | Default quantity |

### platform_setup

Named loadout configurations for a platform, typically filtered by year. Links a platform to its launcher loadout, magazine loadout, and air complement config.

**Primary Key:** (none — composite DatabaseClass + SetupName)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Platform class name |
| SetupName | TEXT | Configuration name (e.g., "F-16C Block 50 (1991)") |
| InitialYear | numeric | First year this setup is available |
| FinalYear | numeric | Last year available (2999 = indefinite) |
| AirComplement | TEXT | air_complement config name (empty if no embarked aircraft) |
| MagazineLoadout | TEXT | magazine_loadout config name (empty if no magazine defaults) |
| LauncherLoadout | TEXT | launcher_loadout config name (empty if no launcher defaults) |

**Convention:** loadout config names typically follow the pattern `"<SetupName>-A"` (air), `"<SetupName>-M"` (magazine), `"<SetupName>-L"` (launcher).

### air_complement

Embarked aircraft assignments for a named air complement configuration. Referenced by `platform_setup.AirComplement`.

**Primary Key:** (none)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Air complement config name |
| AirClass | TEXT | Aircraft class (from air or simpleair table) |
| Quantity | numeric | Number of this aircraft type |
| Prefix | TEXT | Name prefix for generated aircraft instances |
| ReadyLevel | numeric | Initial readiness (1 = ready) |

### equipment_group

Groups weapon/item classes under a single name for flexible launcher configuration. When `launcher_configuration.EquipmentGroup` is set, the launcher accepts any item in this group.

**Primary Key:** (none)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Group name (referenced by launcher_configuration.EquipmentGroup) |
| EquipmentClass | TEXT | Member item class name |

---

## Weapon Tables

### missile

Guided air/surface/anti-ship/SAM missiles.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name |
| DisplayClass | TEXT | User-facing name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | numeric | Launch weight |
| Volume_m3 | numeric | Volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Year introduced |
| FinalYear | numeric | Year retired |
| Country | TEXT | Origin country |
| Subtype | TEXT | Subtype |
| Author | TEXT | Entry author |
| Description | TEXT | Description |
| Notes | TEXT | Notes |
| Sources | TEXT | Sources |
| Damage | numeric | Warhead damage value |
| DamageModel | TEXT | Damage calculation model |
| LaunchSpeed_mps | numeric | Speed at launch |
| targetFlags | numeric | Bitmask — see targetFlags enum |
| MinLaunchAlt_m | numeric | Minimum launch altitude |
| MaxLaunchAlt_m | numeric | Maximum launch altitude |
| MinRange_km | numeric | Minimum range |
| MaxRange_km | numeric | Maximum range |
| ProbNoFaults | numeric | Reliability (0–1) |
| PayloadClass | TEXT | Submunition class (if separating warhead) |
| PayloadQuantity | numeric | Submunition count |
| DatalinkRange_km | REAL | Datalink range for mid-course guidance |
| AcceptsUserCommands | numeric | 1 if player can retarget in flight |
| DetonationRange_m | numeric | Proximity fuze radius |
| NavigationError_m | NUMERIC | CEP for terminal guidance |
| AirSignatureModel | TEXT | Radar signature model |
| RCS_dBsm | REAL | Missile RCS |
| OpticalCrossSection_dBsm | REAL | Optical signature |
| IRSignatureMW_dB | REAL | IR signature MW |
| IRSignatureLW_dB | REAL | IR signature LW |
| EffectiveHeight_m | REAL | Effective height |
| DragArea_sm | numeric | Reference drag area |
| Gmax | numeric | Maximum maneuver g-load |
| MaxTurnRate_degps | numeric | Maximum seeker/body turn rate |
| Cdpsub | numeric | Subsonic drag |
| Cdptran | numeric | Transonic drag |
| Cdpsup | numeric | Supersonic drag |
| Mcm | numeric | Critical Mach |
| Msupm | numeric | Supersonic Mach |
| BoostThrust_N | numeric | Boost motor thrust |
| BoostTime_s | numeric | Boost duration |
| SustThrust_N | numeric | Sustain motor thrust |
| SustTime_s | numeric | Sustain duration |
| ShutdownSpeed_mps | numeric | Speed below which motor shuts down |
| SensorClass | TEXT | Seeker class reference |
| NeedsFireControl | numeric | 1 = requires FCS lock before launch |
| AcceptsWaypoints | numeric | 1 = can be given flight path waypoints |
| Rng1_km–Rng8_km | numeric | Waypoint range thresholds |
| Alt1_m–Alt8_m | numeric | Waypoint altitudes |
| AltMode1–AltMode8 | numeric | Altitude mode at waypoint |
| GuidMode1–GuidMode8 | numeric | Guidance mode at waypoint |
| DamageEffect | TEXT | References damage_effect |

### torpedo

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name |
| DisplayClass | TEXT | User-facing name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | numeric | Weight |
| Volume_m3 | numeric | Volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Year introduced |
| FinalYear | numeric | Year retired |
| Country | TEXT | Origin |
| Subtype | TEXT | Subtype |
| Author | TEXT | Entry author |
| Description | TEXT | Description |
| Notes | TEXT | Notes |
| Sources | TEXT | Sources |
| Damage | numeric | Warhead damage |
| DamageModel | TEXT | Damage model |
| DamageEffect | TEXT | References damage_effect |
| LaunchSpeed_mps | numeric | Launch speed |
| targetFlags | numeric | Target type bitmask |
| MinLaunchAlt_m | numeric | Min depth at launch |
| MaxLaunchAlt_m | numeric | Max depth at launch |
| MinRange_km | numeric | Min range |
| MaxRange_km | numeric | Max range |
| ProbNoFaults | numeric | Reliability |
| PayloadClass | TEXT | Submunition class |
| PayloadQuantity | numeric | Submunition count |
| DatalinkRange_km | REAL | Wire guidance range |
| AcceptsUserCommands | numeric | Player retarget |
| DetonationRange_m | numeric | Proximity fuze |
| NavigationError_m | NUMERIC | Guidance error |
| TS | numeric | Acoustic target strength |
| TS_Model | TEXT | Acoustic model |
| AcousticModel | TEXT | Noise model |
| SL_Model | TEXT | Source level model |
| maxTurnRate_degps | numeric | Seeker turn rate |
| maxDepth_m | numeric | Max operating depth |
| battery_kJ | numeric | Battery energy |
| batteryRate_kW | numeric | Power draw |
| maxSpeed_kts | numeric | Top speed |
| acceleration_ktsps | numeric | Acceleration |
| sonarClass | TEXT | Homing sonar class |
| wireGuidance | numeric | 1 = wire-guided |
| preEnableSpeed_kts | numeric | Arming speed |
| WeaponType | numeric | Torpedo type enum |

### ballistic

Unguided bombs, rockets, and gun ammunition.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Unique class name |
| DisplayClass | TEXT | User-facing name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | NUMERIC | Weight |
| Volume_m3 | NUMERIC | Volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Year introduced |
| FinalYear | NUMERIC | Year retired |
| Country | TEXT | Origin |
| Subtype | TEXT | Subtype |
| Author | TEXT | Entry author |
| Description | TEXT | Description |
| Notes | TEXT | Notes |
| Sources | TEXT | Sources |
| Damage | numeric | Warhead damage |
| DamageModel | TEXT | Damage model |
| DamageEffect | TEXT | References damage_effect |
| LaunchSpeed_mps | numeric | Muzzle/launch speed |
| targetFlags | numeric | Target type bitmask |
| MinLaunchAlt_m | numeric | Min altitude |
| MaxLaunchAlt_m | numeric | Max altitude |
| MinRange_km | numeric | Min range |
| MaxRange_km | numeric | Max range |
| ProbNoFaults | numeric | Reliability |
| PayloadClass | TEXT | Submunition class |
| PayloadQuantity | numeric | Submunition count |
| DatalinkRange_km | REAL | Datalink range |
| AcceptsUserCommands | numeric | Player retarget |
| DetonationRange_m | numeric | Fuze radius |
| NavigationError_m | NUMERIC | Accuracy error |
| BallisticType | numeric | Type (bomb, shell, rocket) |
| AngleError_rad | numeric | Launch angle error |
| BurstCount | numeric | Rounds per burst |
| BurstDuration_s | numeric | Burst duration |
| ClusterCount | numeric | Cluster submunition count |
| ClusterEffectRadius_m | numeric | Cluster dispersion radius |
| SensorClass | numeric | Sensor for smart munitions |
| SmartMaxClimb_rad | numeric | Max climb for smart munitions |
| SmartError_m | numeric | Smart guidance accuracy |
| LockOnAfterLaunch | NUMERIC | 1 = LOAL guidance |

### ballistic_missile

Ballistic missiles with multiple flight stages.

**Primary Key:** DatabaseClass

Shares all columns from `ballistic`, plus:

| Column | Type | Description |
|--------|------|-------------|
| TimeStage1_s | numeric | Stage 1 burn time |
| AccelStage1_mps2 | numeric | Stage 1 acceleration |
| BCStage1 | numeric | Stage 1 ballistic coefficient |
| TimeStage2_s–TimeStage4_s | numeric | Stages 2–4 burn times |
| AccelStage2–4_mps2 | numeric | Stage accelerations |
| BCStage2–4 | numeric | Stage ballistic coefficients |

### directed_energy

Laser and high-power microwave weapons.

**Primary Key:** DatabaseClass

Shares common weapon columns, plus:

| Column | Type | Description |
|--------|------|-------------|
| DEType | NUMERIC | Directed energy type enum |
| Power_kW | NUMERIC | Output power |
| Aperture_m | REAL | Beam aperture |
| DwellTime_s | NUMERIC | Time on target per shot |
| RecoveryTime_s | NUMERIC | Cooldown between shots |
| MinSpot_m | REAL | Minimum beam spot size |
| MinBeamwidth_deg | NUMERIC | Minimum divergence |
| Efficiency | NUMERIC | Wall-plug efficiency |
| Capacity_kJ | NUMERIC | Energy storage |
| Charge_kW | NUMERIC | Recharge rate |

### cm

Countermeasures (chaff, flares, decoys).

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| DisplayClass | TEXT | Display name |
| ModelClassId | INTEGER | See enum |
| ClassificationId | INTEGER | See enum |
| Weight_kg | numeric | Weight |
| Volume_m3 | NUMERIC | Volume |
| ObjectBounds | TEXT | Bounding box |
| InitialYear | numeric | Year introduced |
| FinalYear | numeric | Year retired |
| Country | TEXT | Origin |
| Subtype | TEXT | Subtype |
| LifeSpan_s | NUMERIC | Effective duration |
| Effectiveness | REAL | Countermeasure effectiveness (0–1) |
| MaxSpeed_mps | REAL | Maximum drift speed |
| AirSignatureModel | TEXT | Signature model |
| RCS_dBsm | REAL | Decoy RCS |
| IRSignatureMW_dB | REAL | IR signature MW |
| IRSignatureLW_dB | REAL | IR signature LW |
| TS | numeric | Acoustic target strength |

### fueltank

External fuel tanks for aircraft.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| DisplayClass | TEXT | Display name |
| FuelCapacity_kg | numeric | Additional fuel capacity |
| (+ common fields) | | Weight, volume, years, country, etc. |

### item

Generic non-weapon items (spare parts, passengers, cargo).

**Primary Key:** DatabaseClass

Contains only the common identification columns (DatabaseClass through Sources). No performance parameters.

### sonobuoy

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| TS | numeric | Acoustic target strength |
| TS_Model | TEXT | Acoustic model |
| AcousticModel | TEXT | Noise model |
| SL_Model | TEXT | Source level model |
| BatteryLife_s | numeric | Operational lifetime |
| CommRange_km | REAL | Data transmission range |
| (+ common fields) | | Weight, volume, years, etc. |

---

## Sensor Tables

### radar

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| MaxRange_km | numeric | Maximum detection range |
| RefRange_km | numeric | Reference range (for RCS=0dBsm) |
| FieldOfView_deg | numeric | Horizontal scan arc |
| MinElevation_deg | numeric | Lower elevation limit |
| MaxElevation_deg | numeric | Upper elevation limit |
| ScanPeriod_s | numeric | Full-scan cycle time |
| DamageEffect | TEXT | References damage_effect |
| RangeError | numeric | Range measurement error |
| AngleError_deg | numeric | Bearing error |
| ElevationError_deg | numeric | Elevation error |
| IdThreshold_dB | REAL | Identification threshold |
| CounterMeasureFactor | numeric | ECM susceptibility |
| IsSurveillance | numeric | 1 = surveillance (not fire control) |
| FreqMin_MHz | REAL | Frequency band min |
| FreqMax_MHz | REAL | Frequency band max |
| ERPpeak_dBW | numeric | Peak effective radiated power |
| ERPaverage_dBW | numeric | Average ERP |
| MaxFireControlTracks | numeric | Max simultaneous fire control tracks |
| IsSemiactive | numeric | 1 = illuminates for semi-active missiles |
| BlindSpeed_mps | numeric | Doppler blind speed |
| LookdownWater_dB | numeric | Sea clutter attenuation |
| LookdownLand_dB | numeric | Land clutter attenuation |
| Bandwidth_MHz | numeric | Signal bandwidth |
| AzimuthBeamwidth_deg | numeric | Horizontal beamwidth |
| ElevationBeamwidth_deg | numeric | Vertical beamwidth |
| EffectiveSidelobes_dB | numeric | Effective sidelobe level |
| DetectsSurface | numeric | 1 = detects surface targets |
| DetectsAir | numeric | 1 = detects air targets |
| DetectsMissile | numeric | 1 = detects missiles |
| DetectsGround | numeric | 1 = detects ground targets |
| (+ common identification fields) | | |

### sonar

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| MaxRange_km | numeric | Maximum detection range |
| RefRange_km | numeric | Reference range |
| FieldOfView_deg | numeric | Coverage arc |
| ScanPeriod_s | numeric | Scan cycle |
| SL | numeric | Source level (active) |
| DI | numeric | Directivity index |
| FreqMin_Hz | NUMERIC | Frequency min |
| FreqMax_Hz | NUMERIC | Frequency max |
| isPassive | INTEGER | 1 = passive operation |
| isActive | INTEGER | 1 = active operation |
| isTowed | INTEGER | 1 = towed array |
| maxScope_m | numeric | Periscope depth limit for use |
| isWakeHoming | INTEGER | 1 = wake-following mode |
| (+ common sensor fields) | | Range/angle errors, etc. |

### optical

Electro-optical and IR sensors.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| MaxFireControlTracks | numeric | Max fire control tracks |
| IsSemiactive | numeric | 1 = laser designator/illuminator |
| IsDesignator | numeric | 1 = laser designator |
| DetectsSurface/Air/Missile/Ground | numeric | Target type flags |
| IsIR | numeric | 1 = IR band |
| NightFactor | numeric | Night detection factor |
| WaveMin_um | REAL | Wavelength band min (micrometers) |
| WaveMax_um | REAL | Wavelength band max |
| (+ common sensor fields) | | |

### ecm

Electronic countermeasures (jammers).

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| EcmType | TEXT | Jammer type |
| FreqMin_MHz | REAL | Frequency band min |
| FreqMax_MHz | REAL | Frequency band max |
| ERP_dBW | numeric | Effective radiated power |
| EffectivenessRating | REAL | Overall effectiveness (0–1) |
| IsEffectiveVsSurveillance | INTEGER | Degrades surveillance radars |
| IsEffectiveVsSeeker | INTEGER | Degrades missile seekers |
| (+ common sensor fields) | | |

### esm

Electronic support measures (radar warning/ELINT).

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Class name |
| IsRWR | INTEGER | 1 = radar warning receiver |
| FreqMin_MHz | REAL | Detection frequency band min |
| FreqMax_MHz | REAL | Detection frequency band max |
| (+ common sensor fields) | | |

---

## Platform Support Tables

### stores

Magazine/storage classes carried by platforms. Referenced by `platform_magazine.MagazineClass`.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Stores class name |
| DisplayName | TEXT | User-facing name |
| Capacity | numeric | Maximum item count |
| MaxVolume_m3 | numeric | Volume capacity |
| MaxWeight_kg | numeric | Weight capacity |
| MoveTime_s | numeric | Time to transfer one item to/from launcher |
| Class1–Class4 | TEXT | Compatible item classes (exact match or equipment_group) |
| (+ common identification fields) | | |

### flightport

Flight deck definitions for carriers, airfields, and helo-capable ships.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Flightport class name |
| IsHeloOnly | INTEGER | 1 = helicopters only |
| HangarCapacity | INTEGER | Hangar spaces |
| DeckCapacity | INTEGER | Deck parking spaces |
| Sp1_launch–Sp16_launch | INTEGER | 1 = this spot is a launch position |
| Sp1_x–Sp16_x | REAL | Spot X position (m, right) |
| Sp1_y–Sp16_y | REAL | Spot Y position (m, forward) |
| Sp1_z–Sp16_z | REAL | Spot Z position (m, up) |
| Sp1_dir_deg–Sp16_dir_deg | REAL | Launch heading offset (deg) |
| Sp1_len–Sp16_len | REAL | Runway/deck length available at this spot |
| (+ common identification fields) | | |

### acoustic_noise

Acoustic noise level model for submarines and ships (used with sonar detection).

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Platform class name |
| Speed1_kts–Speed4_kts | numeric | Speed breakpoints |
| SL1–SL4 | numeric | Source level at each speed breakpoint (dB) |
| SpeedMinNL_kts | numeric | Speed of minimum noise level |
| NL_min | numeric | Minimum noise level (dB) |
| SpeedMaxNL_kts | numeric | Speed of maximum noise level |
| NL_max | numeric | Maximum noise level (dB) |
| CavitationOffset_kts | numeric | Depth offset for cavitation speed |
| CavitationSlope_ktsperft | numeric | Cavitation speed vs depth slope |
| CavitationSL | numeric | Cavitation noise level (dB) |
| SnorkelingSL | numeric | Snorkeling noise level (dB) |

### air_engine

Jet engine performance model (referenced by `air.EngineModel`).

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Engine class name |
| ThrustStatic_kN | REAL | Dry static thrust |
| ThrustStaticAB_kN | REAL | Afterburner static thrust |
| AirflowStatic_kgps | REAL | Static airflow rate |
| VeAlt | REAL | Altitude velocity coefficient |
| VeAltAB | REAL | Afterburner altitude coefficient |
| InletArea_m2 | REAL | Inlet area |
| TSFC | REAL | Thrust-specific fuel consumption (dry) |
| TSFC_AB | REAL | Thrust-specific fuel consumption (AB) |
| EfficiencyLimit | REAL | Peak efficiency factor |
| AfterburnerType | INTEGER | 0=none, 1=standard AB |
| Notes | TEXT | Notes |

### air_signature

Aspect-dependent radar/IR signature model for aircraft.

**Primary Key:** (none)

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | References air, simpleair, or missile |
| Type | INT | Signature type (radar=0, IR=1, optical=2) |
| Frequency | REAL | Radar frequency (for type=0) |
| ModelParam | REAL | Model parameter |
| Pattern | TEXT | Aspect-dependent pattern string |
| Notes | TEXT | Notes |

### weapon_damage

Detailed warhead parameters for damage calculation.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Weapon class name |
| MaxRange_m | REAL | Maximum damage radius |
| ProbDetonate | REAL | Probability of detonation (0–1) |
| IsPenetration | INTEGER | 1 = penetrating warhead |
| BlastCharge_kg | REAL | Blast charge equivalent (kg TNT) |
| FragCharge_kg | REAL | Fragmentation charge |
| RadCharge_kg | REAL | Radiation charge |
| FragMetal_kg | REAL | Fragmentation metal mass |
| FragFragment_kg | REAL | Fragment mass |
| FragSpread | REAL | Fragment dispersion angle |

### damage_effect

Visual/gameplay damage effects triggered when a weapon hits.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Effect class name |
| BlastEffect | TEXT | Blast visual effect |
| WaterBlastEffect | TEXT | Underwater blast effect |
| FragEffect | TEXT | Fragmentation effect |
| RadEffect | TEXT | Radiation effect |
| InternalEffect | TEXT | Internal damage effect |

### radiation_pattern

Aspect-dependent radar cross-section pattern for platforms.

**Primary Key:** DatabaseClass

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Platform or weapon class |
| Top_dB | REAL | Top aspect RCS offset |
| Bottom_dB | REAL | Bottom aspect RCS offset |
| Aspect0–Aspect180 | REAL | RCS (dB) at 10-degree aspect increments (0=nose, 180=tail) |

---

## Reference / Lookup Tables

### platform_sensor

Maps sensors to platforms.

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | numeric | Platform class name |
| SensorClass | numeric | Sensor class name |
| SensorAz | numeric | Sensor azimuth mounting angle (deg) |

### platform_names

Named ship/aircraft instances (hull numbers, service dates).

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Platform class name |
| Name | TEXT | Specific vessel/aircraft name |
| HullNumber | TEXT | Hull/tail number |
| DateInService | numeric | Commission date |
| DateOutService | numeric | Decommission date |

### country_data

| Column | Type | Description |
|--------|------|-------------|
| CountryName | TEXT | Country name (matches Country fields in platform tables) |
| EnsignFile | TEXT | Flag image filename |

### country_names

Maps area/period identifiers to display names.

| Column | Type | Description |
|--------|------|-------------|
| AreaName | numeric | Area identifier |
| DateStart | numeric | Period start |
| DateEnd | numeric | Period end |
| PeriodName | numeric | Period display name |

### cross_reference

Maps alternate names to canonical DatabaseClass names.

| Column | Type | Description |
|--------|------|-------------|
| Name1 | TEXT | Alternate name |
| Name2 | TEXT | Canonical DatabaseClass |

### table_reference

Documents foreign key relationships (metadata).

| Column | Type | Description |
|--------|------|-------------|
| TableName | TEXT | Table containing the foreign key |
| ColumnName | TEXT | Column name |
| ReferenceTable | TEXT | Referenced table |
| ReferenceColumn | TEXT | Referenced column |

### object_bounds

3D bounding box overrides for specific platform classes.

| Column | Type | Description |
|--------|------|-------------|
| DatabaseClass | TEXT | Platform class |
| x_min–x_max | NUMERIC | X axis extent (m) |
| y_min–y_max | NUMERIC | Y axis extent (m) |
| z_min–z_max | NUMERIC | Z axis extent (m) |

---

## Enums

### ModelClassId

| Value | Meaning |
|-------|---------|
| 0 | Default |
| 1 | Surface |
| 2 | Carrier |
| 3 | Air |
| 4 | Fixed Wing |
| 5 | Missile |
| 6 | Helicopter |
| 7 | Subsurface |
| 8 | Submarine |
| 9 | Torpedo |
| 10 | Fixed Ground |
| 11 | Platform |
| 12 | Jet |
| 13 | Airfield |
| 14 | Ballistic |
| 15 | Sonobuoy |
| 16 | Air CM |
| 17 | Ground Vehicle |
| 20 | Fuel Tank |
| 21 | Guided Bomb |
| 22 | Water CM |
| 23 | Ballistic Missile |
| 24 | Rocket |
| 25 | Laser |

### ClassificationId

| Value | Meaning |
|-------|---------|
| 16 | Surface |
| 17 | Small Surface |
| 18 | Large Surface |
| 22 | Carrier |
| 32 | Air |
| 33 | Fixed Wing |
| 34 | Helo |
| 36 | Air CM |
| 40 | UAV |
| 64 | Missile |
| 128 | Subsurface |
| 129 | Submarine |
| 130 | Torpedo |
| 132 | Sonobuoy |
| 133 | Sonobuoy Passive |
| 134 | Sonobuoy Active |
| 136 | Water CM |
| 138 | Water Mine |
| 256 | Ground |
| 257 | Airfield |
| 258 | Ground Vehicle |
| 259 | Air Defense |
| 260 | Radar |
| 512 | Ballistic |
| 1024 | Laser |

### targetFlags (bitmask)

Used in `missile.targetFlags`, `torpedo.targetFlags`, `ballistic.targetFlags`, etc.

| Bit | Hex | Meaning |
|-----|-----|---------|
| 0 | 0x0001 | Surface targets |
| 1 | 0x0002 | Air targets |
| 2 | 0x0004 | Land/ground targets |
| 3 | 0x0008 | Missile targets |
| 4 | 0x0010 | Subsurface targets |
| 8 | 0x0100 | Nuclear payload allowed |
| 12 | 0x1000 | AEW/high-value air targets |

**Example:** `targetFlags = 14` → binary `0b1110` → Air + Land + Missile (not Surface, not Subsurface)
