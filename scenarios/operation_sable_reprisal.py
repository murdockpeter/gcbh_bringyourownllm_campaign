# Scenario version: 0.2.1
# Campaign turn 4: generated from the logged outcome of Operation Silver Current
from math import *
from random import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Sable Reprisal'
    d['description'] = """Five hours after the Silver Current engagement, the coalition support group is still intact but its screen has been mauled. HMS Diamond, USS Tempest, both Tiger fighters, and Broadarrow are gone. USS Mason is withdrawing under damage-control restrictions. Iran has lost both Phantom interceptors, but its coastal missile, radar, and fast-attack-craft network remains operational.

Coalition authorities have approved a limited counterstrike against systems directly supporting the attacks. Fresh air-defense capacity is joining from the Gulf of Oman and Al Dhafra is open for recovery. Iran is using the surviving FAC flotilla, MiG-29 cover, and a small Su-24 strike element to make one more attempt on the convoy before dispersal."""
    d['author'] = 'OpenAI Codex'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'night_attack.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 27
    d['scenarioId'] = 'sable_reprisal_001'
    return d


def CreateScenario(SM):
    SM.SetScenarioInfo(ScenarioInfo())

    SM.CreateAlliance(1, 'Blue')
    SM.AddAllianceCountry(1, 'Blue')
    SM.AddAllianceCountry(1, 'USA')
    SM.AddAllianceCountry(1, 'UK')
    SM.SetAlliancePlayable(1, 1)

    SM.CreateAlliance(2, 'Red')
    SM.AddAllianceCountry(2, 'Red')
    SM.AddAllianceCountry(2, 'Iran')
    SM.SetAlliancePlayable(2, 0)

    SM.SetAllianceRelationship(1, 2, 'Hostile')
    SM.SetUserAlliance(1)
    SM.SetDateTime(2026, 5, 22, 12, 0, 0)
    SM.SetSeaState(3)
    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>

Silver Current preserved the convoy, but at unacceptable cost. HMS Diamond, USS Tempest, Tiger flight, and Broadarrow were lost. USS Mason survived with heavy damage and is making twelve knots under escort. Iranian Phantom flight was destroyed, but the coastal kill chain and all three hostile fast-attack craft survived.

The National Command Authority has authorized a limited response against forces directly supporting the attacks. This is not permission for a general strike on Iran.

<color=#00a8ff>MISSION</color>

Cover the withdrawal of RFA Fort Victoria, USNS John Ericsson, USNS Amelia Earhart, and damaged USS Mason. Destroy both inbound Su-24 strike aircraft. Neutralize at least two nodes among Bastion 1, Bastion 2, and Coastwatch 1.

<color=#00a8ff>EXECUTION</color>

USS Chosin and USCGC Stone remain with the withdrawal group. USS Thomas Hudner is arriving from the southeast to restore area air defense. Lancer flight is the limited-response strike package; Viper flight provides CAP. Al Dhafra is now an allied landing destination for every BLUE aircraft.

Positive control applies to the shore strike. Designate the exposed Bastion or Coastwatch targets manually. Do not drive aircraft or ships into the surviving FAC gun envelope. The Iranian boats are not required objectives and may withdraw to fight another day.

<color=#00a8ff>ROE</color>

Engage hostile aircraft and missiles immediately. Surface engagement is authorized in self-defense. Shore attack is restricted to the three designated coastal-network targets.""")

    SM.SetSimpleBriefing(2, """Red is not playable in this scenario.""")

    ##############################
    ### Alliance 1 - withdrawal group and reinforcements
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Fort Victoria AOR'
    unit.unitName = 'RFA Fort Victoria'
    unit.SetPosition(25.357054, 57.634026, 0.0)
    unit.heading = 118.0
    unit.speed = 8.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm Mark 149-4', 120)
    SM.SetUnitLauncherItem(unit.unitName, 1, '20mm Mark 149-4', 120)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '20mm Mark 149-4', 420)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('ShipDefense', 3.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.260000, 57.950000, 0.0, 0.0)
    UI.add_waypoint_advanced(25.280000, 58.250000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Henry J Kaiser'
    unit.unitName = 'USNS John Ericsson'
    unit.SetPosition(25.303835, 57.811901, 0.0)
    unit.heading = 112.0
    unit.speed = 13.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 11500000)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.250000, 58.050000, 0.0, 0.0)
    UI.add_waypoint_advanced(25.300000, 58.300000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Lewis and Clark'
    unit.unitName = 'USNS Amelia Earhart'
    unit.SetPosition(25.380000, 58.250000, 0.0)
    unit.heading = 105.0
    unit.speed = 14.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.350000, 58.400000, 0.0, 0.0)

    # Mason represents the logged heavy-damage survivor: reduced speed and depleted cells.
    unit = SM.GetDefaultUnit()
    unit.className = 'Arleigh Burke IIA DDGHM'
    unit.unitName = 'USS Mason'
    unit.SetPosition(25.900000, 57.100000, 0.0)
    unit.heading = 132.0
    unit.speed = 12.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-156', 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-174A', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RUM-139 Mod4 ASROC', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'RIM-162B', 8)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'RIM-162B', 8)
    SM.SetUnitLauncherItem(unit.unitName, 5, '20mm mark 244-0 ELC', 60)
    SM.SetUnitLauncherItem(unit.unitName, 6, '20mm mark 244-0 ELC', 60)
    SM.SetUnitLauncherItem(unit.unitName, 9, '127mm mk 127 HE-CVT mk 67', 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('ShipDefense', 3.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.700000, 57.350000, 0.0, 0.0)
    UI.add_waypoint_advanced(25.500000, 57.650000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Ticonderoga CG Baseline 4'
    unit.unitName = 'USS Chosin'
    unit.SetPosition(25.820000, 57.220000, 0.0)
    unit.heading = 128.0
    unit.speed = 18.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-174A', 24)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-156', 24)
    SM.SetUnitLauncherItem(unit.unitName, 2, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 3, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, '127mm mk 127 HE-CVT mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 7, '127mm mk 127 HE-CVT mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 8, 'Mk-54', 3)
    SM.SetUnitLauncherItem(unit.unitName, 9, 'Mk-54', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('ShipDefense', 4.0, 3)
    UI.AddTask('PointDefense', 3.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.620000, 57.520000, 0.0, 0.0)
    UI.add_waypoint_advanced(25.430000, 57.850000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Legend WMSL'
    unit.unitName = 'USCGC Stone'
    unit.SetPosition(25.700000, 57.350000, 0.0)
    unit.heading = 125.0
    unit.speed = 17.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 1, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 2, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 3, '.50 cal bullet', 400)
    SM.SetUnitLauncherItem(unit.unitName, 4, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 5, '57mm HE', 100)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('ShipDefense', 3.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.520000, 57.650000, 0.0, 0.0)
    UI.add_waypoint_advanced(25.380000, 57.950000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Arleigh Burke IIA DDGHM'
    unit.unitName = 'USS Thomas Hudner'
    unit.SetPosition(25.300000, 58.200000, 0.0)
    unit.heading = 295.0
    unit.speed = 22.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-174A', 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-156', 12)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RUM-139 Mod4 ASROC', 6)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'RIM-162B', 16)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'RIM-162B', 16)
    SM.SetUnitLauncherItem(unit.unitName, 5, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 6, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 8, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 9, '127mm mk 127 HE-CVT mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 10, 'Mk-54', 3)
    SM.SetUnitLauncherItem(unit.unitName, 11, 'Mk-54', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('ShipDefense', 4.0, 3)
    UI.AddTask('PointDefense', 3.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.450000, 57.900000, 0.0, 0.0)
    UI.add_waypoint_advanced(25.600000, 57.650000, 0.0, 0.0)

    # Recovery base added because Silver Current aircraft had no valid landing destination.
    unit = SM.GetDefaultUnit()
    unit.className = 'Airstrip(USA)'
    unit.unitName = 'Al Dhafra Air Base'
    unit.SetPosition(24.248000, 54.547000, 20.0)
    unit.heading = 130.0
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 250000)
    SM.AddToUnitMagazine(unit.unitName, 'AIM-120D', 48)
    SM.AddToUnitMagazine(unit.unitName, 'AIM-9X', 32)
    SM.AddToUnitMagazine(unit.unitName, 'GBU-39 SDB', 64)
    SM.AddToUnitMagazine(unit.unitName, 'GBU-31A(v)2', 24)
    SM.AddToUnitMagazine(unit.unitName, 'Chaff-1', 480)
    SM.AddToUnitMagazine(unit.unitName, 'Flare-1', 480)
    UI.AddTask('Ground1', 2.0, 3)

    # Lancer: limited counterstrike. Targets are visible but require positive player designation.
    unit = SM.GetDefaultUnit()
    unit.className = 'F-15E'
    unit.unitName = 'Lancer 1'
    unit.SetPosition(25.000000, 55.200000, 7600.0)
    unit.heading = 58.0
    unit.speed = 390.0
    unit.throttle = 0.78
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'GBU-39 SDB', 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-120D', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'AIM-9X', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'GBU-12/B', 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'GBU-31A(v)2', 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'Chaff-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, '20mm PGU', 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.650000, 56.000000, 7600.0, 390.0)
    UI.add_waypoint_advanced(26.550000, 56.250000, 7600.0, 390.0)
    UI.add_waypoint_advanced(24.600000, 54.900000, 6000.0, 360.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'F-15E'
    unit.unitName = 'Lancer 2'
    unit.SetPosition(24.920000, 55.280000, 7600.0)
    unit.heading = 60.0
    unit.speed = 390.0
    unit.throttle = 0.78
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'GBU-39 SDB', 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-120D', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'AIM-9X', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'GBU-12/B', 4)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'GBU-31A(v)2', 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'Chaff-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, '20mm PGU', 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.550000, 56.100000, 7600.0, 390.0)
    UI.add_waypoint_advanced(26.600000, 56.350000, 7600.0, 390.0)
    UI.add_waypoint_advanced(24.550000, 54.850000, 6000.0, 360.0)

    # Viper: replacement defensive CAP, not a direct continuation of the lost Tiger flight.
    unit = SM.GetDefaultUnit()
    unit.className = 'F-15E'
    unit.unitName = 'Viper 1'
    unit.SetPosition(25.350000, 57.100000, 8500.0)
    unit.heading = 330.0
    unit.speed = 380.0
    unit.throttle = 0.72
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '600 gallon tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-120D', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'AIM-9X', 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'AIM-120D', 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'Chaff-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, '20mm PGU', 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.850000, 57.250000, 8500.0, 380.0)
    UI.add_waypoint_advanced(25.350000, 57.100000, 8500.0, 380.0)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = 'F-15E'
    unit.unitName = 'Viper 2'
    unit.SetPosition(25.280000, 57.180000, 8500.0)
    unit.heading = 332.0
    unit.speed = 380.0
    unit.throttle = 0.72
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '600 gallon tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-120D', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'AIM-9X', 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'AIM-120D', 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'Chaff-1', 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, '20mm PGU', 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.780000, 57.350000, 8500.0, 380.0)
    UI.add_waypoint_advanced(25.280000, 57.180000, 8500.0, 380.0)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = 'E-2D'
    unit.unitName = 'Sentinel'
    unit.SetPosition(25.150000, 58.100000, 8500.0)
    unit.heading = 285.0
    unit.speed = 260.0
    unit.throttle = 0.55
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(25.300000, 57.850000, 8500.0, 260.0)
    UI.add_waypoint_advanced(25.100000, 58.200000, 8500.0, 260.0)
    UI.SetNavLoopState(True)

    ##############################
    ### Alliance 2 - surviving kill chain and limited escalation
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Khanjar'
    unit.SetPosition(26.100000, 56.950000, 0.0)
    unit.heading = 310.0
    unit.speed = 24.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RGM-84A Harpoon', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, '76mm HE-MOM', 40)
    SM.SetUnitLauncherItem(unit.unitName, 3, '40mm HE-T', 20)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(26.300000, 56.700000, 0.0, 0.0)
    UI.add_waypoint_advanced(26.450000, 56.550000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Falakhon'
    unit.SetPosition(26.020000, 57.020000, 0.0)
    unit.heading = 315.0
    unit.speed = 18.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, '76mm HE-MOM', 24)
    SM.SetUnitLauncherItem(unit.unitName, 3, '40mm HE-T', 12)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(26.180000, 56.820000, 0.0, 0.0)
    UI.add_waypoint_advanced(26.350000, 56.650000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Shamshir'
    unit.SetPosition(26.180000, 56.880000, 0.0)
    unit.heading = 305.0
    unit.speed = 25.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RGM-84A Harpoon', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, '76mm HE-MOM', 36)
    SM.SetUnitLauncherItem(unit.unitName, 3, '40mm HE-T', 18)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ship1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(26.360000, 56.680000, 0.0, 0.0)
    UI.add_waypoint_advanced(26.500000, 56.560000, 0.0, 0.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'K-300P Bastion-P'
    unit.unitName = 'Bastion 1'
    unit.SetPosition(26.835440, 56.333700, 10.0)
    unit.heading = 170.0
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'P-800 Oniks', 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ground1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)

    unit = SM.GetDefaultUnit()
    unit.className = 'K-300P Bastion-P'
    unit.unitName = 'Bastion 2'
    unit.SetPosition(26.880000, 56.398544, 12.0)
    unit.heading = 165.0
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'P-800 Oniks', 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Ground1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Pantsir-S1'
    unit.unitName = 'Pantsir 1'
    unit.SetPosition(26.834632, 56.338093, 8.0)
    unit.heading = 180.0
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
    UI.AddTask('Ground1', 2.0, 3)
    UI.AddTask('PointDefense', 3.0, 3)
    UI.AddTask('AutoAttack', 4.0, 0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Pantsir-S1'
    unit.unitName = 'Pantsir 2'
    unit.SetPosition(26.870324, 56.399035, 8.0)
    unit.heading = 180.0
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
    UI.AddTask('Ground1', 2.0, 3)
    UI.AddTask('PointDefense', 3.0, 3)
    UI.AddTask('AutoAttack', 4.0, 0)

    # Silver Current omitted S-300 launcher contents; this turn fields the actual battery.
    unit = SM.GetDefaultUnit()
    unit.className = 'S-300PMU-2'
    unit.unitName = 'S-300 Site North'
    unit.SetPosition(27.036039, 56.865368, 15.0)
    unit.heading = 180.0
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '48N6E2', 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, '48N6E2', 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, '48N6E2', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, '48N6E2', 4)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask('Ground1', 2.0, 3)
    UI.AddTask('PointDefense', 3.0, 3)
    UI.AddTask('AutoAttack', 4.0, 0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Generic Radar Post 170'
    unit.unitName = 'Coastwatch 1'
    unit.SetPosition(26.792083, 56.078986, 18.0)
    unit.heading = 180.0
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask('Ground1', 2.0, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Airstrip'
    unit.unitName = 'Bandar Abbas Strip'
    unit.SetPosition(27.080000, 56.980000, 12.0)
    unit.heading = 90.0
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 140000)
    SM.AddToUnitMagazine(unit.unitName, 'R-27R', 20)
    SM.AddToUnitMagazine(unit.unitName, 'R-73', 20)
    SM.AddToUnitMagazine(unit.unitName, 'Kh-59MK', 8)
    UI.AddTask('Ground1', 2.0, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'MiG-29'
    unit.unitName = 'Fulcrum 1'
    unit.SetPosition(26.850000, 56.850000, 7800.0)
    unit.heading = 165.0
    unit.speed = 410.0
    unit.throttle = 0.78
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '1520 Liter Tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-27R', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'R-73', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'R-73', 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, '30mm NR-30 HEI', 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'Chaff-1', 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(26.100000, 57.150000, 7800.0, 410.0)
    UI.add_waypoint_advanced(26.850000, 56.850000, 7800.0, 410.0)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = 'MiG-29'
    unit.unitName = 'Fulcrum 2'
    unit.SetPosition(26.920000, 56.780000, 7800.0)
    unit.heading = 168.0
    unit.speed = 410.0
    unit.throttle = 0.78
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '1520 Liter Tank', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-27R', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'R-73', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'R-73', 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, '30mm NR-30 HEI', 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'Chaff-1', 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(26.180000, 57.050000, 7800.0, 410.0)
    UI.add_waypoint_advanced(26.920000, 56.780000, 7800.0, 410.0)
    UI.SetNavLoopState(True)

    # Limited anti-shipping strike intended to force BLUE air-defense commitment.
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-24M'
    unit.unitName = 'Fencer 1'
    unit.SetPosition(26.950000, 56.650000, 6200.0)
    unit.heading = 150.0
    unit.speed = 420.0
    unit.throttle = 0.80
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'Kh-59MK', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-29T', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'KAB-500L', 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, '23mm AM-23', 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'Chaff-1', 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(26.200000, 57.200000, 6200.0, 420.0)
    UI.add_waypoint_advanced(25.550000, 57.750000, 6200.0, 420.0)
    UI.add_waypoint_advanced(26.950000, 56.650000, 6200.0, 420.0)

    unit = SM.GetDefaultUnit()
    unit.className = 'Su-24M'
    unit.unitName = 'Fencer 2'
    unit.SetPosition(27.000000, 56.580000, 6200.0)
    unit.heading = 152.0
    unit.speed = 420.0
    unit.throttle = 0.80
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'Kh-59MK', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-29T', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'KAB-500L', 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, '23mm AM-23', 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'Chaff-1', 30)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Flare-1', 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('Aircraft1', 2.0, 3)
    UI.AddTask('AutoAttack', 3.0, 0)
    UI.AddTask('AirEvade', 4.0, 3)
    UI.AddTask('Nav', 1.0, 0)
    UI.add_waypoint_advanced(26.300000, 57.100000, 6200.0, 420.0)
    UI.add_waypoint_advanced(25.650000, 57.650000, 6200.0, 420.0)
    UI.add_waypoint_advanced(27.000000, 56.580000, 6200.0, 420.0)

    ##############################
    ### Goals - survival, interception, and bounded retaliation
    ##############################

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.AddTarget('USS Mason')
    goal_temp.SetQuantity(4)
    goal_blue_protect = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Fencer 1')
    goal_temp.AddTarget('Fencer 2')
    goal_temp.SetQuantity(2)
    goal_blue_intercept = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Bastion 1')
    goal_temp.AddTarget('Bastion 2')
    goal_temp.AddTarget('Coastwatch 1')
    goal_temp.SetQuantity(2)
    goal_blue_strike = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_blue_protect)
    goal_temp.AddGoal(goal_blue_intercept)
    goal_temp.AddGoal(goal_blue_strike)
    SM.SetAllianceGoal(1, goal_temp)

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.SetQuantity(2)
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)
    SM.SetAllianceROEByType(2, 2, 2, 2, 2)
