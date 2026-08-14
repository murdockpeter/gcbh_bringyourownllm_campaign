# Scenario version: 0.2.1
# Campaign turn 5: generated from the multiplayer outcome of Operation Silver Current
from math import *
from random import *


def ScenarioInfo():
    d = dict()
    d['name'] = 'Operation Resolute Passage'
    d['description'] = """Eight hours after the improved Silver Current action, the coalition has a narrow opportunity to reopen Hormuz. All fifteen BLUE platforms survived, while both Iranian Phantom interceptors and the FAC Shamshir were destroyed. The success demonstrated that disciplined standoff tactics can contain the immediate threat.

The opportunity cannot be left unused. Missile-defense reloads, aviation fuel, repair modules, and medical stores for the forward force in Bahrain are aboard six auxiliaries east of the Strait. Airlift cannot move the required fuel or vertical-launch-system reloads, and inventories inside the Gulf will fall below contingency levels before another sealift package can arrive. The convoy must therefore make a westbound passage through Hormuz.

Iran has declared a temporary exclusion zone and reinforced the surviving coastal network with frigates, missile boats, fighters, and strike aircraft. The coalition response remains a corridor-opening operation, not a general attack on Iran."""
    d['author'] = 'OpenAI Codex'
    d['playableSides'] = 'Blue'
    d['thumb'] = 'ships3.png'
    d['date'] = 'May 2026'
    d['unitCount'] = 54
    d['scenarioId'] = 'resolute_passage_001'
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
    SM.SetDateTime(2026, 5, 22, 14, 0, 0)
    SM.SetSeaState(3)
    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    SM.SetSimpleBriefing(1, """<color=#00a8ff>SITUATION</color>

Your improved Silver Current action destroyed both hostile Phantoms and Shamshir without losing a BLUE platform. That success has opened a short corridor-reentry window.

Bahrain's forward force will fall below contingency stocks of missile-defense reloads, aviation fuel, repair modules, and medical stores within twenty-four hours. Those supplies are aboard six auxiliaries east of Hormuz. Airlift cannot move the required bulk fuel or VLS reloads. The convoy must pass west through the Strait now, before Iran completes another coastal-force cycle.

Iran has declared an exclusion zone and doubled down with reinforced FAC, frigate, fighter, strike, and coastal-missile elements. National authority permits force necessary to open and hold the navigation corridor; it does not authorize attacks beyond the designated coastal kill chain.

<color=#00a8ff>MISSION</color>

Preserve at least five of the six logistics ships. Destroy at least six of the nine hostile surface combatants. Neutralize at least three designated coastal kill-chain nodes.

<color=#00a8ff>EXECUTION</color>

The convoy and close escorts are already committed westbound. Devastator and Dextrous lead the formation through the traffic corridor. The carrier remains in the Gulf of Oman to recover Tiger flight; Al Dhafra supports the land-based package.

Keep the auxiliaries behind the air-defense screen. Use Broadarrow and Trident to classify surface contacts, then engage from standoff range. Lancer and Wildcat are the shore-strike elements and require manual positive-control target designation. Do not repeat the close FAC engagement from the earlier solo run.

<color=#00a8ff>ROE</color>

Engage hostile aircraft, missiles, and designated attacking surface units. Shore attack is limited to Bastion 1, Bastion 2, Bastion 3, S-300 Site North, and Coastwatch 1.""")
    SM.SetSimpleBriefing(2, 'Red is not playable in this scenario.')

    ##############################
    ### Alliance 1 - corridor force (30 assets)
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = "Fort Victoria AOR"
    unit.unitName = "RFA Fort Victoria"
    unit.SetPosition(25.380000, 58.080000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm Mark 149-4", 120)
    SM.SetUnitLauncherItem(unit.unitName, 1, "20mm Mark 149-4", 120)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Henry J Kaiser"
    unit.unitName = "USNS John Ericsson"
    unit.SetPosition(25.410000, 58.016000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 14.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Lewis and Clark"
    unit.unitName = "USNS Amelia Earhart"
    unit.SetPosition(25.440000, 57.952000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 14.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Fort Victoria AOR"
    unit.unitName = "RFA Tidespring"
    unit.SetPosition(25.470000, 57.888000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 13.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "20mm Mark 149-4", 120)
    SM.SetUnitLauncherItem(unit.unitName, 1, "20mm Mark 149-4", 120)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Henry J Kaiser"
    unit.unitName = "USNS Guadalupe"
    unit.SetPosition(25.500000, 57.824000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 14.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Lewis and Clark"
    unit.unitName = "USNS Cesar Chavez"
    unit.SetPosition(25.530000, 57.760000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 14.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Arleigh Burke IIA DDGHM"
    unit.unitName = "USS Mason"
    unit.SetPosition(25.560000, 57.696000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 20.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-174A", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-156", 12)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RUM-139 Mod4 ASROC", 6)
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
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Ticonderoga CG Baseline 4"
    unit.unitName = "USS Chosin"
    unit.SetPosition(25.590000, 57.632000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 20.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-174A", 24)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-156", 24)
    SM.SetUnitLauncherItem(unit.unitName, 2, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 3, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, "127mm mk 127 HE-CVT mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 7, "127mm mk 127 HE-CVT mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Mk-54", 3)
    SM.SetUnitLauncherItem(unit.unitName, 9, "Mk-54", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Arleigh Burke IIA DDGHM"
    unit.unitName = "USS Thomas Hudner"
    unit.SetPosition(25.620000, 57.568000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-174A", 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-156", 12)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RUM-139 Mod4 ASROC", 6)
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
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Arleigh Burke III DDGHM"
    unit.unitName = "USS Arleigh Burke"
    unit.SetPosition(25.650000, 57.504000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RIM-174A", 16)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RIM-162B", 64)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RUM-139 Mod4 ASROC", 8)
    SM.SetUnitLauncherItem(unit.unitName, 3, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 5, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 7, "127mm mk 127 HE-CVT mk 67", 20)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Mk-54", 3)
    SM.SetUnitLauncherItem(unit.unitName, 9, "Mk-54", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Type 45 DDG"
    unit.unitName = "HMS Diamond"
    unit.SetPosition(25.680000, 57.440000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 21.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "ASTER 30", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "ASTER 15", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 3, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, "114mm N4A1 HE", 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Type 23 FF"
    unit.unitName = "HMS Richmond"
    unit.SetPosition(25.710000, 57.376000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 20.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Sea Wolf", 6)
    SM.SetUnitLauncherItem(unit.unitName, 1, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "RGM-84F Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "114mm N4A1 HE", 16)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm/75 GCM-AO3-2 HE", 83)
    SM.SetUnitLauncherItem(unit.unitName, 5, "30mm/75 GCM-AO3-2 HE", 83)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Stingray", 3)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Stingray", 3)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Cyclone PBFM"
    unit.unitName = "USS Tempest"
    unit.SetPosition(25.740000, 57.312000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 22.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 450)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 450)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".50 cal bullet", 450)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".50 cal bullet", 450)
    SM.SetUnitLauncherItem(unit.unitName, 4, "25mm APDS", 250)
    SM.SetUnitLauncherItem(unit.unitName, 5, "25mm APDS", 250)
    SM.SetUnitLauncherItem(unit.unitName, 6, "FIM-92 Stinger", 4)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Legend WMSL"
    unit.unitName = "USCGC Stone"
    unit.SetPosition(25.770000, 57.248000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 19.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 400)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 400)
    SM.SetUnitLauncherItem(unit.unitName, 2, ".50 cal bullet", 400)
    SM.SetUnitLauncherItem(unit.unitName, 3, ".50 cal bullet", 400)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm mark 244-0 ELC", 97)
    SM.SetUnitLauncherItem(unit.unitName, 5, "57mm HE", 100)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Avenger MCM"
    unit.unitName = "USS Devastator"
    unit.SetPosition(25.800000, 57.184000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 10.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Avenger MCM"
    unit.unitName = "USS Dextrous"
    unit.SetPosition(25.830000, 57.120000, 0.000000)
    unit.heading = 285.000000
    unit.speed = 10.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, ".50 cal bullet", 600)
    SM.SetUnitLauncherItem(unit.unitName, 1, ".50 cal bullet", 600)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 3.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.420000, 56.380000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.400000, 55.780000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(26.380000, 55.760000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "CVN-77 (Nimitz) USS George H.W. Bush"
    unit.unitName = "USS George H.W. Bush"
    unit.SetPosition(25.300000, 58.150000, 0.000000)
    unit.heading = 305.000000
    unit.speed = 12.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("ShipDefense", 4.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Airstrip(USA)"
    unit.unitName = "Al Dhafra Air Base"
    unit.SetPosition(24.248000, 54.547000, 20.000000)
    unit.heading = 130.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 400000)
    SM.AddToUnitMagazine(unit.unitName, "AIM-120D", 96)
    SM.AddToUnitMagazine(unit.unitName, "AIM-9X", 64)
    SM.AddToUnitMagazine(unit.unitName, "GBU-39 SDB", 128)
    SM.AddToUnitMagazine(unit.unitName, "GBU-31A(v)2", 48)
    SM.AddToUnitMagazine(unit.unitName, "Chaff-1", 960)
    SM.AddToUnitMagazine(unit.unitName, "Flare-1", 960)
    UI.AddTask("Ground1", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 1"
    unit.SetPosition(25.950000, 58.050000, 7800.000000)
    unit.heading = 285.000000
    unit.speed = 360.000000
    unit.throttle = 0.720000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.050000, 57.300000, 8200.000000, 380.000000)
    UI.add_waypoint_advanced(26.300000, 56.750000, 8200.000000, 380.000000)
    UI.add_waypoint_advanced(26.050000, 57.300000, 8200.000000, 380.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "F/A-18F"
    unit.unitName = "Tiger 2"
    unit.SetPosition(25.870000, 58.120000, 7800.000000)
    unit.heading = 285.000000
    unit.speed = 360.000000
    unit.throttle = 0.720000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "1400 liter tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 6, "20mm PGU", 46)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 25)
    SM.SetUnitLauncherItem(unit.unitName, 8, "Flare-1", 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.050000, 57.300000, 8200.000000, 380.000000)
    UI.add_waypoint_advanced(26.300000, 56.750000, 8200.000000, 380.000000)
    UI.add_waypoint_advanced(26.050000, 57.300000, 8200.000000, 380.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Lancer 1"
    unit.SetPosition(24.950000, 55.200000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 390.000000
    unit.throttle = 0.720000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.650000, 56.950000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(26.550000, 56.350000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(24.600000, 54.900000, 6000.000000, 360.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Lancer 2"
    unit.SetPosition(24.880000, 55.280000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 390.000000
    unit.throttle = 0.720000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.650000, 56.950000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(26.550000, 56.350000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(24.600000, 54.900000, 6000.000000, 360.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper 1"
    unit.SetPosition(25.400000, 57.300000, 8600.000000)
    unit.heading = 285.000000
    unit.speed = 380.000000
    unit.throttle = 0.720000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "600 gallon tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.900000, 57.500000, 8600.000000, 380.000000)
    UI.add_waypoint_advanced(26.200000, 56.900000, 8600.000000, 380.000000)
    UI.add_waypoint_advanced(25.900000, 57.500000, 8600.000000, 380.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Viper 2"
    unit.SetPosition(25.320000, 57.380000, 8600.000000)
    unit.heading = 285.000000
    unit.speed = 380.000000
    unit.throttle = 0.720000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "600 gallon tank", 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AIM-120D", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "AIM-9X", 2)
    SM.SetUnitLauncherItem(unit.unitName, 4, "AIM-120D", 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Flare-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Chaff-1", 120)
    SM.SetUnitLauncherItem(unit.unitName, 8, "20mm PGU", 46)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.900000, 57.500000, 8600.000000, 380.000000)
    UI.add_waypoint_advanced(26.200000, 56.900000, 8600.000000, 380.000000)
    UI.add_waypoint_advanced(25.900000, 57.500000, 8600.000000, 380.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Wildcat 1"
    unit.SetPosition(25.180000, 56.150000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 390.000000
    unit.throttle = 0.720000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.650000, 56.950000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(26.550000, 56.350000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(24.600000, 54.900000, 6000.000000, 360.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "F-15E"
    unit.unitName = "Wildcat 2"
    unit.SetPosition(25.100000, 56.220000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 390.000000
    unit.throttle = 0.720000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.650000, 56.950000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(26.550000, 56.350000, 7600.000000, 390.000000)
    UI.add_waypoint_advanced(24.600000, 54.900000, 6000.000000, 360.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "P-8 MPA"
    unit.unitName = "Broadarrow"
    unit.SetPosition(26.250000, 58.050000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 280.000000
    unit.throttle = 0.580000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-84D Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AN/AAQ-24 Nemesis Laser Beam", 100)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.100000, 57.500000, 7600.000000, 280.000000)
    UI.add_waypoint_advanced(25.950000, 56.950000, 7600.000000, 280.000000)
    UI.add_waypoint_advanced(25.700000, 57.600000, 7600.000000, 280.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "P-8 MPA"
    unit.unitName = "Trident"
    unit.SetPosition(25.950000, 58.250000, 7600.000000)
    unit.heading = 285.000000
    unit.speed = 280.000000
    unit.throttle = 0.580000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, "Mk-46 Mod5", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "AGM-84D Harpoon", 4)
    SM.SetUnitLauncherItem(unit.unitName, 5, "AN/AAQ-24 Nemesis Laser Beam", 100)
    SM.SetUnitLauncherItem(unit.unitName, 6, "Chaff-1", 30)
    SM.SetUnitLauncherItem(unit.unitName, 7, "Flare-1", 30)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.100000, 57.500000, 7600.000000, 280.000000)
    UI.add_waypoint_advanced(25.950000, 56.950000, 7600.000000, 280.000000)
    UI.add_waypoint_advanced(25.700000, 57.600000, 7600.000000, 280.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "E-2D"
    unit.unitName = "Sentinel"
    unit.SetPosition(25.300000, 58.200000, 8500.000000)
    unit.heading = 285.000000
    unit.speed = 260.000000
    unit.throttle = 0.550000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.400000, 57.900000, 8500.000000, 260.000000)
    UI.add_waypoint_advanced(25.200000, 58.300000, 8500.000000, 260.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "KC-135R"
    unit.unitName = "Shell 1"
    unit.SetPosition(25.100000, 58.450000, 9000.000000)
    unit.heading = 285.000000
    unit.speed = 300.000000
    unit.throttle = 0.540000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(25.200000, 58.000000, 9000.000000, 300.000000)
    UI.add_waypoint_advanced(25.000000, 58.500000, 9000.000000, 300.000000)
    UI.SetNavLoopState(True)

    ##############################
    ### Alliance 2 - exclusion force (24 assets)
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Khanjar"
    unit.SetPosition(26.420000, 56.380000, 0.000000)
    unit.heading = 300.000000
    unit.speed = 24.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 40)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 20)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Falakhon"
    unit.SetPosition(26.419000, 56.395000, 0.000000)
    unit.heading = 305.000000
    unit.speed = 18.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 24)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 12)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Dagger"
    unit.SetPosition(26.417000, 56.410000, 0.000000)
    unit.heading = 135.000000
    unit.speed = 26.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 40)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 20)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Scimitar"
    unit.SetPosition(26.415000, 56.425000, 0.000000)
    unit.heading = 140.000000
    unit.speed = 26.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 40)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 20)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Kaman FACM"
    unit.unitName = "Zolfaghar"
    unit.SetPosition(26.413000, 56.440000, 0.000000)
    unit.heading = 145.000000
    unit.speed = 25.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "RGM-84A Harpoon", 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, "76mm HE-MOM", 40)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 20)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Moudge FFG"
    unit.unitName = "IRIS Sahand"
    unit.SetPosition(26.411000, 56.455000, 0.000000)
    unit.heading = 150.000000
    unit.speed = 20.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "76mm HC", 60)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 55)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm HE-T x2", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("ShipDefense", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Moudge FFG"
    unit.unitName = "IRIS Dena"
    unit.SetPosition(26.409000, 56.470000, 0.000000)
    unit.heading = 155.000000
    unit.speed = 20.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "76mm HC", 60)
    SM.SetUnitLauncherItem(unit.unitName, 1, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, "Noor", 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, "40mm HE-T", 55)
    SM.SetUnitLauncherItem(unit.unitName, 4, "20mm HE-T x2", 50)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("ShipDefense", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Pr 205ER Tsunami (Iran)"
    unit.unitName = "Tsunami 1"
    unit.SetPosition(26.406000, 56.490000, 0.000000)
    unit.heading = 105.000000
    unit.speed = 25.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-20M Rubezh", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm OF-83 HE-FRAG", 250)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm OF-83 HE-FRAG", 250)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Pr 205ER Tsunami (Iran)"
    unit.unitName = "Tsunami 2"
    unit.SetPosition(26.403000, 56.510000, 0.000000)
    unit.heading = 110.000000
    unit.speed = 25.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-20M Rubezh", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "30mm OF-83 HE-FRAG", 250)
    SM.SetUnitLauncherItem(unit.unitName, 2, "30mm OF-83 HE-FRAG", 250)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ship1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.400000, 56.520000, 0.000000, 0.000000)
    UI.add_waypoint_advanced(25.860000, 57.060000, 0.000000, 0.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "K-300P Bastion-P"
    unit.unitName = "Bastion 1"
    unit.SetPosition(26.835440, 56.333700, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-800 Oniks", 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "K-300P Bastion-P"
    unit.unitName = "Bastion 2"
    unit.SetPosition(26.880000, 56.398544, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-800 Oniks", 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "K-300P Bastion-P"
    unit.unitName = "Bastion 3"
    unit.SetPosition(27.052409, 56.483620, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "P-800 Oniks", 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Pantsir-S1"
    unit.unitName = "Pantsir 1"
    unit.SetPosition(26.834632, 56.338093, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm 3UBR8 APDS", 400)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("PointDefense", 3.000000, 3)
    UI.AddTask("AutoAttack", 4.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Pantsir-S1"
    unit.unitName = "Pantsir 2"
    unit.SetPosition(26.870324, 56.399035, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm 3UBR8 APDS", 400)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("PointDefense", 3.000000, 3)
    UI.AddTask("AutoAttack", 4.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Pantsir-S1"
    unit.unitName = "Pantsir 3"
    unit.SetPosition(27.053302, 56.482007, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 3, "95Ya6", 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, "30mm 3UBR8 APDS", 400)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("PointDefense", 3.000000, 3)
    UI.AddTask("AutoAttack", 4.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "S-300PMU-2"
    unit.unitName = "S-300 Site North"
    unit.SetPosition(27.036039, 56.865368, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, "48N6E2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, "48N6E2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, "48N6E2", 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, "48N6E2", 4)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("PointDefense", 3.000000, 3)
    UI.AddTask("AutoAttack", 4.000000, 0)

    unit = SM.GetDefaultUnit()
    unit.className = "Generic Radar Post 170"
    unit.unitName = "Coastwatch 1"
    unit.SetPosition(26.792083, 56.078986, 10.000000)
    unit.heading = 180.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.SetSensorState(0, 1)
    UI.AddTask("Ground1", 2.000000, 3)
    UI.AddTask("PointDefense", 3.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "Airstrip"
    unit.unitName = "Bandar Abbas Strip"
    unit.SetPosition(27.080000, 56.980000, 12.000000)
    unit.heading = 90.000000
    unit.speed = 0.000000
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine(unit.unitName, "Fuel", 250000)
    SM.AddToUnitMagazine(unit.unitName, "R-27R", 48)
    SM.AddToUnitMagazine(unit.unitName, "R-73", 48)
    SM.AddToUnitMagazine(unit.unitName, "Kh-59MK", 24)
    SM.AddToUnitMagazine(unit.unitName, "Chaff-1", 480)
    SM.AddToUnitMagazine(unit.unitName, "Flare-1", 480)
    UI.AddTask("Ground1", 2.000000, 3)

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum 1"
    unit.SetPosition(26.850000, 56.850000, 7800.000000)
    unit.heading = 165.000000
    unit.speed = 410.000000
    unit.throttle = 0.780000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.200000, 57.050000, 7800.000000, 410.000000)
    UI.add_waypoint_advanced(26.850000, 56.850000, 7800.000000, 410.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum 2"
    unit.SetPosition(26.920000, 56.780000, 7800.000000)
    unit.heading = 168.000000
    unit.speed = 410.000000
    unit.throttle = 0.780000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.200000, 57.050000, 7800.000000, 410.000000)
    UI.add_waypoint_advanced(26.850000, 56.850000, 7800.000000, 410.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum 3"
    unit.SetPosition(27.000000, 56.720000, 8200.000000)
    unit.heading = 172.000000
    unit.speed = 410.000000
    unit.throttle = 0.780000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.200000, 57.050000, 7800.000000, 410.000000)
    UI.add_waypoint_advanced(26.850000, 56.850000, 7800.000000, 410.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "MiG-29"
    unit.unitName = "Fulcrum 4"
    unit.SetPosition(27.060000, 56.650000, 8200.000000)
    unit.heading = 175.000000
    unit.speed = 410.000000
    unit.throttle = 0.780000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.200000, 57.050000, 7800.000000, 410.000000)
    UI.add_waypoint_advanced(26.850000, 56.850000, 7800.000000, 410.000000)
    UI.SetNavLoopState(True)

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer 1"
    unit.SetPosition(26.950000, 56.650000, 6200.000000)
    unit.heading = 150.000000
    unit.speed = 420.000000
    unit.throttle = 0.800000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.250000, 57.200000, 6200.000000, 420.000000)
    UI.add_waypoint_advanced(25.650000, 57.550000, 6200.000000, 420.000000)
    UI.add_waypoint_advanced(27.000000, 56.600000, 6200.000000, 420.000000)

    unit = SM.GetDefaultUnit()
    unit.className = "Su-24M"
    unit.unitName = "Fencer 2"
    unit.SetPosition(27.000000, 56.580000, 6200.000000)
    unit.heading = 152.000000
    unit.speed = 420.000000
    unit.throttle = 0.800000
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
    UI.AddTask("Aircraft1", 2.000000, 3)
    UI.AddTask("AutoAttack", 3.000000, 0)
    UI.AddTask("AirEvade", 4.000000, 3)
    UI.AddTask("Nav", 1.000000, 0)
    UI.add_waypoint_advanced(26.250000, 57.200000, 6200.000000, 420.000000)
    UI.add_waypoint_advanced(25.650000, 57.550000, 6200.000000, 420.000000)
    UI.add_waypoint_advanced(27.000000, 56.600000, 6200.000000, 420.000000)

    ##############################
    ### Goals
    ##############################

    goal_temp = SM.ProtectGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.AddTarget('RFA Tidespring')
    goal_temp.AddTarget('USNS Guadalupe')
    goal_temp.AddTarget('USNS Cesar Chavez')
    goal_temp.SetQuantity(5)
    goal_blue_protect = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Khanjar')
    goal_temp.AddTarget('Falakhon')
    goal_temp.AddTarget('Dagger')
    goal_temp.AddTarget('Scimitar')
    goal_temp.AddTarget('Zolfaghar')
    goal_temp.AddTarget('IRIS Sahand')
    goal_temp.AddTarget('IRIS Dena')
    goal_temp.AddTarget('Tsunami 1')
    goal_temp.AddTarget('Tsunami 2')
    goal_temp.SetQuantity(6)
    goal_blue_surface = goal_temp

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('Bastion 1')
    goal_temp.AddTarget('Bastion 2')
    goal_temp.AddTarget('Bastion 3')
    goal_temp.AddTarget('S-300 Site North')
    goal_temp.AddTarget('Coastwatch 1')
    goal_temp.SetQuantity(3)
    goal_blue_shore = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_blue_protect)
    goal_temp.AddGoal(goal_blue_surface)
    goal_temp.AddGoal(goal_blue_shore)
    SM.SetAllianceGoal(1, goal_temp)

    goal_temp = SM.DestroyGoal('')
    goal_temp.AddTarget('RFA Fort Victoria')
    goal_temp.AddTarget('USNS John Ericsson')
    goal_temp.AddTarget('USNS Amelia Earhart')
    goal_temp.AddTarget('RFA Tidespring')
    goal_temp.AddTarget('USNS Guadalupe')
    goal_temp.AddTarget('USNS Cesar Chavez')
    goal_temp.SetQuantity(3)
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)
    SM.SetAllianceROEByType(2, 2, 2, 2, 2)
