# Scenario version: 0.2.1
# Generated for GCB Horizon build 25411882; database schema 4
from math import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Island Lance'
    d['description'] = """Campaign Turn 7. A 180-entity, multi-axis operation replaces the repetitive Strait gauntlet with simultaneous island air assault, convoy protection, coastal suppression, maritime interdiction, counter-air, and civilian deconfliction missions."""
    d['author'] = 'Dynamic Campaign Mission Generator'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'ships3.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 180
    d['scenarioId'] = 'island_lance_001'
    return d


def CreateScenario(SM):
    SM.SetScenarioInfo(ScenarioInfo())
    SM.CreateAlliance(1, 'Blue')
    SM.AddAllianceCountry(1, 'USA')
    SM.AddAllianceCountry(1, 'UK')
    SM.SetAlliancePlayable(1, 1)
    SM.CreateAlliance(2, 'Red')
    SM.AddAllianceCountry(2, 'Iran')
    SM.SetAlliancePlayable(2, 0)
    SM.CreateAlliance(3, 'Neutral')
    SM.AddAllianceCountry(3, 'Neutral')
    SM.SetAlliancePlayable(3, 0)
    SM.SetAllianceRelationship(1, 2, 'Hostile')
    SM.SetAllianceRelationship(1, 3, 'Neutral')
    SM.SetAllianceRelationship(2, 3, 'Neutral')
    SM.SetUserAlliance(1)
    SM.SetDateTime(2026, 5, 23, 2, 30, 0)
    SM.SetSeaState(3)
    SM.SetSVP('0.000000,1521.000000,3.000000,1480.000000,20.000000,1485.000000,100.000000,1500.000000,200.000000,1520.000000,300.000000,1530.000000')
    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>

Narrow Furnace preserved the sealift but lost both Lancers and left the Iranian coastal belt largely intact. A reinforced amphibious ready group will now seize a lodgment on Greater Tunb while the convoy completes passage and carrier/land aviation suppress the mainland network. Neutral shipping remains in the battlespace.

<color=#00a8ff>MISSION</color>

Execute six linked missions at once: preserve five convoy auxiliaries; establish the Greater Tunb lodgment; suppress four island-defense nodes; interdict eight hostile maritime units; neutralize seven mainland kill-chain nodes; and protect at least twelve neutral merchants.

<color=#00a8ff>EXECUTION</color>

Osprey and King flights form on the southern approach with Tiger escort and Viper/Venom gunships. Razor/Growler/Viper Strike remain at standoff against the mainland IADS. Poseidon, Romeo, and the submarines isolate the eastern approaches. Do not repeat Narrow Furnace by driving strike aircraft into surviving FAC gun envelopes.

<color=#00a8ff>NEW BUILD NOTES</color>

Use group auto-attack and formation-leader selection to control packages. Improved grounding avoidance should help surface groups, but the player remains responsible for spacing and route changes. Anti-air gun ranges were corrected in this build; respect the displayed envelopes.""")
    SM.SetSimpleBriefing(2, """Contest the Greater Tunb lodgment, break the convoy and amphibious force, and exploit the mainland IADS to fragment BLUE's simultaneous packages. Preserve mobile launchers where possible.""")

    ##############################
    ### Alliance 1 - BLUE (100)
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = "Fort Victoria AOR"
    unit.unitName = "RFA Fort Victoria"
    unit.SetPosition(25.868000, 57.108000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm Mark 149-4", 141)
    SM.SetUnitLauncherItem(unit.unitName, 1, "20mm Mark 149-4", 141)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    SM.AddToUnitMagazine(unit.unitName, "20mm Mark 149-4", 970)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.176000, 56.800000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.401000, 56.535000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.431000, 56.385000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.411000, 56.100000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.411000, 55.800000, 0.000000, 12.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Henry J Kaiser"
    unit.unitName = "USNS John Ericsson"
    unit.SetPosition(25.913000, 57.063000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 15000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.180000, 56.800000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.405000, 56.535000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.435000, 56.385000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.415000, 56.100000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.415000, 55.800000, 0.000000, 12.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Lewis and Clark"
    unit.unitName = "USNS Amelia Earhart"
    unit.SetPosition(25.958000, 57.018000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 1000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.184000, 56.800000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.409000, 56.535000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.439000, 56.385000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.419000, 56.100000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.419000, 55.800000, 0.000000, 12.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Fort Victoria AOR"
    unit.unitName = "RFA Tidespring"
    unit.SetPosition(25.832000, 57.072000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm Mark 149-4", 141)
    SM.SetUnitLauncherItem(unit.unitName, 1, "20mm Mark 149-4", 141)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    SM.AddToUnitMagazine(unit.unitName, "20mm Mark 149-4", 970)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.156000, 56.770000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.391000, 56.525000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.416000, 56.380000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.396000, 56.080000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.396000, 55.780000, 0.000000, 12.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Henry J Kaiser"
    unit.unitName = "USNS Guadalupe"
    unit.SetPosition(25.877000, 57.027000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 15000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.160000, 56.770000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.395000, 56.525000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.400000, 56.080000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 12.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Lewis and Clark"
    unit.unitName = "USNS Cesar Chavez"
    unit.SetPosition(25.922000, 56.982000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 1000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.164000, 56.770000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.399000, 56.525000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.424000, 56.380000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.404000, 56.080000, 0.000000, 12.000000)
    UI.add_waypoint_advanced(26.404000, 55.780000, 0.000000, 12.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Arleigh Burke IIA DDGHM"
    unit.unitName = "USS Mason"
    unit.SetPosition(25.895000, 56.935000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-66M", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-156", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RIM-174A", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "RIM-162B", 16)
    SM.SetUnitLauncherItem(unit.unitName, 4, "RIM-162B", 16)
    SM.SetUnitLauncherItem(unit.unitName, 5, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 8, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 9, "127mm mk 127 HE-CVT mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 10, "Mk-54", 3)
    SM.SetUnitLauncherItem(unit.unitName, 11, "Mk-54", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "120 gallon tank", 4)
    SM.AddToUnitMagazine(unit.unitName, "AGM-114 Hellfire", 16)
    SM.AddToUnitMagazine(unit.unitName, "AGM-119B", 4)
    SM.AddToUnitMagazine(unit.unitName, "AGM-65J", 12)
    SM.AddToUnitMagazine(unit.unitName, "Chaff-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "DICASS (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "DIFAR (110) Sonobuoy", 608)
    SM.AddToUnitMagazine(unit.unitName, "Flare-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 56117)
    SM.AddToUnitMagazine(unit.unitName, "LOFAR (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "Mk-50", 2)
    SM.AddToUnitMagazine(unit.unitName, "Mk-54", 34)
    SM.AddToUnitMagazine(unit.unitName, "BGM-109 TLAM", 36)
    SM.AddToUnitMagazine(unit.unitName, "RIM-156", 10)
    SM.AddToUnitMagazine(unit.unitName, "RIM-174A", 10)
    SM.AddToUnitMagazine(unit.unitName, "RIM-66M", 28)
    SM.AddToUnitMagazine(unit.unitName, "RUM-139 Mod4 ASROC", 12)
    SM.AddToUnitMagazine(unit.unitName, "127mm mk 127 HE-CVT mk 67", 680)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 1046)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.146000, 56.770000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.396000, 56.530000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.426000, 56.380000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.406000, 56.080000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.406000, 55.780000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Ticonderoga CG Baseline 4"
    unit.unitName = "USS Chosin"
    unit.SetPosition(25.975000, 57.145000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "SM-2MR Bk3B", 29)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-162A", 64)
    SM.SetUnitLauncherItem(unit.unitName, 2, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 3, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, "127mm mk 80 HE-PD mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 7, "127mm mk 80 HE-PD mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Mk-54", 3)
    SM.SetUnitLauncherItem(unit.unitName, 9, "Mk-54", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "127mm mk 80 HE-PD mk 67", 1200)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 1046)
    SM.AddToUnitMagazine(unit.unitName, "120 gallon tank", 4)
    SM.AddToUnitMagazine(unit.unitName, "AGM-114 Hellfire", 16)
    SM.AddToUnitMagazine(unit.unitName, "AGM-119B", 4)
    SM.AddToUnitMagazine(unit.unitName, "AGM-65J", 12)
    SM.AddToUnitMagazine(unit.unitName, "Chaff-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "DICASS (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "DIFAR (110) Sonobuoy", 608)
    SM.AddToUnitMagazine(unit.unitName, "Flare-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 56117)
    SM.AddToUnitMagazine(unit.unitName, "LOFAR (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "Mk-50", 2)
    SM.AddToUnitMagazine(unit.unitName, "Mk-54", 34)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.205000, 56.815000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.430000, 56.550000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.460000, 56.400000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.440000, 56.120000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.440000, 55.820000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Arleigh Burke IIA DDGHM"
    unit.unitName = "USS Thomas Hudner"
    unit.SetPosition(25.840000, 56.990000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-66M", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-156", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RIM-174A", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "RIM-162B", 16)
    SM.SetUnitLauncherItem(unit.unitName, 4, "RIM-162B", 16)
    SM.SetUnitLauncherItem(unit.unitName, 5, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 8, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 9, "127mm mk 127 HE-CVT mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 10, "Mk-54", 3)
    SM.SetUnitLauncherItem(unit.unitName, 11, "Mk-54", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "120 gallon tank", 4)
    SM.AddToUnitMagazine(unit.unitName, "AGM-114 Hellfire", 16)
    SM.AddToUnitMagazine(unit.unitName, "AGM-119B", 4)
    SM.AddToUnitMagazine(unit.unitName, "AGM-65J", 12)
    SM.AddToUnitMagazine(unit.unitName, "Chaff-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "DICASS (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "DIFAR (110) Sonobuoy", 608)
    SM.AddToUnitMagazine(unit.unitName, "Flare-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 56117)
    SM.AddToUnitMagazine(unit.unitName, "LOFAR (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "Mk-50", 2)
    SM.AddToUnitMagazine(unit.unitName, "Mk-54", 34)
    SM.AddToUnitMagazine(unit.unitName, "BGM-109 TLAM", 36)
    SM.AddToUnitMagazine(unit.unitName, "RIM-156", 10)
    SM.AddToUnitMagazine(unit.unitName, "RIM-174A", 10)
    SM.AddToUnitMagazine(unit.unitName, "RIM-66M", 28)
    SM.AddToUnitMagazine(unit.unitName, "RUM-139 Mod4 ASROC", 12)
    SM.AddToUnitMagazine(unit.unitName, "127mm mk 127 HE-CVT mk 67", 680)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 1046)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.140000, 56.769000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.390000, 56.529000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.420000, 56.379000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.400000, 56.079000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.400000, 55.779000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Arleigh Burke III DDGHM"
    unit.unitName = "USS Arleigh Burke"
    unit.SetPosition(25.785000, 57.045000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-174A", 24)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-162B", 64)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RIM-156", 32)
    SM.SetUnitLauncherItem(unit.unitName, 3, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 5, "RGM-84G Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, "RGM-84G Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 7, "127mm mk 127 HE-CVT mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Mk-54", 3)
    SM.SetUnitLauncherItem(unit.unitName, 9, "Mk-54", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "120 gallon tank", 4)
    SM.AddToUnitMagazine(unit.unitName, "AGM-114 Hellfire", 16)
    SM.AddToUnitMagazine(unit.unitName, "Chaff-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "DICASS (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "DIFAR (110) Sonobuoy", 608)
    SM.AddToUnitMagazine(unit.unitName, "Flare-1", 75)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 56117)
    SM.AddToUnitMagazine(unit.unitName, "LOFAR (110) Sonobuoy", 203)
    SM.AddToUnitMagazine(unit.unitName, "Mk-54", 34)
    SM.AddToUnitMagazine(unit.unitName, "BGM-109 TLAM", 36)
    SM.AddToUnitMagazine(unit.unitName, "RIM-174A", 20)
    SM.AddToUnitMagazine(unit.unitName, "RUM-139 Mod4 ASROC", 12)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 1046)
    SM.AddToUnitMagazine(unit.unitName, "127mm mk 127 HE-CVT mk 67", 680)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.134000, 56.770000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.384000, 56.530000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.414000, 56.380000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.394000, 56.080000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.394000, 55.780000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Type 45 DDG"
    unit.unitName = "HMS Diamond"
    unit.SetPosition(26.030000, 57.090000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "ASTER 30", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "ASTER 15", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 3, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, "114mm N4A1 HE", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "ASTER 15", 11)
    SM.AddToUnitMagazine(unit.unitName, "ASTER 30", 31)
    SM.AddToUnitMagazine(unit.unitName, "114mm N4A1 HE", 800)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 1046)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 23700)
    SM.AddToUnitMagazine(unit.unitName, "Sea Skua", 16)
    SM.AddToUnitMagazine(unit.unitName, "Stingray", 30)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.211000, 56.815000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.436000, 56.550000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.466000, 56.400000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.446000, 56.120000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.446000, 55.820000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Type 23 FF"
    unit.unitName = "HMS Richmond"
    unit.SetPosition(25.920000, 57.200000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Sea Wolf", 6)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "114mm N4A1 HE", 16)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm/75 GCM-AO3-2 APDS", 83)
    SM.SetUnitLauncherItem(unit.unitName, 5, "30mm/75 GCM-AO3-2 APDS", 83)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Stingray", 3)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Stingray", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "114mm N4A1 HE", 800)
    SM.AddToUnitMagazine(unit.unitName, "30mm/75 GCM-AO3-2 APDS", 1660)
    SM.AddToUnitMagazine(unit.unitName, "Sea Wolf", 20)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 23700)
    SM.AddToUnitMagazine(unit.unitName, "Sea Skua", 16)
    SM.AddToUnitMagazine(unit.unitName, "Stingray", 29)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.199000, 56.815000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.424000, 56.550000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.454000, 56.400000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.434000, 56.120000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.434000, 55.820000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Cyclone PBFM"
    unit.unitName = "USS Tempest"
    unit.SetPosition(25.945000, 57.075000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 4, "25mm APDS", 400)
    SM.SetUnitLauncherItem(unit.unitName, 5, "25mm APDS", 400)
    SM.SetUnitLauncherItem(unit.unitName, 6, "FIM-92 Stinger", 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 7200)
    SM.AddToUnitMagazine(unit.unitName, "25mm APDS", 2400)
    SM.AddToUnitMagazine(unit.unitName, "FIM-92 Stinger", 6)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.172000, 56.800000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.397000, 56.535000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.427000, 56.385000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.407000, 56.100000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.407000, 55.800000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Legend WMSL"
    unit.unitName = "USCGC Stone"
    unit.SetPosition(25.900000, 57.000000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm mark 244-0 ELC", 523)
    SM.SetUnitLauncherItem(unit.unitName, 5, "57mm HCER", 840)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 24000)
    SM.AddToUnitMagazine(unit.unitName, "57mm HCER", 840)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 523)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 38294)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.152000, 56.770000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.387000, 56.525000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.412000, 56.380000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.392000, 56.080000, 0.000000, 18.000000)
    UI.add_waypoint_advanced(26.392000, 55.780000, 0.000000, 18.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Avenger MCM"
    unit.unitName = "USS Devastator"
    unit.SetPosition(25.980000, 56.925000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 10.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 12000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.168000, 56.770000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.403000, 56.525000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.428000, 56.380000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.408000, 56.080000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.408000, 55.780000, 0.000000, 10.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Avenger MCM"
    unit.unitName = "USS Dextrous"
    unit.SetPosition(26.015000, 56.955000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 10.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 12000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.188000, 56.800000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.413000, 56.535000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.443000, 56.385000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.423000, 56.100000, 0.000000, 10.000000)
    UI.add_waypoint_advanced(26.423000, 55.800000, 0.000000, 10.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "CVN-77 (Nimitz) USS George H.W. Bush"
    unit.unitName = "USS George H.W. Bush"
    unit.SetPosition(25.323411, 58.113014, 0.000000)
    unit.heading = 285.000000
    unit.speed = 16.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.400000, 57.950000, 0.000000, 16.000000)
    UI.add_waypoint_advanced(25.550000, 57.750000, 0.000000, 16.000000)
    UI.add_waypoint_advanced(25.350000, 58.050000, 0.000000, 16.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Wasp LHDM"
    unit.unitName = "USS Iwo Jima"
    unit.SetPosition(25.200000, 57.625000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 16.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-7P(v1)", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-7P(v1)", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RIM-116A RAM", 21)
    SM.SetUnitLauncherItem(unit.unitName, 3, "RIM-116A RAM", 21)
    SM.SetUnitLauncherItem(unit.unitName, 4, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 5, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 8, "25mm APDS", 400)
    SM.SetUnitLauncherItem(unit.unitName, 9, "25mm APDS", 400)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 12000)
    SM.AddToUnitMagazine(unit.unitName, "25mm APDS", 8000)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 1046)
    SM.AddToUnitMagazine(unit.unitName, "RIM-116A RAM", 84)
    SM.AddToUnitMagazine(unit.unitName, "RIM-7P(v1)", 48)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 1200000)
    SM.AddToUnitMagazine(unit.unitName, "120 gallon tank", 8)
    SM.AddToUnitMagazine(unit.unitName, "190 gallon wing tank", 40)
    SM.AddToUnitMagazine(unit.unitName, "300 gallon wing tank", 40)
    SM.AddToUnitMagazine(unit.unitName, "AGM-114 Hellfire", 1675)
    SM.AddToUnitMagazine(unit.unitName, "AGM-119B", 8)
    SM.AddToUnitMagazine(unit.unitName, "AGM-65D", 399)
    SM.AddToUnitMagazine(unit.unitName, "AGM-88C", 160)
    SM.AddToUnitMagazine(unit.unitName, "AIM-120D", 279)
    SM.AddToUnitMagazine(unit.unitName, "AIM-9X", 144)
    SM.AddToUnitMagazine(unit.unitName, "BGM-71E TOW 2", 1675)
    SM.AddToUnitMagazine(unit.unitName, "Chaff-1", 13462)
    SM.AddToUnitMagazine(unit.unitName, "DICASS (110) Sonobuoy", 526)
    SM.AddToUnitMagazine(unit.unitName, "DIFAR (110) Sonobuoy", 1576)
    SM.AddToUnitMagazine(unit.unitName, "Flare-1", 13462)
    SM.AddToUnitMagazine(unit.unitName, "GBU-31A(v)2", 479)
    SM.AddToUnitMagazine(unit.unitName, "GBU-31C(v)4", 479)
    SM.AddToUnitMagazine(unit.unitName, "GBU-32A(v)2", 479)
    SM.AddToUnitMagazine(unit.unitName, "GBU-32C(v)4", 479)
    SM.AddToUnitMagazine(unit.unitName, "GBU-39 SDB", 1436)
    SM.AddToUnitMagazine(unit.unitName, "Hydra-70 rocket", 47747)
    SM.AddToUnitMagazine(unit.unitName, "LOFAR (110) Sonobuoy", 526)
    SM.AddToUnitMagazine(unit.unitName, "Mk 71 Zuni WAFAR", 2333)
    SM.AddToUnitMagazine(unit.unitName, "Mk-46 Mod5", 4)
    SM.AddToUnitMagazine(unit.unitName, "Mk-50", 4)
    SM.AddToUnitMagazine(unit.unitName, "Mk-54", 58)
    SM.AddToUnitMagazine(unit.unitName, "Mk-81", 1117)
    SM.AddToUnitMagazine(unit.unitName, "Mk-82", 1117)
    SM.AddToUnitMagazine(unit.unitName, "Mk-83", 279)
    SM.AddToUnitMagazine(unit.unitName, "Mk-84", 419)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "America LHA"
    unit.unitName = "USS America"
    unit.SetPosition(25.200000, 57.675000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 16.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-162D", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-162D", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RIM-116C RAM", 21)
    SM.SetUnitLauncherItem(unit.unitName, 3, "RIM-116C RAM", 21)
    SM.SetUnitLauncherItem(unit.unitName, 4, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 5, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, "20mm mark 244-0 ELC", 97)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 4200)
    SM.AddToUnitMagazine(unit.unitName, "20mm mark 244-0 ELC", 1046)
    SM.AddToUnitMagazine(unit.unitName, "RIM-116C RAM", 42)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 800000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "San Antonio LPDM"
    unit.unitName = "USS Arlington"
    unit.SetPosition(25.200000, 57.725000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 16.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm AP-I", 100)
    SM.SetUnitLauncherItem(unit.unitName, 5, "30mm AP-I", 100)
    SM.SetUnitLauncherItem(unit.unitName, 6, "RIM-7P(v2)", 1)
    SM.SetUnitLauncherItem(unit.unitName, 7, "RIM-116A RAM", 11)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 24000)
    SM.AddToUnitMagazine(unit.unitName, "30mm AP-I", 2000)
    SM.AddToUnitMagazine(unit.unitName, "RIM-7P(v2)", 15)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Albion Class LPD"
    unit.unitName = "HMS Albion"
    unit.SetPosition(25.200000, 57.775000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 16.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Landing Craft Air Cushion LCAC"
    unit.unitName = "Surf Rider 1"
    unit.SetPosition(26.225000, 55.600000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 32.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 3, "30mm APFSDS-T", 100)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "30mm APFSDS-T", 4000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Landing Craft Air Cushion LCAC"
    unit.unitName = "Surf Rider 2"
    unit.SetPosition(26.225000, 55.675000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 32.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 3, "30mm APFSDS-T", 100)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "30mm APFSDS-T", 4000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Landing Craft Air Cushion LCAC"
    unit.unitName = "Surf Rider 3"
    unit.SetPosition(26.225000, 55.750000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 32.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 3, "30mm APFSDS-T", 100)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "30mm APFSDS-T", 4000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Landing Craft Air Cushion LCAC"
    unit.unitName = "Surf Rider 4"
    unit.SetPosition(26.275000, 55.600000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 32.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm APFSDS-T", 100)
    SM.SetUnitLauncherItem(unit.unitName, 3, "30mm APFSDS-T", 100)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "30mm APFSDS-T", 4000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "LCU 1600 LCU-Navy"
    unit.unitName = "Beachmaster 1"
    unit.SetPosition(26.275000, 55.675000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 10.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".50 cal bullet", 600)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 24000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "LCU 1600 LCU-Navy"
    unit.unitName = "Beachmaster 2"
    unit.SetPosition(26.275000, 55.750000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 10.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".50 cal bullet", 600)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, ".50 cal bullet", 24000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "SSN 774.4 Virginia"
    unit.unitName = "Silent Service 1"
    unit.SetPosition(25.350000, 56.300000, -90.000000)
    unit.heading = 285.000000
    unit.speed = 8.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-48 Mod6", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Mk-48 Mod6", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Mk-48 Mod6", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "UGM-84C Harpoon", 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, "UGM-109C", 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Decoy-1", 10)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Decoy-1", 10)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "Mk-48 Mod6", 19)
    SM.AddToUnitMagazine(unit.unitName, "UGM-84C Harpoon", 5)
    SM.AddToUnitMagazine(unit.unitName, "UGM-109C", 12)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.620000, 55.920000, -90.000000, 8.000000)
    UI.add_waypoint_advanced(25.860000, 55.620000, -90.000000, 6.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "SSN 774.4 Virginia"
    unit.unitName = "Silent Service 2"
    unit.SetPosition(25.350000, 56.324000, -90.000000)
    unit.heading = 285.000000
    unit.speed = 8.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-48 Mod6", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Mk-48 Mod6", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Mk-48 Mod6", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "UGM-84C Harpoon", 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, "UGM-109C", 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Decoy-1", 10)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Decoy-1", 10)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "Mk-48 Mod6", 19)
    SM.AddToUnitMagazine(unit.unitName, "UGM-84C Harpoon", 5)
    SM.AddToUnitMagazine(unit.unitName, "UGM-109C", 12)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.620000, 55.920000, -90.000000, 8.000000)
    UI.add_waypoint_advanced(25.860000, 55.620000, -90.000000, 6.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Astute SSN"
    unit.unitName = "HMS Ambush"
    unit.SetPosition(25.480000, 57.000000, -100.000000)
    unit.heading = 285.000000
    unit.speed = 8.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Spearfish", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Spearfish", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Spearfish", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Spearfish", 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Spearfish", 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, "UGM-109C", 1)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Decoy-1", 1)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Decoy-1", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "Spearfish", 26)
    SM.AddToUnitMagazine(unit.unitName, "UGM-109C", 6)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.550000, -100.000000, 8.000000)
    UI.add_waypoint_advanced(25.920000, 56.120000, -100.000000, 6.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 1"
    unit.SetPosition(25.580000, 56.140000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 2"
    unit.SetPosition(25.580000, 56.164000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 3"
    unit.SetPosition(25.580000, 56.188000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 4"
    unit.SetPosition(25.580000, 56.212000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 5"
    unit.SetPosition(25.598000, 56.140000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 6"
    unit.SetPosition(25.598000, 56.164000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 7"
    unit.SetPosition(25.598000, 56.188000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "MV-22 Osprey"
    unit.unitName = "Osprey 8"
    unit.SetPosition(25.598000, 56.212000, 800.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "CH-53K"
    unit.unitName = "King 1"
    unit.SetPosition(25.560000, 56.020000, 600.000000)
    unit.heading = 285.000000
    unit.speed = 150.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "CH-53K"
    unit.unitName = "King 2"
    unit.SetPosition(25.560000, 56.044000, 600.000000)
    unit.heading = 285.000000
    unit.speed = 150.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "CH-53K"
    unit.unitName = "King 3"
    unit.SetPosition(25.560000, 56.068000, 600.000000)
    unit.heading = 285.000000
    unit.speed = 150.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "CH-53K"
    unit.unitName = "King 4"
    unit.SetPosition(25.560000, 56.092000, 600.000000)
    unit.heading = 285.000000
    unit.speed = 150.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('LandTarget', "Tunb Expeditionary LZ")
    UI.add_waypoint_advanced(25.820000, 55.920000, 900.000000, 190.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup")
    UI.add_waypoint_advanced(26.080000, 55.520000, 500.000000, 190.000000)
    UI.add_waypoint_advanced(26.255000, 55.305000, 120.000000, 80.000000)
    UI.SetNavWaypointTasks(2, "Land")

    unit = SM.GetDefaultUnit()
    unit.className = "AH-1Z Viper"
    unit.unitName = "Viper Gunship 1"
    unit.SetPosition(25.660000, 55.980000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 145.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm M53 API", 230)
    SM.SetUnitLauncherItem(unit.unitName, 1, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "", 0)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.880000, 55.840000, 800.000000, 150.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.160000, 55.420000, 500.000000, 150.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(26.270000, 55.300000, 350.000000, 120.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "AH-1Z Viper"
    unit.unitName = "Viper Gunship 2"
    unit.SetPosition(25.660000, 56.004000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 145.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm M53 API", 230)
    SM.SetUnitLauncherItem(unit.unitName, 1, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "", 0)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.880000, 55.840000, 800.000000, 150.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.160000, 55.420000, 500.000000, 150.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(26.270000, 55.300000, 350.000000, 120.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "AH-1Z Viper"
    unit.unitName = "Viper Gunship 3"
    unit.SetPosition(25.660000, 56.028000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 145.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm M53 API", 230)
    SM.SetUnitLauncherItem(unit.unitName, 1, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "", 0)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.880000, 55.840000, 800.000000, 150.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.160000, 55.420000, 500.000000, 150.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(26.270000, 55.300000, 350.000000, 120.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "AH-1Z Viper"
    unit.unitName = "Viper Gunship 4"
    unit.SetPosition(25.660000, 56.052000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 145.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm M53 API", 230)
    SM.SetUnitLauncherItem(unit.unitName, 1, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-114 Hellfire", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "BGM-71E TOW 2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "", 0)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.880000, 55.840000, 800.000000, 150.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.160000, 55.420000, 500.000000, 150.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(26.270000, 55.300000, 350.000000, 120.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "UH-1Y Venom"
    unit.unitName = "Venom 1"
    unit.SetPosition(25.620000, 55.940000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 140.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Hydra-70 rocket", 19)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Hydra-70 rocket", 19)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".30 cal bullet", 629)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".30 cal bullet", 629)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.880000, 55.840000, 800.000000, 150.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.160000, 55.420000, 500.000000, 150.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(26.270000, 55.300000, 350.000000, 120.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "UH-1Y Venom"
    unit.unitName = "Venom 2"
    unit.SetPosition(25.620000, 55.964000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 140.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Hydra-70 rocket", 19)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Hydra-70 rocket", 19)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".30 cal bullet", 629)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".30 cal bullet", 629)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.880000, 55.840000, 800.000000, 150.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.160000, 55.420000, 500.000000, 150.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(26.270000, 55.300000, 350.000000, 120.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 1"
    unit.SetPosition(25.440000, 56.480000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.700000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 2"
    unit.SetPosition(25.440000, 56.504000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.706000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 3"
    unit.SetPosition(25.440000, 56.528000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.712000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 4"
    unit.SetPosition(25.440000, 56.552000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.718000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 5"
    unit.SetPosition(25.458000, 56.480000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.724000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 6"
    unit.SetPosition(25.458000, 56.504000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.730000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 7"
    unit.SetPosition(25.458000, 56.528000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.736000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 8"
    unit.SetPosition(25.458000, 56.552000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.742000, 56.100000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.250000, 55.380000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(25.780000, 55.920000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Razor 1"
    unit.SetPosition(25.300000, 57.050000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120C7", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AGM-65J", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Razor 2"
    unit.SetPosition(25.300000, 57.074000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120C7", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AGM-65J", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Razor 3"
    unit.SetPosition(25.300000, 57.098000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120C7", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AGM-65J", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Razor 4"
    unit.SetPosition(25.318000, 57.050000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120C7", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AGM-65J", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Razor 5"
    unit.SetPosition(25.318000, 57.074000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120C7", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AGM-65J", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Razor 6"
    unit.SetPosition(25.318000, 57.098000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120C7", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-88C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AGM-65J", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "EA-18G"
    unit.unitName = "Growler 1"
    unit.SetPosition(25.220000, 56.920000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AIM-120C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-88C", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "480 gallon tank", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "EA-18G"
    unit.unitName = "Growler 2"
    unit.SetPosition(25.220000, 56.944000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AIM-120C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-88C", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "480 gallon tank", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "EA-18G"
    unit.unitName = "Growler 3"
    unit.SetPosition(25.220000, 56.968000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AIM-120C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-88C", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "480 gallon tank", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "EA-18G"
    unit.unitName = "Growler 4"
    unit.SetPosition(25.220000, 56.992000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AIM-120C", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-88C", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "480 gallon tank", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper Strike 1"
    unit.SetPosition(24.940000, 56.900000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 430.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "GBU-39 SDB", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "GBU-12/B", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "GBU-31A(v)2", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper Strike 2"
    unit.SetPosition(24.940000, 56.924000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 430.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "GBU-39 SDB", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "GBU-12/B", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "GBU-31A(v)2", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper Strike 3"
    unit.SetPosition(24.940000, 56.948000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 430.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "GBU-39 SDB", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "GBU-12/B", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "GBU-31A(v)2", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper Strike 4"
    unit.SetPosition(24.958000, 56.900000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 430.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "GBU-39 SDB", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "GBU-12/B", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "GBU-31A(v)2", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper Strike 5"
    unit.SetPosition(24.958000, 56.924000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 430.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "GBU-39 SDB", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "GBU-12/B", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "GBU-31A(v)2", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper Strike 6"
    unit.SetPosition(24.958000, 56.948000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 430.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "GBU-39 SDB", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "GBU-12/B", 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, "GBU-31A(v)2", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.680000, 8500.000000, 430.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.450000, 56.480000, 7800.000000, 440.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(25.660000, 56.840000, 8000.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Hammer 1"
    unit.SetPosition(25.340000, 56.900000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.620000, 56.780000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.020000, 56.180000, 5200.000000, 430.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(25.480000, 56.720000, 7600.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Hammer 2"
    unit.SetPosition(25.340000, 56.924000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.620000, 56.780000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.020000, 56.180000, 5200.000000, 430.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(25.480000, 56.720000, 7600.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Hammer 3"
    unit.SetPosition(25.340000, 56.948000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.620000, 56.780000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.020000, 56.180000, 5200.000000, 430.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(25.480000, 56.720000, 7600.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Hammer 4"
    unit.SetPosition(25.340000, 56.972000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AGM-84F Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.620000, 56.780000, 7600.000000, 420.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.020000, 56.180000, 5200.000000, 430.000000)
    UI.SetNavWaypointTasks(1, "AutoAttack")
    UI.add_waypoint_advanced(25.480000, 56.720000, 7600.000000, 400.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "P-8 MPA"
    unit.unitName = "Poseidon 1"
    unit.SetPosition(25.080000, 57.550000, 7000.000000)
    unit.heading = 285.000000
    unit.speed = 310.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-84D Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AN/AAQ-24 Nemesis Laser Beam", 100)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "P-8 MPA"
    unit.unitName = "Poseidon 2"
    unit.SetPosition(25.080000, 57.574000, 7000.000000)
    unit.heading = 285.000000
    unit.speed = 310.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-84D Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AN/AAQ-24 Nemesis Laser Beam", 100)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "P-8 MPA"
    unit.unitName = "Poseidon 3"
    unit.SetPosition(25.080000, 57.598000, 7000.000000)
    unit.heading = 285.000000
    unit.speed = 310.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-84D Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AN/AAQ-24 Nemesis Laser Beam", 100)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "P-8 MPA"
    unit.unitName = "Poseidon 4"
    unit.SetPosition(25.080000, 57.622000, 7000.000000)
    unit.heading = 285.000000
    unit.speed = 310.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-84D Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AN/AAQ-24 Nemesis Laser Beam", 100)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "E-2D"
    unit.unitName = "Hawkeye 1"
    unit.SetPosition(25.120000, 57.300000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 280.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    UI.add_waypoint_advanced(25.380000, 56.920000, 8500.000000, 280.000000)
    UI.add_waypoint_advanced(25.120000, 57.300000, 8500.000000, 280.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "E-2D"
    unit.unitName = "Hawkeye 2"
    unit.SetPosition(25.120000, 57.324000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 280.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    UI.add_waypoint_advanced(25.380000, 56.920000, 8500.000000, 280.000000)
    UI.add_waypoint_advanced(25.120000, 57.300000, 8500.000000, 280.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "KC-135R"
    unit.unitName = "Shell 1"
    unit.SetPosition(24.920000, 57.550000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 310.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    UI.add_waypoint_advanced(25.050000, 57.100000, 9000.000000, 310.000000)
    UI.add_waypoint_advanced(24.920000, 57.550000, 9000.000000, 310.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "KC-135R"
    unit.unitName = "Shell 2"
    unit.SetPosition(24.920000, 57.574000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 310.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AirEvade", 2.000000, 3)
    UI.AddTask("Nav", 3.000000, 3)
    UI.add_waypoint_advanced(25.050000, 57.100000, 9000.000000, 310.000000)
    UI.add_waypoint_advanced(24.920000, 57.550000, 9000.000000, 310.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "MQ-9B SeaGuardian"
    unit.unitName = "Sea Guardian 1"
    unit.SetPosition(25.550000, 56.820000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 3, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 4, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 6, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 7, "AGM-114 Hellfire", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "MQ-9B SeaGuardian"
    unit.unitName = "Sea Guardian 2"
    unit.SetPosition(25.550000, 56.844000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 3, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 4, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 6, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 7, "AGM-114 Hellfire", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "MQ-9B SeaGuardian"
    unit.unitName = "Sea Guardian 3"
    unit.SetPosition(25.550000, 56.868000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 3, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 4, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 6, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 7, "AGM-114 Hellfire", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "MQ-9B SeaGuardian"
    unit.unitName = "Sea Guardian 4"
    unit.SetPosition(25.550000, 56.892000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 220.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 3, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 4, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DIFAR (50) Sonobuoy", 10)
    SM.SetUnitLauncherItem(unit.unitName, 6, "AGM-114 Hellfire", 1)
    SM.SetUnitLauncherItem(unit.unitName, 7, "AGM-114 Hellfire", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "S-70B Seahawk"
    unit.unitName = "Romeo 1"
    unit.SetPosition(25.780000, 56.420000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 135.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 6, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 7, "DIFAR (100) Sonobuoy", 15)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.920000, 56.050000, 400.000000, 130.000000)
    UI.add_waypoint_advanced(26.050000, 55.720000, 400.000000, 130.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "S-70B Seahawk"
    unit.unitName = "Romeo 2"
    unit.SetPosition(25.780000, 56.444000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 135.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 6, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 7, "DIFAR (100) Sonobuoy", 15)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.920000, 56.050000, 400.000000, 130.000000)
    UI.add_waypoint_advanced(26.050000, 55.720000, 400.000000, 130.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "S-70B Seahawk"
    unit.unitName = "Romeo 3"
    unit.SetPosition(25.780000, 56.468000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 135.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 6, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 7, "DIFAR (100) Sonobuoy", 15)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.920000, 56.050000, 400.000000, 130.000000)
    UI.add_waypoint_advanced(26.050000, 55.720000, 400.000000, 130.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "S-70B Seahawk"
    unit.unitName = "Romeo 4"
    unit.SetPosition(25.780000, 56.492000, 500.000000)
    unit.heading = 285.000000
    unit.speed = 135.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Mk-46 Mod5", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Flare-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 5, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 6, "DICASS (100) Sonobuoy", 5)
    SM.SetUnitLauncherItem(unit.unitName, 7, "DIFAR (100) Sonobuoy", 15)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.920000, 56.050000, 400.000000, 130.000000)
    UI.add_waypoint_advanced(26.050000, 55.720000, 400.000000, 130.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Airstrip, Small (USA)"
    unit.unitName = "Tunb Expeditionary LZ"
    unit.SetPosition(26.258000, 55.304000, 8.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "M113 APC"
    unit.unitName = "Pathfinder 1"
    unit.SetPosition(26.253000, 55.299000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "M113 APC"
    unit.unitName = "Pathfinder 2"
    unit.SetPosition(26.253000, 55.303000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "M113 APC"
    unit.unitName = "Pathfinder 3"
    unit.SetPosition(26.253000, 55.307000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "M2A3 Bradley"
    unit.unitName = "Rampart 1"
    unit.SetPosition(26.255000, 55.301000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "25mm M791 APDS-T", 400)
    SM.SetUnitLauncherItem(unit.unitName, 1, "BGM-71A TOW", 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "BGM-71A TOW", 5)
    UI.AddTask("Ground1", 1.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "M2A3 Bradley"
    unit.unitName = "Rampart 2"
    unit.SetPosition(26.255000, 55.305000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "25mm M791 APDS-T", 400)
    SM.SetUnitLauncherItem(unit.unitName, 1, "BGM-71A TOW", 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "BGM-71A TOW", 5)
    UI.AddTask("Ground1", 1.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Stinger Vehicle"
    unit.unitName = "Stinger Team 1"
    unit.SetPosition(26.255000, 55.309000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Stinger Vehicle"
    unit.unitName = "Stinger Team 2"
    unit.SetPosition(26.255000, 55.313000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)

    ##############################
    ### Alliance 2 - RED (65)
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Khanjar"
    unit.SetPosition(26.200000, 56.525000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "76mm HE-MOM", 240)
    SM.AddToUnitMagazine(unit.unitName, "40mm HE-T", 500)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Falakhon"
    unit.SetPosition(26.200000, 56.600000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "76mm HE-MOM", 240)
    SM.AddToUnitMagazine(unit.unitName, "40mm HE-T", 500)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Scimitar"
    unit.SetPosition(26.200000, 56.675000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "76mm HE-MOM", 240)
    SM.AddToUnitMagazine(unit.unitName, "40mm HE-T", 500)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Zolfaghar"
    unit.SetPosition(26.200000, 56.750000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "76mm HE-MOM", 240)
    SM.AddToUnitMagazine(unit.unitName, "40mm HE-T", 500)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Pr 205ER Tsunami (Iran)"
    unit.unitName = "Tsunami 1"
    unit.SetPosition(26.200000, 56.825000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-21 Termit", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm OF-83 HE-FRAG", 250)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm OF-83 HE-FRAG", 250)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Pr 205ER Tsunami (Iran)"
    unit.unitName = "Tsunami 2"
    unit.SetPosition(26.200000, 56.900000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-21 Termit", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm OF-83 HE-FRAG", 250)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm OF-83 HE-FRAG", 250)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Shamshir"
    unit.SetPosition(26.250000, 56.525000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "76mm HE-MOM", 240)
    SM.AddToUnitMagazine(unit.unitName, "40mm HE-T", 500)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Neyzeh"
    unit.SetPosition(26.250000, 56.600000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "76mm HE-MOM", 240)
    SM.AddToUnitMagazine(unit.unitName, "40mm HE-T", 500)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Tabarzin"
    unit.SetPosition(26.250000, 56.675000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84A Harpoon", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "76mm HE-MOM", 240)
    SM.AddToUnitMagazine(unit.unitName, "40mm HE-T", 500)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Moudge FFG"
    unit.unitName = "IRIS Jamaran"
    unit.SetPosition(26.250000, 56.750000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "76mm HC", 60)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm PFHE", 55)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm HE-T x2", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Moudge FFG"
    unit.unitName = "IRIS Damavand"
    unit.SetPosition(26.250000, 56.825000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "76mm HC", 60)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm PFHE", 55)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm HE-T x2", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Pr 205ER Tsunami (Iran)"
    unit.unitName = "Tsunami 3"
    unit.SetPosition(26.250000, 56.900000, 0.000000)
    unit.heading = 120.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-21 Termit", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm OF-83 HE-FRAG", 250)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm OF-83 HE-FRAG", 250)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("ShipDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Fateh"
    unit.unitName = "Fateh Patrol 1"
    unit.SetPosition(25.780000, 55.660000, -45.000000)
    unit.heading = 120.000000
    unit.speed = 5.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Jask-2", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Jask-2", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "53-65KE", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "TEST-71ME", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "53-65KE", 3)
    SM.AddToUnitMagazine(unit.unitName, "Jask-2", 2)
    SM.AddToUnitMagazine(unit.unitName, "TEST-71ME", 3)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.920000, 55.820000, -50.000000, 5.000000)
    UI.add_waypoint_advanced(26.020000, 56.000000, -55.000000, 5.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Fateh"
    unit.unitName = "Fateh Patrol 2"
    unit.SetPosition(25.780000, 55.684000, -45.000000)
    unit.heading = 120.000000
    unit.speed = 5.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Jask-2", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Jask-2", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "53-65KE", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "TEST-71ME", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "53-65KE", 3)
    SM.AddToUnitMagazine(unit.unitName, "Jask-2", 2)
    SM.AddToUnitMagazine(unit.unitName, "TEST-71ME", 3)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.920000, 55.820000, -50.000000, 5.000000)
    UI.add_waypoint_advanced(26.020000, 56.000000, -55.000000, 5.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Fateh"
    unit.unitName = "Fateh Patrol 3"
    unit.SetPosition(25.780000, 55.708000, -45.000000)
    unit.heading = 120.000000
    unit.speed = 5.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Jask-2", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Jask-2", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "53-65KE", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "TEST-71ME", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "53-65KE", 3)
    SM.AddToUnitMagazine(unit.unitName, "Jask-2", 2)
    SM.AddToUnitMagazine(unit.unitName, "TEST-71ME", 3)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.920000, 55.820000, -50.000000, 5.000000)
    UI.add_waypoint_advanced(26.020000, 56.000000, -55.000000, 5.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Pr 877EKM Paltus(Iran)"
    unit.unitName = "Kilo Patrol 1"
    unit.SetPosition(25.540000, 56.080000, -90.000000)
    unit.heading = 120.000000
    unit.speed = 5.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "9M32M Strela 3", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "TEST-71ME", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "TEST-71ME", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "53-65KE", 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, "53-65KE", 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, "3M54E Klub Alfa", 1)
    SM.SetUnitLauncherItem(unit.unitName, 6, "3M54E Klub Alfa", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "3M54E Klub Alfa", 4)
    SM.AddToUnitMagazine(unit.unitName, "53-65KE", 4)
    SM.AddToUnitMagazine(unit.unitName, "TEST-71ME", 4)
    SM.AddToUnitMagazine(unit.unitName, "9M32M Strela 3", 8)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.220000, -90.000000, 5.000000)
    UI.add_waypoint_advanced(25.900000, 56.360000, -90.000000, 5.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Pr 877EKM Paltus(Iran)"
    unit.unitName = "Kilo Patrol 2"
    unit.SetPosition(25.540000, 56.104000, -90.000000)
    unit.heading = 120.000000
    unit.speed = 5.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "9M32M Strela 3", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "TEST-71ME", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "TEST-71ME", 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, "53-65KE", 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, "53-65KE", 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, "3M54E Klub Alfa", 1)
    SM.SetUnitLauncherItem(unit.unitName, 6, "3M54E Klub Alfa", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "3M54E Klub Alfa", 4)
    SM.AddToUnitMagazine(unit.unitName, "53-65KE", 4)
    SM.AddToUnitMagazine(unit.unitName, "TEST-71ME", 4)
    SM.AddToUnitMagazine(unit.unitName, "9M32M Strela 3", 8)
    UI.AddTask("Submarine1", 1.000000, 3)
    UI.AddTask("SubmarineAttack", 2.000000, 3)
    UI.AddTask("SubmarineEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.720000, 56.220000, -90.000000, 5.000000)
    UI.add_waypoint_advanced(25.900000, 56.360000, -90.000000, 5.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "F-14A"
    unit.unitName = "Shahin 1"
    unit.SetPosition(26.880000, 56.920000, 7600.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-54C ECCM", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-7M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-14A"
    unit.unitName = "Shahin 2"
    unit.SetPosition(26.880000, 56.944000, 7600.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-54C ECCM", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-7M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-14A"
    unit.unitName = "Shahin 3"
    unit.SetPosition(26.880000, 56.968000, 7600.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-54C ECCM", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-7M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "F-14A"
    unit.unitName = "Shahin 4"
    unit.SetPosition(26.880000, 56.992000, 7600.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-54C ECCM", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-7M", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 1"
    unit.SetPosition(27.000000, 56.720000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 2"
    unit.SetPosition(27.000000, 56.744000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 3"
    unit.SetPosition(27.000000, 56.768000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 4"
    unit.SetPosition(27.000000, 56.792000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 5"
    unit.SetPosition(27.000000, 56.816000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 6"
    unit.SetPosition(27.018000, 56.720000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 7"
    unit.SetPosition(27.018000, 56.744000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 8"
    unit.SetPosition(27.018000, 56.768000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 9"
    unit.SetPosition(27.018000, 56.792000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum Reserve 10"
    unit.SetPosition(27.018000, 56.816000, 7200.000000)
    unit.heading = 120.000000
    unit.speed = 420.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1520 Liter Tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "R-27R", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "R-73", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm NR-30 HEI", 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.720000, 56.780000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.180000, 55.620000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(1, "AirPatrolArea,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.420000, 7600.000000, 410.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 1"
    unit.SetPosition(27.040000, 56.480000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 2"
    unit.SetPosition(27.040000, 56.504000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 3"
    unit.SetPosition(27.040000, 56.528000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 4"
    unit.SetPosition(27.040000, 56.552000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 5"
    unit.SetPosition(27.058000, 56.480000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 6"
    unit.SetPosition(27.058000, 56.504000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 7"
    unit.SetPosition(27.058000, 56.528000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer Reserve 8"
    unit.SetPosition(27.058000, 56.552000, 7000.000000)
    unit.heading = 120.000000
    unit.speed = 410.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "R-60", 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Kh-59MK", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Kh-29T", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "KAB-500L", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "23mm AM-23", 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(26.700000, 56.420000, 7000.000000, 410.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.220000, 56.050000, 5500.000000, 420.000000)
    UI.SetNavWaypointTasks(1, "GroundStrike,AutoAttack")
    UI.add_waypoint_advanced(26.550000, 56.620000, 7000.000000, 390.000000)
    UI.SetNavWaypointTasks(2, "AutoAttack")

    unit = SM.GetDefaultUnit()
    unit.className = "P-3F Orion"
    unit.unitName = "Persian Orion 1"
    unit.SetPosition(26.820000, 56.580000, 5500.000000)
    unit.heading = 120.000000
    unit.speed = 300.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "DICASS (105) Sonobuoy", 17)
    SM.SetUnitLauncherItem(unit.unitName, 1, "LOFAR (105) Sonobuoy", 17)
    SM.SetUnitLauncherItem(unit.unitName, 2, "DIFAR (105) Sonobuoy", 50)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Mk-44", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "P-3F Orion"
    unit.unitName = "Persian Orion 2"
    unit.SetPosition(26.820000, 56.604000, 5500.000000)
    unit.heading = 120.000000
    unit.speed = 300.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "DICASS (105) Sonobuoy", 17)
    SM.SetUnitLauncherItem(unit.unitName, 1, "LOFAR (105) Sonobuoy", 17)
    SM.SetUnitLauncherItem(unit.unitName, 2, "DIFAR (105) Sonobuoy", 50)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Mk-44", 2)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Mk-44", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Aircraft1", 1.000000, 3)
    UI.AddTask("AutoAttack", 2.000000, 0)
    UI.AddTask("AirEvade", 3.000000, 3)
    UI.AddTask("Nav", 4.000000, 3)
    UI.add_waypoint_advanced(25.750000, 56.950000, 7000.000000, 300.000000)
    UI.SetNavWaypointTasks(0, "WaitForGroup,AutoAttack")
    UI.add_waypoint_advanced(26.100000, 56.200000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(1, "ASWPatrol,EngageAll")
    UI.add_waypoint_advanced(25.700000, 56.720000, 6500.000000, 300.000000)
    UI.SetNavWaypointTasks(2, "ASWPatrol,EngageAll")

    unit = SM.GetDefaultUnit()
    unit.className = "Khordad-15"
    unit.unitName = "Tunb Khordad"
    unit.SetPosition(26.270000, 55.306000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Sayyad-3", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "Sayyad-3", 24)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Generic Mobile Radar Post 170"
    unit.unitName = "Tunb Watch"
    unit.SetPosition(26.276000, 55.299000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "ZSU-23-4M4 Biryusa"
    unit.unitName = "Tunb Shilka 1"
    unit.SetPosition(26.263000, 55.296000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "ZSU-23-4M4 Biryusa"
    unit.unitName = "Tunb Shilka 2"
    unit.SetPosition(26.267000, 55.314000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "T-72 MBT"
    unit.unitName = "Tunb Armor 1"
    unit.SetPosition(26.272000, 55.316000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "125mm 3VBM19 APFSDS", 39)
    SM.SetUnitLauncherItem(unit.unitName, 1, "12.7x108mm", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "12.7x108mm", 300)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "T-72 MBT"
    unit.unitName = "Tunb Armor 2"
    unit.SetPosition(26.279000, 55.310000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "125mm 3VBM19 APFSDS", 39)
    SM.SetUnitLauncherItem(unit.unitName, 1, "12.7x108mm", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "12.7x108mm", 300)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "K-300P Bastion-P"
    unit.unitName = "Bastion 1"
    unit.SetPosition(26.720000, 57.100000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "3M10 Granat", 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "3M10 Granat", 6)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "K-300P Bastion-P"
    unit.unitName = "Bastion 2"
    unit.SetPosition(26.720000, 57.150000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "3M10 Granat", 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "3M10 Granat", 6)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "K-300P Bastion-P"
    unit.unitName = "Bastion 3"
    unit.SetPosition(26.745000, 57.075000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "3M10 Granat", 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "3M10 Granat", 6)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Pantsir-S1"
    unit.unitName = "Pantsir 1"
    unit.SetPosition(26.745000, 57.125000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm 3UBR8 APDS", 400)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Pantsir-S1"
    unit.unitName = "Pantsir 2"
    unit.SetPosition(26.770000, 56.000000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm 3UBR8 APDS", 400)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Pantsir-S1"
    unit.unitName = "Pantsir 3"
    unit.SetPosition(26.770000, 57.100000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm 3UBR8 APDS", 400)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "S-300PMU-2"
    unit.unitName = "S-300 Site North"
    unit.SetPosition(26.770000, 57.150000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "48N6E2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "48N6E2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "48N6E2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "48N6E2", 4)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "48N6E2", 72)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Khordad-15"
    unit.unitName = "Khordad Coast 1"
    unit.SetPosition(26.795000, 56.025000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Sayyad-3", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "Sayyad-3", 24)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Khordad-15"
    unit.unitName = "Khordad Coast 2"
    unit.SetPosition(26.795000, 57.075000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Sayyad-3", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "Sayyad-3", 24)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Khordad-15"
    unit.unitName = "Khordad Coast 3"
    unit.SetPosition(26.795000, 57.125000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Sayyad-3", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "Sayyad-3", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    SM.AddToUnitMagazine(unit.unitName, "Sayyad-3", 24)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Shahed OWA TEL"
    unit.unitName = "Shahed Battery 1"
    unit.SetPosition(26.820000, 56.000000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Shahed 136", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Shahed 131", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Shahed 238", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Shahed OWA TEL"
    unit.unitName = "Shahed Battery 2"
    unit.SetPosition(26.820000, 56.050000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Shahed 136", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Shahed 131", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Shahed 238", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Shahed OWA TEL"
    unit.unitName = "Shahed Battery 3"
    unit.SetPosition(26.820000, 57.100000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Shahed 136", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Shahed 131", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Shahed 238", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Shahed OWA TEL"
    unit.unitName = "Shahed Battery 4"
    unit.SetPosition(26.820000, 57.150000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Shahed 136", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Shahed 131", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Shahed 238", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Shahed OWA TEL"
    unit.unitName = "Shahed Battery 5"
    unit.SetPosition(26.845000, 56.025000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Shahed 136", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Shahed 131", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Shahed 238", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Shahed OWA TEL"
    unit.unitName = "Shahed Battery 6"
    unit.SetPosition(26.845000, 56.075000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Shahed 136", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Shahed 131", 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Shahed 238", 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Generic Radar Post 300"
    unit.unitName = "Coastwatch North"
    unit.SetPosition(26.845000, 57.050000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Generic Mobile Radar Post 220"
    unit.unitName = "Coastwatch West"
    unit.SetPosition(26.845000, 57.125000, 10.000000)
    unit.heading = 120.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.SetAllSensorState(1)
    UI.AddTask("Ground1", 1.000000, 3)
    UI.AddTask("GroundDefense", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    ##############################
    ### Alliance 3 - NEUTRAL (15)
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = "Container Ship"
    unit.unitName = "Merchant 01"
    unit.SetPosition(25.200000, 57.825000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Oil Tanker"
    unit.unitName = "Merchant 02"
    unit.SetPosition(25.200000, 57.875000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "General Cargo"
    unit.unitName = "Merchant 03"
    unit.SetPosition(25.200000, 57.925000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Chemical Tanker"
    unit.unitName = "Merchant 04"
    unit.SetPosition(25.200000, 57.975000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Container Ship"
    unit.unitName = "Merchant 05"
    unit.SetPosition(25.200000, 58.025000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Oil Tanker"
    unit.unitName = "Merchant 06"
    unit.SetPosition(25.200000, 58.075000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "General Cargo"
    unit.unitName = "Merchant 07"
    unit.SetPosition(25.200000, 58.125000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Chemical Tanker"
    unit.unitName = "Merchant 08"
    unit.SetPosition(25.200000, 58.175000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Container Ship"
    unit.unitName = "Merchant 09"
    unit.SetPosition(25.200000, 58.225000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Oil Tanker"
    unit.unitName = "Merchant 10"
    unit.SetPosition(25.200000, 58.275000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "General Cargo"
    unit.unitName = "Merchant 11"
    unit.SetPosition(25.250000, 57.525000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Chemical Tanker"
    unit.unitName = "Merchant 12"
    unit.SetPosition(25.250000, 57.625000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Container Ship"
    unit.unitName = "Merchant 13"
    unit.SetPosition(25.250000, 57.675000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Oil Tanker"
    unit.unitName = "Merchant 14"
    unit.SetPosition(25.250000, 57.725000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "General Cargo"
    unit.unitName = "Merchant 15"
    unit.SetPosition(25.250000, 57.775000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 11.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 3)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetFuelFraction(1.000000)
    UI.AddTask("Ship1", 1.000000, 3)
    UI.AddTask("Nav", 2.000000, 3)

    ##############################
    ### Initial formations
    ##############################

    UI = SM.GetUnitInterface("USNS John Ericsson")
    UI.SetFormationLeader(SM.GetUnitIdByName("RFA Fort Victoria"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USNS Amelia Earhart")
    UI.SetFormationLeader(SM.GetUnitIdByName("RFA Fort Victoria"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("RFA Tidespring")
    UI.SetFormationLeader(SM.GetUnitIdByName("RFA Fort Victoria"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USNS Guadalupe")
    UI.SetFormationLeader(SM.GetUnitIdByName("RFA Fort Victoria"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USNS Cesar Chavez")
    UI.SetFormationLeader(SM.GetUnitIdByName("RFA Fort Victoria"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS Chosin")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS Thomas Hudner")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS Arleigh Burke")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("HMS Diamond")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("HMS Richmond")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS Tempest")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USCGC Stone")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS Devastator")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS Dextrous")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Mason"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS America")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Iwo Jima"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("USS Arlington")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Iwo Jima"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("HMS Albion")
    UI.SetFormationLeader(SM.GetUnitIdByName("USS Iwo Jima"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Surf Rider 2")
    UI.SetFormationLeader(SM.GetUnitIdByName("Surf Rider 1"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Surf Rider 3")
    UI.SetFormationLeader(SM.GetUnitIdByName("Surf Rider 1"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Surf Rider 4")
    UI.SetFormationLeader(SM.GetUnitIdByName("Surf Rider 1"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Beachmaster 1")
    UI.SetFormationLeader(SM.GetUnitIdByName("Surf Rider 1"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Beachmaster 2")
    UI.SetFormationLeader(SM.GetUnitIdByName("Surf Rider 1"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Falakhon")
    UI.SetFormationLeader(SM.GetUnitIdByName("Khanjar"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Tsunami 1")
    UI.SetFormationLeader(SM.GetUnitIdByName("Khanjar"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Tsunami 2")
    UI.SetFormationLeader(SM.GetUnitIdByName("Khanjar"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("IRIS Damavand")
    UI.SetFormationLeader(SM.GetUnitIdByName("IRIS Jamaran"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Shamshir")
    UI.SetFormationLeader(SM.GetUnitIdByName("IRIS Jamaran"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Neyzeh")
    UI.SetFormationLeader(SM.GetUnitIdByName("IRIS Jamaran"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Tabarzin")
    UI.SetFormationLeader(SM.GetUnitIdByName("IRIS Jamaran"))
    UI.SetFormationMode(1)
    UI = SM.GetUnitInterface("Tsunami 3")
    UI.SetFormationLeader(SM.GetUnitIdByName("IRIS Jamaran"))
    UI.SetFormationMode(1)

    ##############################
    ### Multi-mission goals
    ##############################

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget("RFA Fort Victoria")
    goal_temp.AddTarget("USNS John Ericsson")
    goal_temp.AddTarget("USNS Amelia Earhart")
    goal_temp.AddTarget("RFA Tidespring")
    goal_temp.AddTarget("USNS Guadalupe")
    goal_temp.AddTarget("USNS Cesar Chavez")
    goal_temp.SetQuantity(5)
    blue_0 = goal_temp

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget("USS Iwo Jima")
    goal_temp.AddTarget("USS America")
    goal_temp.AddTarget("USS Arlington")
    goal_temp.AddTarget("HMS Albion")
    goal_temp.AddTarget("Tunb Expeditionary LZ")
    goal_temp.AddTarget("Pathfinder 1")
    goal_temp.AddTarget("Pathfinder 2")
    goal_temp.AddTarget("Pathfinder 3")
    goal_temp.AddTarget("Rampart 1")
    goal_temp.AddTarget("Rampart 2")
    goal_temp.SetQuantity(7)
    blue_1 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget("Tunb Khordad")
    goal_temp.AddTarget("Tunb Watch")
    goal_temp.AddTarget("Tunb Shilka 1")
    goal_temp.AddTarget("Tunb Shilka 2")
    goal_temp.AddTarget("Tunb Armor 1")
    goal_temp.AddTarget("Tunb Armor 2")
    goal_temp.SetQuantity(4)
    blue_2 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget("Khanjar")
    goal_temp.AddTarget("Falakhon")
    goal_temp.AddTarget("Scimitar")
    goal_temp.AddTarget("Zolfaghar")
    goal_temp.AddTarget("Tsunami 1")
    goal_temp.AddTarget("Tsunami 2")
    goal_temp.AddTarget("Shamshir")
    goal_temp.AddTarget("Neyzeh")
    goal_temp.AddTarget("Tabarzin")
    goal_temp.AddTarget("IRIS Jamaran")
    goal_temp.AddTarget("IRIS Damavand")
    goal_temp.AddTarget("Tsunami 3")
    goal_temp.AddTarget("Fateh Patrol 1")
    goal_temp.AddTarget("Fateh Patrol 2")
    goal_temp.AddTarget("Fateh Patrol 3")
    goal_temp.AddTarget("Kilo Patrol 1")
    goal_temp.AddTarget("Kilo Patrol 2")
    goal_temp.SetQuantity(8)
    blue_3 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget("Bastion 1")
    goal_temp.AddTarget("Bastion 2")
    goal_temp.AddTarget("Bastion 3")
    goal_temp.AddTarget("Pantsir 1")
    goal_temp.AddTarget("Pantsir 2")
    goal_temp.AddTarget("Pantsir 3")
    goal_temp.AddTarget("S-300 Site North")
    goal_temp.AddTarget("Khordad Coast 1")
    goal_temp.AddTarget("Khordad Coast 2")
    goal_temp.AddTarget("Khordad Coast 3")
    goal_temp.AddTarget("Coastwatch North")
    goal_temp.AddTarget("Coastwatch West")
    goal_temp.SetQuantity(7)
    blue_4 = goal_temp

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget("Merchant 01")
    goal_temp.AddTarget("Merchant 02")
    goal_temp.AddTarget("Merchant 03")
    goal_temp.AddTarget("Merchant 04")
    goal_temp.AddTarget("Merchant 05")
    goal_temp.AddTarget("Merchant 06")
    goal_temp.AddTarget("Merchant 07")
    goal_temp.AddTarget("Merchant 08")
    goal_temp.AddTarget("Merchant 09")
    goal_temp.AddTarget("Merchant 10")
    goal_temp.AddTarget("Merchant 11")
    goal_temp.AddTarget("Merchant 12")
    goal_temp.AddTarget("Merchant 13")
    goal_temp.AddTarget("Merchant 14")
    goal_temp.AddTarget("Merchant 15")
    goal_temp.SetQuantity(12)
    blue_5 = goal_temp
    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(blue_0)
    goal_temp.AddGoal(blue_1)
    goal_temp.AddGoal(blue_2)
    goal_temp.AddGoal(blue_3)
    goal_temp.AddGoal(blue_4)
    goal_temp.AddGoal(blue_5)
    SM.SetAllianceGoal(1, goal_temp)

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget("USS Iwo Jima")
    goal_temp.AddTarget("USS America")
    goal_temp.AddTarget("USS Arlington")
    goal_temp.AddTarget("HMS Albion")
    goal_temp.AddTarget("Tunb Expeditionary LZ")
    goal_temp.AddTarget("RFA Fort Victoria")
    goal_temp.AddTarget("USNS John Ericsson")
    goal_temp.AddTarget("USNS Amelia Earhart")
    goal_temp.AddTarget("RFA Tidespring")
    goal_temp.AddTarget("USNS Guadalupe")
    goal_temp.AddTarget("USNS Cesar Chavez")
    goal_temp.SetQuantity(5)
    red_strike = goal_temp
    SM.SetAllianceGoal(2, red_strike)

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget("Merchant 01")
    goal_temp.AddTarget("Merchant 02")
    goal_temp.AddTarget("Merchant 03")
    goal_temp.AddTarget("Merchant 04")
    goal_temp.AddTarget("Merchant 05")
    goal_temp.AddTarget("Merchant 06")
    goal_temp.AddTarget("Merchant 07")
    goal_temp.AddTarget("Merchant 08")
    goal_temp.AddTarget("Merchant 09")
    goal_temp.AddTarget("Merchant 10")
    goal_temp.AddTarget("Merchant 11")
    goal_temp.AddTarget("Merchant 12")
    goal_temp.AddTarget("Merchant 13")
    goal_temp.AddTarget("Merchant 14")
    goal_temp.AddTarget("Merchant 15")
    goal_temp.SetQuantity(10)
    neutral_survival = goal_temp
    SM.SetAllianceGoal(3, neutral_survival)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)
    SM.SetAllianceROEByType(2, 2, 2, 2, 2)
    SM.SetAllianceROEByType(3, 0, 0, 0, 0)
