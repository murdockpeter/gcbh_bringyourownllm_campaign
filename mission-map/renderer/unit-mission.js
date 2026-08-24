function includes(text, pattern) {
  return pattern.test(text);
}

function launcherText(unit) {
  return (unit.launcherItems || []).map((launcher) => launcher.item).join(' ').toLowerCase();
}

function mission(code, label, summary) {
  return { code, label, summary, tooltip: `Mission: ${code} — ${label}. ${summary}` };
}

export function inferUnitMission(unit) {
  const identity = `${unit.name || ''} ${unit.className || ''}`.toLowerCase();
  const weapons = launcherText(unit);
  const combined = `${identity} ${weapons} ${(unit.tasks || []).join(' ').toLowerCase()}`;

  if (includes(identity, /airstrip|air base/)) return mission('BASE', 'Aviation support', 'Hosts, recovers, rearms, and sustains aircraft.');
  if (includes(identity, /cvn-|aircraft carrier|nimitz/)) return mission('CV / C2', 'Carrier support', 'Provides aviation basing, recovery, and command support.');
  if (includes(identity, /e-2|awacs|early warning/)) return mission('AEW&C', 'Airborne early warning', 'Builds the air picture and supports battle management.');
  if (includes(identity, /kc-135|kc-10|tanker/)) return mission('AAR', 'Aerial refueling', 'Extends the endurance of the airborne package.');
  if (includes(identity, /radar post|coastwatch/)) return mission('ISR / C2', 'Surveillance and cueing', 'Detects contacts and supports the theater targeting network.');
  if (includes(identity, /pantsir|s-300|sam/)) return mission('AAW / IADS', 'Air defense', 'Defends the force or coastal network against aircraft and missiles.');
  if (includes(identity, /bastion|k-300|coastal missile/)) return mission('ASuW', 'Coastal anti-surface warfare', 'Attacks surface vessels from a shore-based missile position.');
  if (includes(identity, /avenger mcm|mine countermeasure|mcm/)) return mission('MCM', 'Mine countermeasures', 'Leads and checks the transit route for mine hazards.');
  if (includes(identity, /fort victoria|henry j kaiser|lewis and clark|aor|auxiliary|supply/)) return mission('LOG', 'Logistics support', 'Carries or transfers fuel, stores, ammunition, and sustainment cargo.');

  if (unit.domain === 'air') {
    const antiSurface = includes(weapons, /harpoon|exocet|noor|kh-59|sea eagle/);
    const antiSubmarine = includes(weapons, /mk-46|mk-50|mk-54|stingray|torpedo|sonobuoy/);
    if (includes(identity, /p-8|mpa|orion/)) {
      if (antiSurface && antiSubmarine) return mission('ASuW / ASW', 'Maritime patrol', 'Searches, classifies, and attacks surface or submarine contacts.');
      return mission(antiSubmarine ? 'ASW' : 'ASuW / ISR', 'Maritime patrol', 'Builds the maritime picture and attacks designated contacts.');
    }
    const strikeWeapons = includes(weapons, /gbu-|agm-|harm|sdb|jdam|kh-|bomb/);
    if (includes(identity, /lancer|wildcat/) && strikeWeapons) return mission('SEAD / STRIKE', 'Corridor suppression', 'Attacks designated air-defense and coastal-control targets from standoff.');
    if (strikeWeapons || includes(identity, /su-24|fencer|strike/)) return mission(antiSurface ? 'ASuW / STRIKE' : 'STRIKE', 'Strike warfare', 'Attacks designated surface or land targets.');
    if (includes(combined, /aim-|r-27|r-73|aircraft1/) || includes(identity, /f-14|f-15|f\/a-18|mig-/)) return mission('CAP', 'Combat air patrol', 'Protects the force and intercepts hostile aircraft.');
    return mission('AIR SUPPORT', 'Aviation support', 'Performs its assigned airborne support task.');
  }

  if (unit.domain === 'surface') {
    if (includes(identity, /kaman|facm|tsunami|missile boat|fast attack craft/)) return mission('ASuW', 'Surface attack', 'Intercepts, blocks, or attacks hostile surface vessels.');
    const roles = [];
    if (includes(weapons, /rim-|aster|sea wolf|stinger|sm-2|sm-3|sm-6/)) roles.push('AAW');
    if (includes(weapons, /harpoon|noor|p-20|oniks|exocet|sea skua/)) roles.push('ASuW');
    if (includes(weapons, /asroc|mk-46|mk-50|mk-54|stingray|torpedo/)) roles.push('ASW');
    if (roles.length) return mission(roles.join(' / '), roles.length > 1 ? 'Multi-mission surface combatant' : `${roles[0]} surface combatant`, 'Screens the formation and engages threats within its fitted warfare areas.');
    return mission('PATROL / ESCORT', 'Surface security', 'Screens, patrols, and responds to hostile surface contacts.');
  }

  return mission('SUPPORT', 'General support', 'Supports the assigned force within its platform capabilities.');
}
