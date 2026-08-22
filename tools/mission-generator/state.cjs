'use strict';

const { GeneratorError } = require('./errors.cjs');

function inferRole(unit, domain) {
  const text = `${unit.unit_name} ${unit.platform_class}`.toLowerCase();
  if (/airstrip|air base|carrier|cvn-/.test(text)) return 'base';
  if (/aor|kaiser|lewis and clark|victoria|logistic|supply|auxiliary/.test(text)) return 'logistics';
  if (/radar post|coastwatch|e-2/.test(text)) return 'reconnaissance';
  if (/kc-135|tanker/.test(text)) return 'tanker';
  if (/p-8|mpa/.test(text)) return 'maritime_patrol';
  if (/bastion|coastal|k-300/.test(text)) return 'coastal_strike';
  if (/pantsir|s-300|sam/.test(text)) return 'air_defense';
  if (domain === 'air' && /f-15|su-24|strike|lancer|fencer/.test(text)) return 'strike';
  if (domain === 'air') return 'fighter';
  if (domain === 'ship') return 'surface_combatant';
  if (domain === 'sub') return 'submarine';
  if (domain === 'ground') return 'ground';
  return 'support';
}

function repairHours(unit) {
  const repair = unit.repair || {};
  return Math.max(Number(repair.emergency_hours_remaining || 0), Number(repair.pier_side_hours_required || 0));
}

function eligibility(unit) {
  const reasons = [];
  if (unit.status === 'destroyed') reasons.push('status is destroyed');
  if (!unit.mission_capable) reasons.push('mission_capable is false');
  if (unit.structural_integrity_pct < 30) reasons.push('structural integrity is below 30%');
  if (repairHours(unit) > 0 && unit.status === 'under_repair') reasons.push(`repair window has ${repairHours(unit)} hours remaining`);
  return { eligible: reasons.length === 0, reasons };
}

function indexCampaign(state, database) {
  const accepted = [];
  const rejected = [];
  for (const side of ['blue', 'red']) {
    for (const unit of state.sides[side].units) {
      const platform = database.platform(unit.platform_class);
      if (!platform) {
        rejected.push({ side, unit_name: unit.unit_name, reasons: [`platform class is absent from database: ${unit.platform_class}`] });
        continue;
      }
      const availability = eligibility(unit);
      const normalized = { ...unit, side, domain: platform.domain, role: inferRole(unit, platform.domain), platform };
      if (availability.eligible) accepted.push(normalized);
      else rejected.push({ side, unit_name: unit.unit_name, reasons: availability.reasons });
    }
  }
  if (!accepted.some((unit) => unit.side === 'blue') || !accepted.some((unit) => unit.side === 'red')) {
    throw new GeneratorError('ROSTER_EMPTY', 'Both sides require at least one eligible database-backed unit');
  }
  return { accepted, rejected };
}

module.exports = { inferRole, repairHours, eligibility, indexCampaign };
