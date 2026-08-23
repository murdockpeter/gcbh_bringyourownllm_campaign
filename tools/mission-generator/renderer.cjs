'use strict';

const { assertApprovedGoals } = require('./objectives.cjs');

const q = (value) => JSON.stringify(value);
const f = (value) => Number(value).toFixed(6);

function safeTriple(value) {
  return String(value).replace(/"""/g, '\\"\\"\\"');
}

function renderUnit(unit, alliance) {
  const lines = [
    '    unit = SM.GetDefaultUnit()',
    `    unit.className = ${q(unit.platform_class)}`,
    `    unit.unitName = ${q(unit.unit_name)}`,
    `    unit.SetPosition(${f(unit.position.lat)}, ${f(unit.position.lon)}, ${f(unit.position.altitude || 0)})`,
    `    unit.heading = ${f(unit.heading)}`,
    `    unit.speed = ${f(unit.speed)}`,
    '    unit.cost = 0.0',
    `    SM.AddUnitToAlliance(unit, ${alliance})`,
  ];
  if (unit.alwaysVisible) lines.push('    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)');
  for (const launcher of unit.launchers) {
    lines.push(`    SM.SetUnitLauncherItem(unit.unitName, ${launcher.launcherId}, ${q(launcher.item)}, ${launcher.quantity})`);
  }
  lines.push('    UI = SM.GetUnitInterface(unit.unitName)');
  lines.push(`    UI.SetFuelFraction(${f(unit.fuelFraction)})`);
  if (['air_defense', 'coastal_strike', 'reconnaissance', 'maritime_patrol', 'fighter', 'strike'].includes(unit.role)) lines.push('    UI.SetAllSensorState(1)');
  for (const magazine of unit.magazines) lines.push(`    SM.AddToUnitMagazine(unit.unitName, ${q(magazine.item)}, ${magazine.quantity})`);
  unit.tasks.forEach((task, index) => lines.push(`    UI.AddTask(${q(task)}, ${f(index + 1)}, ${task === 'AutoAttack' ? 0 : 3})`));
  for (const point of unit.route) {
    lines.push(`    UI.add_waypoint_advanced(${f(point.lat)}, ${f(point.lon)}, ${f(point.altitude || 0)}, ${f(point.speed || unit.speed)})`);
  }
  if (unit.navLoop) lines.push('    UI.SetNavLoopState(True)');
  return lines.join('\n');
}

function flightDeckLoadout(unit) {
  const totals = new Map();
  for (const launcher of unit.launchers) totals.set(launcher.item, (totals.get(launcher.item) || 0) + launcher.quantity);
  return [...totals.entries()].sort(([left], [right]) => left.localeCompare(right)).map(([item, quantity]) => `${quantity} ${item};`).join('');
}

function renderStagedUnit(unit) {
  const lines = [
    `    # ${unit.presence.toUpperCase()}: ${unit.unit_name}`,
    `    SM.AddUnitToFlightDeck(${q(unit.host)}, ${q(unit.platform_class)}, ${q(unit.unit_name)}, ${unit.flightDeckLocation})`,
  ];
  const loadout = flightDeckLoadout(unit);
  if (loadout) lines.push(`    SM.SetFlightDeckUnitLoadout(${q(unit.host)}, ${q(unit.unit_name)}, ${q(loadout)})`);
  return lines.join('\n');
}

function renderSide(units, alliance) {
  const active = units.filter((unit) => !['staged', 'maintenance'].includes(unit.presence));
  const staged = units.filter((unit) => ['staged', 'maintenance'].includes(unit.presence));
  return [...active.map((unit) => renderUnit(unit, alliance)), ...staged.map(renderStagedUnit)].join('\n\n');
}

function renderSimpleGoal(goal, variable) {
  const lines = [`    goal_temp = SM.${goal.type}('')`];
  for (const target of goal.targets) lines.push(`    goal_temp.AddTarget(${q(target)})`);
  lines.push(`    goal_temp.SetQuantity(${goal.quantity})`, `    ${variable} = goal_temp`);
  return lines.join('\n');
}

function renderAllianceGoal(goal, alliance, prefix) {
  assertApprovedGoals(goal);
  if (goal.type !== 'CompoundGoal') {
    return `${renderSimpleGoal(goal, `${prefix}_goal`)}\n    SM.SetAllianceGoal(${alliance}, ${prefix}_goal)`;
  }
  const lines = [];
  goal.goals.forEach((child, index) => lines.push(renderSimpleGoal(child, `${prefix}_${index}`)));
  lines.push(`    goal_temp = SM.CompoundGoal(${goal.mode || 0})`);
  goal.goals.forEach((_, index) => lines.push(`    goal_temp.AddGoal(${prefix}_${index})`));
  lines.push(`    SM.SetAllianceGoal(${alliance}, goal_temp)`);
  return lines.join('\n');
}

function objectiveSentence(goal) {
  if (goal.type === 'CompoundGoal') return goal.goals.map(objectiveSentence).join(' Also ');
  const verb = goal.type === 'ProtectGoal' ? 'Preserve' : 'Neutralize';
  return `${verb} at least ${goal.quantity} of: ${goal.targets.join(', ')}.`;
}

function briefing(side, seed, archetype, objectives, balance) {
  const intent = side === 'blue' ? seed.blue_intent : seed.red_intent;
  const goal = side === 'blue' ? objectives.blue : objectives.red;
  const constraints = seed.escalation_constraints.length ? seed.escalation_constraints.join(' ') : 'Apply force only as required by the mission.';
  return `<color=#00a8ff>SITUATION</color>\n\n${seed.premise}\n\n<color=#00a8ff>MISSION</color>\n\n${objectiveSentence(goal)}\n\n<color=#00a8ff>EXECUTION</color>\n\n${intent || archetype.playerProblem}\n\n<color=#00a8ff>ROE</color>\n\n${constraints}\n\n<color=#00a8ff>ASSESSMENT</color>\n\nGenerated difficulty ratio: ${balance.ratio}.`;
}

function localDateParts(iso) {
  const match = String(iso).match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);
  if (!match) throw new Error(`Invalid date-time: ${iso}`);
  return match.slice(1).map(Number);
}

function renderScenario(model) {
  const [year, month, day, hour, minute, second] = localDateParts(model.seed.date_time);
  const units = [...model.units.blue, ...model.units.red];
  const description = `${model.seed.premise}\n\nMission archetype: ${model.archetype.label}. This scenario was generated from campaign turn ${model.state.turn} with deterministic seed ${model.effectiveSeed}.`;
  const dateLabel = new Intl.DateTimeFormat('en-US', { month: 'long', year: 'numeric', timeZone: 'UTC' }).format(new Date(Date.UTC(year, month - 1, 1)));
  return `# Scenario version: 0.2.1
# Generated by Mission Generator v2; RNG seed: ${model.effectiveSeed}
from math import *


def ScenarioInfo():
    d = dict()
    d['name'] = ${q(model.seed.scenario_name)}
    d['description'] = """${safeTriple(description)}"""
    d['author'] = 'Mission Generator v2'
    d['playableSides'] = ${q(model.seed.playable_side === 'blue' ? 'Blue' : 'Red')}
    d['thumb'] = 'ships3.png'
    d['date'] = ${q(dateLabel)}
    d['unitCount'] = ${units.length}
    d['scenarioId'] = ${q(model.seed.scenario_id)}
    return d


def CreateScenario(SM):
    SM.SetScenarioInfo(ScenarioInfo())

    SM.CreateAlliance(1, 'Blue')
    SM.AddAllianceCountry(1, 'Blue')
    SM.AddAllianceCountry(1, 'USA')
    SM.AddAllianceCountry(1, 'UK')
    SM.SetAlliancePlayable(1, ${model.seed.playable_side === 'blue' ? 1 : 0})

    SM.CreateAlliance(2, 'Red')
    SM.AddAllianceCountry(2, 'Red')
    SM.AddAllianceCountry(2, 'Iran')
    SM.SetAlliancePlayable(2, ${model.seed.playable_side === 'red' ? 1 : 0})

    SM.SetAllianceRelationship(1, 2, 'Hostile')
    SM.SetUserAlliance(${model.seed.playable_side === 'blue' ? 1 : 2})
    SM.SetDateTime(${year}, ${month}, ${day}, ${hour}, ${minute}, ${second})
    SM.SetSeaState(${model.seed.sea_state})
    SM.SetSVP(${q(model.seed.svp)})

    SM.SetSimpleBriefing(1, """${safeTriple(briefing('blue', model.seed, model.archetype, model.objectives, model.balance))}""")
    SM.SetSimpleBriefing(2, """${safeTriple(briefing('red', model.seed, model.archetype, model.objectives, model.balance))}""")

    ##############################
    ### Alliance 1 - BLUE
    ##############################

${renderSide(model.units.blue, 1)}

    ##############################
    ### Alliance 2 - RED
    ##############################

${renderSide(model.units.red, 2)}

    ##############################
    ### Goals
    ##############################

${renderAllianceGoal(model.objectives.blue, 1, 'blue')}

${renderAllianceGoal(model.objectives.red, 2, 'red')}

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)
    SM.SetAllianceROEByType(2, 2, 2, 2, 2)
`;
}

module.exports = { safeTriple, renderUnit, renderStagedUnit, renderSide, renderAllianceGoal, objectiveSentence, briefing, localDateParts, renderScenario };
