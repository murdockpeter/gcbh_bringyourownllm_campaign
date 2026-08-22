'use strict';

const { GeneratorError } = require('./errors.cjs');

const ARCHETYPES = Object.freeze({
  convoy_escort: {
    label: 'Convoy Escort', protectRoles: ['logistics'], destroyRoles: ['surface_combatant', 'coastal_strike'],
    layout: 'transit', playerProblem: 'Preserve the logistics force while crossing the hostile threat area.',
  },
  withdrawal: {
    label: 'Withdrawal', protectRoles: ['logistics', 'surface_combatant'], destroyRoles: ['surface_combatant', 'strike'],
    layout: 'egress', playerProblem: 'Extract damaged or high-value forces while containing pursuit.',
  },
  corridor_opening: {
    label: 'Corridor Opening', protectRoles: ['logistics'], destroyRoles: ['surface_combatant', 'coastal_strike', 'reconnaissance'],
    layout: 'transit', playerProblem: 'Break a bounded kill chain and open a route for follow-on forces.',
  },
  interception: {
    label: 'Interception', protectRoles: ['base', 'logistics'], destroyRoles: ['strike', 'surface_combatant'],
    layout: 'converging', playerProblem: 'Stop a hostile package before it reaches the defended force.',
  },
  limited_strike: {
    label: 'Limited Strike', protectRoles: ['strike', 'base'], destroyRoles: ['coastal_strike', 'air_defense', 'reconnaissance'],
    layout: 'strike', playerProblem: 'Neutralize designated nodes without widening the conflict.',
  },
  reconnaissance: {
    label: 'Reconnaissance', protectRoles: ['reconnaissance', 'maritime_patrol'], destroyRoles: ['fighter', 'surface_combatant'],
    layout: 'patrol', playerProblem: 'Preserve the sensing force while exposing the hostile picture.',
  },
  recovery: {
    label: 'Recovery', protectRoles: ['logistics', 'surface_combatant', 'maritime_patrol'], destroyRoles: ['surface_combatant', 'strike'],
    layout: 'recovery', playerProblem: 'Cover a vulnerable recovery force and suppress pursuers.',
  },
});

function getArchetype(name) {
  const archetype = ARCHETYPES[name];
  if (!archetype) throw new GeneratorError('ARCHETYPE_UNKNOWN', `Unknown mission archetype: ${name}`);
  return { id: name, ...archetype };
}

module.exports = { ARCHETYPES, getArchetype };
