# Scenario version: 0.2.1
# Current-format scenario for Global Conflict Blue: Horizon
from math import *
from random import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Silver Current'
    d['description'] = """At first light, the coalition's controlled relocation has expanded into a contested theater movement. A cruiser-led escort group, logistics shipping, maritime surveillance, fighter cover, strike aircraft, and tanker support are converging on the Gulf of Oman corridor.

Red has committed a third fast-attack craft, a second coastal missile section, layered air defenses, coastal radar cueing, and a two-aircraft interceptor element. Blue must preserve the support group, defeat the surface interception, and suppress enough of the shore network to keep the corridor open."""
    d['author'] = 'OpenAI Codex'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'CarrierStrike.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 27
    d['scenarioId'] = 'silver_current_002'
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

    SM.SetDateTime(2026, 5, 22, 6, 0, 0)
    SM.SetSeaState(3)
    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>

RFA Fort Victoria has been stabilized, but the relocation is no longer a limited escort action. Red has reinforced the maritime interception and activated a layered shore-based threat network astride the corridor.

<color=#00a8ff>FRIENDLY FORCES</color>

USS Mason, HMS Diamond, and USS Chosin form the principal escort; USS Tempest and USCGC Stone cover the inshore and outer surface sectors. RFA Fort Victoria, USNS John Ericsson, and USNS Amelia Earhart form the support group. Sentinel and Broadarrow maintain the air and maritime picture while Tiger and Lancer flights operate beneath Shell 1 tanker support.

<color=#00a8ff>THREAT</color>

Khanjar, Falakhon, and Shamshir are converging from the northwest. Two Bastion sections are protected by Pantsir vehicles and an S-300 site, with Coastwatch radar providing cueing. Phantom interceptors are airborne from the Bandar Abbas strip.

<color=#00a8ff>MISSION</color>

Preserve all three logistics ships, destroy the three hostile fast-attack craft, and eliminate at least two critical nodes in the coastal attack network so the support corridor remains usable.""")

    SM.SetSimpleBriefing(2, """Red is not playable in this scenario.""")

    ##############################
    ### Alliance 1 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Fort Victoria AOR'
    unit.unitName = 'RFA Fort Victoria'
    unit.SetPosition(26.000000, 56.950000, 0.0)
    unit.heading = 108.00
    unit.speed = 9.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm Mark 149-4', 120)
    SM.SetUnitLauncherItem(unit.unitName, 1, '20mm Mark 149-4', 120)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '20mm Mark 149-4', 640)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.702776, 57.062870, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.592082, 57.247144, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.357054, 57.634026, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Arleigh Burke IIA DDGHM'
    unit.unitName = 'USS Mason'
    unit.SetPosition(26.090000, 56.820000, 0.0)
    unit.heading = 108.00
    unit.speed = 18.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-66M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-156', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-174A', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'RIM-162B', 12)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'RIM-162B', 12)
    SM.SetUnitLauncherItem(unit.unitName, 5, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 6, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'RGM-84F Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 8, 'RGM-84F Harpoon', 2)
    SM.SetUnitLauncherItem(unit.unitName, 9, '127mm mk 127 HE-CVT mk 67', 16)
    SM.SetUnitLauncherItem(unit.unitName, 10, 'Mk-54', 3)
    SM.SetUnitLauncherItem(unit.unitName, 11, 'Mk-54', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '120 gallon tank', 3)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-114 Hellfire', 12)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-119B', 2)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-65J', 8)
    SM.AddToUnitMagazine(unit.unitName, 'Chaff-1', 60)
    SM.AddToUnitMagazine(unit.unitName, 'DICASS (110) Sonobuoy', 140)
    SM.AddToUnitMagazine(unit.unitName, 'DIFAR (110) Sonobuoy', 420)
    SM.AddToUnitMagazine(unit.unitName, 'Flare-1', 60)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 46000)
    SM.AddToUnitMagazine(unit.unitName, 'LOFAR (110) Sonobuoy', 150)
    SM.AddToUnitMagazine(unit.unitName, 'Mk-50', 2)
    SM.AddToUnitMagazine(unit.unitName, 'Mk-54', 24)
    SM.AddToUnitMagazine(unit.unitName, 'BGM-109 TLAM', 36)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-156', 8)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-174A', 8)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-66M', 20)
    SM.AddToUnitMagazine(unit.unitName, 'RUM-139 Mod4 ASROC', 10)
    SM.AddToUnitMagazine(unit.unitName, '127mm mk 127 HE-CVT mk 67', 520)
    SM.AddToUnitMagazine(unit.unitName, '20mm mark 244-0 ELC', 900)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.820110, 57.149290, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.691494, 57.276910, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.523748, 57.605330, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Cyclone PBFM'
    unit.unitName = 'USS Tempest'
    unit.SetPosition(25.900000, 57.040000, 0.0)
    unit.heading = 105.00
    unit.speed = 20.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '.50 cal bullet', 450)
    SM.SetUnitLauncherItem(unit.unitName, 1, '.50 cal bullet', 450)
    SM.SetUnitLauncherItem(unit.unitName, 2, '.50 cal bullet', 450)
    SM.SetUnitLauncherItem(unit.unitName, 3, '.50 cal bullet', 450)
    SM.SetUnitLauncherItem(unit.unitName, 4, '25mm APDS', 250)
    SM.SetUnitLauncherItem(unit.unitName, 5, '25mm APDS', 250)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'FIM-92 Stinger', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '.50 cal bullet', 4200)
    SM.AddToUnitMagazine(unit.unitName, '25mm APDS', 1200)
    SM.AddToUnitMagazine(unit.unitName, 'FIM-92 Stinger', 2)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.727746, 57.148242, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.570183, 57.352143, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.393291, 57.660356, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Type 45 DDG'
    unit.unitName = 'HMS Diamond'
    unit.SetPosition(25.500000, 57.250000, 0.0)
    unit.heading = 350.00
    unit.speed = 22.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'ASTER 30', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'ASTER 15', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 3, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, '114mm N4A1 HE', 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, 'ASTER 15', 11)
    SM.AddToUnitMagazine(unit.unitName, 'ASTER 30', 31)
    SM.AddToUnitMagazine(unit.unitName, '114mm N4A1 HE', 800)
    SM.AddToUnitMagazine(unit.unitName, '20mm mark 244-0 ELC', 1046)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 23700)
    SM.AddToUnitMagazine(unit.unitName, 'Sea Skua', 16)
    SM.AddToUnitMagazine(unit.unitName, 'Stingray', 30)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.430552, 57.326866, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.169596, 57.626208, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Henry J Kaiser'
    unit.unitName = 'USNS John Ericsson'
    unit.SetPosition(25.632682, 57.545981, 0.0)
    unit.heading = 280.00
    unit.speed = 14.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 15000000)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.419448, 57.737782, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.303835, 57.811901, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Ticonderoga CG Baseline 4'
    unit.unitName = 'USS Chosin'
    unit.SetPosition(25.580000, 57.500000, 0.0)
    unit.heading = 112.00
    unit.speed = 18.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.450000, 57.800000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.500000, 58.100000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Lewis and Clark'
    unit.unitName = 'USNS Amelia Earhart'
    unit.SetPosition(25.460000, 57.750000, 0.0)
    unit.heading = 72.00
    unit.speed = 15.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.400000, 58.000000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.380000, 58.250000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Legend WMSL'
    unit.unitName = 'USCGC Stone'
    unit.SetPosition(25.720000, 57.450000, 0.0)
    unit.heading = 105.00
    unit.speed = 20.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.500000, 57.600000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.450000, 57.900000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.500000, 58.220000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'E-2D'
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
    unit.SetPosition(26.424282, 56.555618, 0.0)
    unit.heading = 175.00
    unit.speed = 28.0
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
    UI.add_waypoint_advanced(26.070000, 56.920000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Falakhon'
    unit.SetPosition(26.480000, 56.620000, 0.0)
    unit.heading = 182.00
    unit.speed = 30.0
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
    UI.add_waypoint_advanced(26.000000, 57.050000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'K-300P Bastion-P'
    unit.unitName = 'Bastion 1'
    unit.SetPosition(26.835440, 56.333700, 10.0)
    unit.heading = 170.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'P-800 Oniks', 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '3M10 Granat', 3)
    UI.AddTask('Ground1', 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Pantsir-S1'
    unit.unitName = 'Pantsir 1'
    unit.SetPosition(26.834632, 56.338093, 8.0)
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
    unit.className = 'Kaman FACM'
    unit.unitName = 'Shamshir'
    unit.SetPosition(26.320000, 56.680000, 0.0)
    unit.heading = 160.00
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
    UI.add_waypoint_advanced(26.100000, 56.950000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'K-300P Bastion-P'
    unit.unitName = 'Bastion 2'
    unit.SetPosition(26.880000, 56.398544, 12.0)
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
    unit.unitName = 'Pantsir 2'
    unit.SetPosition(26.870324, 56.399035, 8.0)
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
    unit.SetPosition(27.036039, 56.865368, 15.0)
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
    unit.SetPosition(26.792083, 56.078986, 18.0)
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
    goal_temp.SetQuantity(3)
    goal_0_1 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Bastion 1')
    goal_temp.AddTarget('Bastion 2')
    goal_temp.AddTarget('S-300 Site North')
    goal_temp.AddTarget('Coastwatch 1')
    goal_temp.SetQuantity(2)
    goal_0_2 = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_0_0)
    goal_temp.AddGoal(goal_0_1)
    goal_temp.AddGoal(goal_0_2)
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
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(2, 2, 2, 2, 2)

    ##############################
    ### Randomization Info
    ##############################
