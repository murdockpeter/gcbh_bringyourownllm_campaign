# Scenario version: 0.2.1
from math import *
from random import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Iron Shelter'
    d['description'] = """The coalition withdrawal has become a short-notice stabilization operation. Damaged shipping, incoming logistics, area air-defense reinforcements, maritime patrol coverage, and the first deliberate strike actions against the northern shore are all unfolding at once.

Your task is only one part of that larger fight: hold the support corridor east of the Strait, keep the logistics handoff alive, and break the local Red sea-and-shore threat ring before it can disrupt the operational reset."""
    d['author'] = 'OpenAI Codex Draft'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'operation_iron_shelter.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 22
    d['scenarioId'] = 'iron_shelter_draft_003'
    return d


def CreateScenario(SM):
    info = ScenarioInfo()
    SM.SetScenarioInfo(info)

    SM.CreateAlliance(1, 'Blue')
    SM.AddAllianceCountry(1, 'Blue')
    SM.AddAllianceCountry(1, 'USA')
    SM.AddAllianceCountry(1, 'UK')
    SM.SetAlliancePlayable(1, 1)

    SM.CreateAlliance(2, 'Red')
    SM.AddAllianceCountry(2, 'Red')
    SM.SetAlliancePlayable(2, 0)

    SM.SetAllianceRelationship(1, 2, 'Hostile')
    SM.SetUserAlliance(1)

    SM.SetDateTime(2026, 5, 22, 4, 30, 0)
    SM.SetSeaState(3)
    SM.SetSVP('0.000000,1515.000000,150.000000,1506.000000,250.000000,1501.000000,400.000000,1511.000000,750.000000,1530.000000,5000.000000,1600.000000')

    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>

Blue has transitioned from emergency withdrawal to emergency stabilization. Damaged shipping is still in the area, replenishment units are entering the support box, HMS Diamond and USS Chosin are expanding the air-defense umbrella, Broadarrow and Sentinel are maintaining ISR coverage, and separate strike missions are beginning against Red's northern shore threat ring.

<color=#00a8ff>MISSION</color>

Your force protects the logistics handoff east of Hormuz, defeats the local Red sea threat, and helps suppress the specific shore nodes that can still cue or execute attacks into the support corridor.

<color=#00a8ff>FRIENDLY FORCES</color>

RFA Fort Victoria is damaged and slow but still afloat. USNS John Ericsson and USNS Amelia Earhart are entering the area to restore fuel and stores support. USS Mason remains the forward escort. HMS Diamond and USS Chosin are building a layered air-and-missile defense screen. USCGC Stone is covering the outer surface picture. Friendly AEW, tanker, patrol, CAP, and strike missions are active simultaneously.

<color=#00a8ff>ENEMY FORCES</color>

Red has re-sorted multiple FACs, reactivated a second Bastion battery, thickened local point defense, and is relying on radar cueing plus an S-300 umbrella to contest the corridor. Limited fixed-wing activity from the Bandar Abbas axis is possible during the fight.

<color=#00a8ff>PRIMARY OBJECTIVES</color>

1. Preserve the logistics handoff group.
2. Destroy the active FAC thrust.
3. Knock out the key coastal attack/cueing nodes threatening this sector.

<color=#00a8ff>COMMANDER'S INTENT</color>

You are not fighting the whole theater. Other missions are already in motion. Keep the corridor open, keep the high-value shipping alive, and break the local threat ring hard enough for the larger operation to continue.""")

    SM.SetSimpleBriefing(2, """Red is not playable in this draft scenario.""")

    ##############################
    ### Alliance 1 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Fort Victoria AOR'
    unit.unitName = 'RFA Fort Victoria'
    unit.SetPosition(25.980000, 57.000000, 0.0)
    unit.heading = 95.00
    unit.speed = 8.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm Mark 149-4', 110)
    SM.SetUnitLauncherItem(unit.unitName, 1, '20mm Mark 149-4', 110)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '20mm Mark 149-4', 520)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.950000, 57.450000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.900000, 57.950000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Arleigh Burke IIA DDGHM'
    unit.unitName = 'USS Mason'
    unit.SetPosition(26.050000, 56.870000, 0.0)
    unit.heading = 98.00
    unit.speed = 18.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-66M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-156', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-174A', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'RIM-162B', 10)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'RIM-162B', 10)
    SM.SetUnitLauncherItem(unit.unitName, 5, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 6, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'RGM-84F Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 8, 'RGM-84F Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 9, '127mm mk 127 HE-CVT mk 67', 18)
    SM.SetUnitLauncherItem(unit.unitName, 10, 'Mk-54', 3)
    SM.SetUnitLauncherItem(unit.unitName, 11, 'Mk-54', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '120 gallon tank', 3)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-114 Hellfire', 10)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-119B', 2)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-65J', 8)
    SM.AddToUnitMagazine(unit.unitName, 'Chaff-1', 55)
    SM.AddToUnitMagazine(unit.unitName, 'DICASS (110) Sonobuoy', 120)
    SM.AddToUnitMagazine(unit.unitName, 'DIFAR (110) Sonobuoy', 360)
    SM.AddToUnitMagazine(unit.unitName, 'Flare-1', 55)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 43000)
    SM.AddToUnitMagazine(unit.unitName, 'LOFAR (110) Sonobuoy', 120)
    SM.AddToUnitMagazine(unit.unitName, 'Mk-50', 2)
    SM.AddToUnitMagazine(unit.unitName, 'Mk-54', 20)
    SM.AddToUnitMagazine(unit.unitName, 'BGM-109 TLAM', 24)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-156', 8)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-174A', 6)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-66M', 18)
    SM.AddToUnitMagazine(unit.unitName, 'RUM-139 Mod4 ASROC', 8)
    SM.AddToUnitMagazine(unit.unitName, '127mm mk 127 HE-CVT mk 67', 420)
    SM.AddToUnitMagazine(unit.unitName, '20mm mark 244-0 ELC', 840)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.000000, 57.350000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.960000, 57.860000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Type 45 DDG'
    unit.unitName = 'HMS Diamond'
    unit.SetPosition(25.760000, 57.120000, 0.0)
    unit.heading = 35.00
    unit.speed = 22.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'ASTER 30', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'ASTER 15', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 3, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, '114mm N4A1 HE', 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, 'ASTER 15', 10)
    SM.AddToUnitMagazine(unit.unitName, 'ASTER 30', 28)
    SM.AddToUnitMagazine(unit.unitName, '114mm N4A1 HE', 720)
    SM.AddToUnitMagazine(unit.unitName, '20mm mark 244-0 ELC', 980)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 23000)
    SM.AddToUnitMagazine(unit.unitName, 'Sea Skua', 8)
    SM.AddToUnitMagazine(unit.unitName, 'Stingray', 16)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.880000, 57.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.920000, 57.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Ticonderoga CG Baseline 4'
    unit.unitName = 'USS Chosin'
    unit.SetPosition(25.720000, 57.620000, 0.0)
    unit.heading = 300.00
    unit.speed = 20.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.780000, 57.250000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.620000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Cyclone PBFM'
    unit.unitName = 'USS Tempest'
    unit.SetPosition(25.910000, 57.180000, 0.0)
    unit.heading = 110.00
    unit.speed = 22.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 1, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 2, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 3, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 4, '25mm APDS', 200)
    SM.SetUnitLauncherItem(unit.unitName, 5, '25mm APDS', 200)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'FIM-92 Stinger', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '.50 cal bullet', 3200)
    SM.AddToUnitMagazine(unit.unitName, '25mm APDS', 1000)
    SM.AddToUnitMagazine(unit.unitName, 'FIM-92 Stinger', 2)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.900000, 57.430000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Henry J Kaiser'
    unit.unitName = 'USNS John Ericsson'
    unit.SetPosition(25.820000, 57.900000, 0.0)
    unit.heading = 278.00
    unit.speed = 15.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 15000000)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.830000, 57.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.250000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Lewis and Clark'
    unit.unitName = 'USNS Amelia Earhart'
    unit.SetPosition(25.640000, 58.020000, 0.0)
    unit.heading = 276.00
    unit.speed = 15.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.720000, 57.630000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.770000, 57.320000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Legend WMSL'
    unit.unitName = 'USCGC Stone'
    unit.SetPosition(26.160000, 57.320000, 0.0)
    unit.heading = 70.00
    unit.speed = 20.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.180000, 57.020000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.080000, 57.460000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'E-2C'
    unit.unitName = 'Sentinel'
    unit.SetPosition(25.650000, 58.250000, 8500.0)
    unit.heading = 270.00
    unit.speed = 260.0
    unit.throttle = 0.55
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.720000, 57.780000, 8500.000000, 260.000000)
    UI.add_waypoint_advanced(25.900000, 57.520000, 8500.000000, 260.000000)
    UI.add_waypoint_advanced(25.820000, 57.960000, 8500.000000, 260.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = 'P-8 MPA'
    unit.unitName = 'Broadarrow'
    unit.SetPosition(26.320000, 57.980000, 7600.0)
    unit.heading = 255.00
    unit.speed = 280.0
    unit.throttle = 0.58
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.280000, 57.420000, 7600.000000, 280.000000)
    UI.add_waypoint_advanced(26.050000, 56.980000, 7600.000000, 280.000000)
    UI.add_waypoint_advanced(25.960000, 57.500000, 7600.000000, 280.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = 'F/A-18F'
    unit.unitName = 'Tiger 1'
    unit.SetPosition(25.980000, 58.120000, 7800.0)
    unit.heading = 280.00
    unit.speed = 360.0
    unit.throttle = 0.72
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('AirEvade', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.960000, 57.680000, 7800.000000, 360.000000)
    UI.add_waypoint_advanced(26.120000, 57.280000, 7800.000000, 360.000000)
    UI.add_waypoint_advanced(26.020000, 57.860000, 7800.000000, 360.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = 'F/A-18F'
    unit.unitName = 'Tiger 2'
    unit.SetPosition(25.900000, 58.180000, 7800.0)
    unit.heading = 285.00
    unit.speed = 360.0
    unit.throttle = 0.72
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('AirEvade', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.940000, 57.720000, 7800.000000, 360.000000)
    UI.add_waypoint_advanced(26.100000, 57.240000, 7800.000000, 360.000000)
    UI.add_waypoint_advanced(26.000000, 57.900000, 7800.000000, 360.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = 'F-15E'
    unit.unitName = 'Lancer 1'
    unit.SetPosition(26.420000, 57.820000, 6800.0)
    unit.heading = 300.00
    unit.speed = 420.0
    unit.throttle = 0.76
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('AirEvade', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.350000, 57.100000, 6800.000000, 420.000000)
    UI.add_waypoint_advanced(26.520000, 56.760000, 6800.000000, 420.000000)
    UI.add_waypoint_advanced(26.260000, 57.480000, 6800.000000, 420.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'F-15E'
    unit.unitName = 'Lancer 2'
    unit.SetPosition(26.360000, 57.940000, 6800.0)
    unit.heading = 302.00
    unit.speed = 420.0
    unit.throttle = 0.76
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('AirEvade', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.280000, 57.180000, 6800.000000, 420.000000)
    UI.add_waypoint_advanced(26.460000, 56.820000, 6800.000000, 420.000000)
    UI.add_waypoint_advanced(26.220000, 57.520000, 6800.000000, 420.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'KC-135R'
    unit.unitName = 'Shell 1'
    unit.SetPosition(25.520000, 58.380000, 9000.0)
    unit.heading = 270.00
    unit.speed = 300.0
    unit.throttle = 0.54
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.500000, 57.980000, 9000.000000, 300.000000)
    UI.add_waypoint_advanced(25.620000, 58.280000, 9000.000000, 300.000000)
    UI.SetNavLoopState(True)

    ##############################
    ### Alliance 2 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Khanjar'
    unit.SetPosition(26.360000, 56.560000, 0.0)
    unit.heading = 175.00
    unit.speed = 26.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RGM-84A Harpoon', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RGM-84A Harpoon', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, '76mm HE-MOM', 70)
    SM.SetUnitLauncherItem(unit.unitName, 3, '40mm HE-T', 40)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '76mm HE-MOM', 120)
    SM.AddToUnitMagazine(unit.unitName, '40mm HE-T', 240)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.140000, 56.980000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Falakhon'
    unit.SetPosition(26.480000, 56.620000, 0.0)
    unit.heading = 182.00
    unit.speed = 29.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RGM-84A Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RGM-84A Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, '76mm HE-MOM', 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, '40mm HE-T', 50)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '76mm HE-MOM', 200)
    SM.AddToUnitMagazine(unit.unitName, '40mm HE-T', 360)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.100000, 57.040000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Shamshir'
    unit.SetPosition(26.420000, 56.760000, 0.0)
    unit.heading = 190.00
    unit.speed = 29.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RGM-84A Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RGM-84A Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, '76mm HE-MOM', 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, '40mm HE-T', 50)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '76mm HE-MOM', 240)
    SM.AddToUnitMagazine(unit.unitName, '40mm HE-T', 500)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.000000, 57.120000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'K-300P Bastion-P'
    unit.unitName = 'Bastion 1'
    unit.SetPosition(26.690000, 56.280000, 10.0)
    unit.heading = 175.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'P-800 Oniks', 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ground1', 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'K-300P Bastion-P'
    unit.unitName = 'Bastion 2'
    unit.SetPosition(26.880000, 56.520000, 12.0)
    unit.heading = 165.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'P-800 Oniks', 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ground1', 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Pantsir-S1'
    unit.unitName = 'Pantsir 1'
    unit.SetPosition(26.665000, 56.325000, 8.0)
    unit.heading = 180.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, '30mm 3UBR8 APDS', 400)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask('Ground1', 2.000000, 3)
    UI.AddTask('PointDefense', 3.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Pantsir-S1'
    unit.unitName = 'Pantsir 2'
    unit.SetPosition(26.845000, 56.560000, 8.0)
    unit.heading = 180.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, '95Ya6', 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, '30mm 3UBR8 APDS', 400)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask('Ground1', 2.000000, 3)
    UI.AddTask('PointDefense', 3.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'S-300PMU-2'
    unit.unitName = 'S-300 Site North'
    unit.SetPosition(26.930000, 56.760000, 15.0)
    unit.heading = 180.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask('Ground1', 2.000000, 3)
    UI.AddTask('PointDefense', 3.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Generic Radar Post 170'
    unit.unitName = 'Coastwatch 1'
    unit.SetPosition(26.740000, 56.180000, 18.0)
    unit.heading = 180.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask('Ground1', 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Generic Mobile Radar Post 170'
    unit.unitName = 'Coastwatch 2'
    unit.SetPosition(26.820000, 56.450000, 18.0)
    unit.heading = 180.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask('Ground1', 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Airstrip'
    unit.unitName = 'Bandar Abbas Strip'
    unit.SetPosition(27.080000, 56.980000, 12.0)
    unit.heading = 90.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ground1', 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'F-4E'
    unit.unitName = 'Phantom 1'
    unit.SetPosition(26.980000, 56.920000, 7000.0)
    unit.heading = 190.00
    unit.speed = 360.0
    unit.throttle = 0.74
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('AirEvade', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.520000, 56.980000, 7000.000000, 360.000000)
    UI.add_waypoint_advanced(26.080000, 57.180000, 7000.000000, 360.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'F-4E'
    unit.unitName = 'Phantom 2'
    unit.SetPosition(27.020000, 56.860000, 7000.0)
    unit.heading = 196.00
    unit.speed = 360.0
    unit.throttle = 0.74
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.000000, 3)
    UI.AddTask('AutoAttack', 3.000000, 0)
    UI.AddTask('AirEvade', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.600000, 56.940000, 7000.000000, 360.000000)
    UI.add_waypoint_advanced(26.180000, 57.140000, 7000.000000, 360.000000)

    ##############################
    ### Alliance 1 goals
    ##############################

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.SetQuantity(3)
    goal_0_0 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Khanjar')
    goal_temp.AddTarget('Falakhon')
    goal_temp.AddTarget('Shamshir')
    goal_temp.AddTarget('Bastion 2')
    goal_temp.AddTarget('Coastwatch 2')
    goal_temp.SetQuantity(4)
    goal_0_1 = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_0_0)
    goal_temp.AddGoal(goal_0_1)
    SM.SetAllianceGoal(1, goal_temp)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)

    ##############################
    ### Alliance 2 goals
    ##############################

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.SetQuantity(2)
    goal_1_0 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('USS Mason')
    goal_temp.AddTarget('HMS Diamond')
    goal_temp.AddTarget('USS Chosin')
    goal_temp.SetQuantity(1)
    goal_1_1 = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_1_0)
    goal_temp.AddGoal(goal_1_1)
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(2, 2, 2, 2, 2)

    ##############################
    ### Randomization Info
    ##############################
