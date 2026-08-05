# Follow-on draft scenario for Global Conflict Blue: Horizon
from math import *
from random import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Ember Wake'
    d['description'] = """Hours after the opening gauntlet, the coalition convoy has reversed course. RFA Fort Victoria has taken enough damage to end any immediate push toward the Strait of Hormuz. Blue is now fighting for something more basic: preserving logistics, buying repair time, and preventing a local success from becoming an operational setback.

Red recognizes the opening. A surviving Kaman FAC and a fresh reserve boat are pushing south again while the coastal missile battery remains a live threat. Blue reinforcements are arriving, but not all at once."""
    d['author'] = 'OpenAI Codex Draft'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'CarrierStrike.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 9
    d['scenarioId'] = 'ember_wake_draft_002'
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

    SM.SetDateTime(2026, 5, 21, 18, 0, 0)
    SM.SetStartTheater(57.350000, 25.950000)
    SM.SetSeaState(2)
    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>

RFA Fort Victoria was damaged during the first convoy run and can no longer support the planned westward push. You are conducting an emergency eastward withdrawal to a support rendezvous.

<color=#00a8ff>FRIENDLY FORCES</color>

USS Mason remains the principal escort. USS Tempest is still in the screen but partially depleted. HMS Diamond is arriving to strengthen area air defense. USNS John Ericsson is moving west to support the withdrawal once the force clears the danger zone.

<color=#00a8ff>THREAT</color>

One surviving hostile Kaman FAC has re-engaged with a second reserve boat. The coastal anti-ship battery remains active and may still have one effective salvo left.

<color=#00a8ff>MISSION</color>

Keep RFA Fort Victoria alive for two hours while withdrawing east and preserving the rendezvous with support shipping.""")

    SM.SetSimpleBriefing(2, """Red is not playable in this draft scenario.""")

    ##############################
    ### Alliance 1 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Fort Victoria AOR'
    unit.unitName = 'RFA Fort Victoria'
    unit.SetPosition(56.950000, 26.000000, 0.0)
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
    unit.SetPosition(56.820000, 26.090000, 0.0)
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
    unit.SetPosition(57.040000, 25.900000, 0.0)
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
    unit.SetPosition(57.250000, 25.500000, 0.0)
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
    unit.SetPosition(57.545981, 25.632682, 0.0)
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

    ##############################
    ### Alliance 2 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Kaman FACM'
    unit.unitName = 'Khanjar'
    unit.SetPosition(56.555618, 26.424282, 0.0)
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
    unit.SetPosition(56.620000, 26.480000, 0.0)
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
    unit.SetPosition(56.333700, 26.835440, 10.0)
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
    unit.SetPosition(56.338093, 26.834632, 8.0)
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
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.SetQuantity(2)
    goal_0_0 = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Khanjar')
    goal_temp.AddTarget('Falakhon')
    goal_temp.SetQuantity(2)
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
