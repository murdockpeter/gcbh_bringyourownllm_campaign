# Draft scenario for Global Conflict Blue: Horizon
from math import *
from random import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Gate Latch'
    d['description'] = """A coalition escort group is shepherding a logistics ship westward through the Gulf of Oman toward the Strait of Hormuz. Iranian fast attack craft have sortied from the northern coast while a coastal anti-ship battery has been detected covering the approaches.

This opening scenario is meant to establish the larger campaign. The immediate task is limited: keep the escorted ship alive, break up the fast attack craft ambush, and preserve the freedom to continue west."""
    d['author'] = 'OpenAI Codex Draft'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'hornet_landing.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 8
    d['scenarioId'] = 'gate_latch_draft_001'
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

    SM.SetDateTime(2026, 5, 21, 6, 0, 0)
    SM.SetStartTheater(56.800000, 26.250000)
    SM.SetSeaState(2)
    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    SM.SetSimpleBriefing(1, """<color=#00a8ff>MISSION</color>

Escort RFA Fort Victoria westward through the Gulf of Oman toward the Strait of Hormuz.

<color=#00a8ff>THREAT</color>

Three hostile fast attack craft are closing from the north. A coastal anti-ship missile battery has also been identified on the Iranian side of the approaches. In this draft build the battery is visible from the start so you can validate the scenario and choose whether to strike it.

<color=#00a8ff>PRIMARY OBJECTIVES</color>

Keep RFA Fort Victoria afloat and destroy the three hostile FACs.

<color=#00a8ff>NOTES</color>

This is a first-pass campaign opener. It favors load stability and a clean tactical problem over scripting complexity.""")

    SM.SetSimpleBriefing(2, """Red is not playable in this draft scenario.""")

    ##############################
    ### Alliance 1 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Fort Victoria AOR'
    unit.unitName = 'RFA Fort Victoria'
    unit.SetPosition(57.220000, 25.980000, 0.0)
    unit.heading = 285.00
    unit.speed = 14.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm Mark 149-4', 141)
    SM.SetUnitLauncherItem(unit.unitName, 1, '20mm Mark 149-4', 141)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '20mm Mark 149-4', 970)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.020000, 56.850000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.090000, 56.520000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Arleigh Burke IIA DDGHM'
    unit.unitName = 'USS Mason'
    unit.SetPosition(57.060000, 26.020000, 0.0)
    unit.heading = 285.00
    unit.speed = 16.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-66M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-156', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-174A', 1)
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
    SM.AddToUnitMagazine(unit.unitName, '120 gallon tank', 4)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-114 Hellfire', 16)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-119B', 4)
    SM.AddToUnitMagazine(unit.unitName, 'AGM-65J', 12)
    SM.AddToUnitMagazine(unit.unitName, 'Chaff-1', 75)
    SM.AddToUnitMagazine(unit.unitName, 'DICASS (110) Sonobuoy', 203)
    SM.AddToUnitMagazine(unit.unitName, 'DIFAR (110) Sonobuoy', 608)
    SM.AddToUnitMagazine(unit.unitName, 'Flare-1', 75)
    SM.AddToUnitMagazine(unit.unitName, 'Fuel', 56117)
    SM.AddToUnitMagazine(unit.unitName, 'LOFAR (110) Sonobuoy', 203)
    SM.AddToUnitMagazine(unit.unitName, 'Mk-50', 2)
    SM.AddToUnitMagazine(unit.unitName, 'Mk-54', 34)
    SM.AddToUnitMagazine(unit.unitName, 'BGM-109 TLAM', 36)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-156', 10)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-174A', 10)
    SM.AddToUnitMagazine(unit.unitName, 'RIM-66M', 28)
    SM.AddToUnitMagazine(unit.unitName, 'RUM-139 Mod4 ASROC', 12)
    SM.AddToUnitMagazine(unit.unitName, '127mm mk 127 HE-CVT mk 67', 680)
    SM.AddToUnitMagazine(unit.unitName, '20mm mark 244-0 ELC', 1046)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 4.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(26.050000, 56.820000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.120000, 56.500000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Cyclone PBFM'
    unit.unitName = 'USS Tempest'
    unit.SetPosition(57.120000, 25.860000, 0.0)
    unit.heading = 285.00
    unit.speed = 22.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '.50 cal bullet', 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, '.50 cal bullet', 600)
    SM.SetUnitLauncherItem(unit.unitName, 2, '.50 cal bullet', 600)
    SM.SetUnitLauncherItem(unit.unitName, 3, '.50 cal bullet', 600)
    SM.SetUnitLauncherItem(unit.unitName, 4, '25mm APDS', 400)
    SM.SetUnitLauncherItem(unit.unitName, 5, '25mm APDS', 400)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'FIM-92 Stinger', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '.50 cal bullet', 7200)
    SM.AddToUnitMagazine(unit.unitName, '25mm APDS', 2400)
    SM.AddToUnitMagazine(unit.unitName, 'FIM-92 Stinger', 6)
    UI.AddTask('Ship1', 2.000000, 3)
    UI.AddTask('ShipDefense', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.add_waypoint_advanced(25.930000, 56.900000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.010000, 56.600000, 0.000000, 0.000000)

    ##############################
    ### Alliance 2 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Peykan'
    unit.SetPosition(56.520000, 26.540000, 0.0)
    unit.heading = 210.00
    unit.speed = 28.0
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
    UI.add_waypoint_advanced(26.270000, 56.900000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Joshan'
    unit.SetPosition(56.660000, 26.600000, 0.0)
    unit.heading = 215.00
    unit.speed = 28.0
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
    UI.add_waypoint_advanced(26.250000, 56.820000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Khanjar'
    unit.SetPosition(56.450000, 26.550000, 0.0)
    unit.heading = 220.00
    unit.speed = 28.0
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
    UI.add_waypoint_advanced(26.220000, 56.700000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = 'K-300P Bastion-P'
    unit.unitName = 'Bastion 1'
    unit.SetPosition(56.330000, 26.770000, 10.0)
    unit.heading = 180.00
    unit.speed = 0.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'P-800 Oniks', 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, '3M10 Granat', 6)
    UI.AddTask('Ground1', 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = 'Pantsir-S1'
    unit.unitName = 'Pantsir 1'
    unit.SetPosition(56.350000, 26.735000, 8.0)
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

    ##############################
    ### Alliance 1 goals
    ##############################

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.SetQuantity(1)
    goal_0_0 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Peykan')
    goal_temp.AddTarget('Joshan')
    goal_temp.AddTarget('Khanjar')
    goal_temp.SetQuantity(3)
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
    goal_temp.SetQuantity(1)
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(2, 2, 2, 2, 2)

    ##############################
    ### Randomization Info
    ##############################
