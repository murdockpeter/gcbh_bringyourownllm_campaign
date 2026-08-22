'use strict';

const { GeneratorError } = require('./errors.cjs');

function integerRange(value, label) {
  if (!Array.isArray(value) || value.length !== 2 || !value.every(Number.isInteger) || value[1] < value[0]) {
    throw new GeneratorError('VARIATION_RANGE', `${label} must be an ascending pair of integers`);
  }
  return value;
}

function shiftLocalDateTime(value, minutes) {
  const match = String(value).match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.\d+)?(Z|[+-]\d{2}:\d{2})$/);
  if (!match) throw new GeneratorError('VARIATION_TIME', 'date_time must include seconds and a UTC offset');
  const [, year, month, day, hour, minute, second, suffix] = match;
  const shifted = new Date(Date.UTC(Number(year), Number(month) - 1, Number(day), Number(hour), Number(minute) + minutes, Number(second)));
  return shifted.toISOString().replace('Z', suffix);
}

function applyVariation(sourceSeed, rng) {
  const seed = structuredClone(sourceSeed);
  const variation = seed.variation || {};
  const applied = {};
  if (variation.time_offset_minutes !== undefined) {
    const [minimum, maximum] = integerRange(variation.time_offset_minutes, 'time_offset_minutes');
    const offset = rng.integer(minimum, maximum, 'variation:time-offset-minutes');
    seed.date_time = shiftLocalDateTime(seed.date_time, offset);
    applied.time_offset_minutes = offset;
  }
  if (variation.sea_state_range !== undefined) {
    const [minimum, maximum] = integerRange(variation.sea_state_range, 'sea_state_range');
    if (minimum < 0 || maximum > 9) throw new GeneratorError('VARIATION_RANGE', 'sea_state_range must stay between 0 and 9');
    seed.sea_state = rng.integer(minimum, maximum, 'variation:sea-state');
    applied.sea_state = seed.sea_state;
  }
  if (variation.reserve_slots) {
    for (const side of ['blue', 'red']) {
      if (variation.reserve_slots[side] === undefined) continue;
      const [minimum, maximum] = integerRange(variation.reserve_slots[side], `reserve_slots.${side}`);
      const slots = rng.integer(minimum, maximum, `variation:${side}:reserve-slots`);
      const policy = seed.force_policy[side] || (seed.force_policy[side] = {});
      if (Number.isInteger(policy.max_units)) policy.max_units += slots;
      applied[`${side}_reserve_slots`] = slots;
    }
  }
  return { seed, applied };
}

module.exports = { integerRange, shiftLocalDateTime, applyVariation };
