export function allianceSide(allianceName = '', allianceId = null) {
  if (/blue|usa|uk|coalition/i.test(allianceName)) return 'blue';
  if (/red|iran|russia/i.test(allianceName)) return 'red';
  if (Number(allianceId) === 1) return 'blue';
  if (Number(allianceId) === 2) return 'red';
  return 'other';
}

export function visibleUnits(units = [], side = 'all') {
  if (side === 'all') return units;
  return units.filter((unit) => allianceSide(unit.allianceName, unit.allianceId) === side);
}

export function visibleFindings(findings = [], units = [], side = 'all') {
  if (side === 'all') return findings;
  const unitSides = new Map(units.map((unit) => [unit.name, allianceSide(unit.allianceName, unit.allianceId)]));
  return findings.filter((finding) => {
    const findingSide = unitSides.get(finding.unit);
    return findingSide ? findingSide === side : true;
  });
}
