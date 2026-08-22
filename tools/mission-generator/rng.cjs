'use strict';

const crypto = require('node:crypto');

function canonicalize(value) {
  if (Array.isArray(value)) return value.map(canonicalize);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, canonicalize(value[key])]));
  }
  return value;
}

function canonicalJson(value) {
  return JSON.stringify(canonicalize(value));
}

function hashValue(value) {
  return crypto.createHash('sha256').update(canonicalJson(value)).digest('hex');
}

function seedToUint32(seed) {
  const digest = crypto.createHash('sha256').update(String(seed)).digest();
  return digest.readUInt32LE(0) || 0x9e3779b9;
}

function createRng(seed) {
  let state = seedToUint32(seed);
  const draws = [];
  function next(label = 'unlabelled') {
    state += 0x6d2b79f5;
    let value = state;
    value = Math.imul(value ^ (value >>> 15), value | 1);
    value ^= value + Math.imul(value ^ (value >>> 7), value | 61);
    const result = ((value ^ (value >>> 14)) >>> 0) / 4294967296;
    draws.push({ index: draws.length, label, value: Number(result.toFixed(12)) });
    return result;
  }
  function integer(minimum, maximum, label) {
    if (!Number.isInteger(minimum) || !Number.isInteger(maximum) || maximum < minimum) {
      throw new RangeError('Invalid RNG integer range');
    }
    return minimum + Math.floor(next(label) * (maximum - minimum + 1));
  }
  function pick(values, label) {
    if (!values.length) return undefined;
    return values[integer(0, values.length - 1, label)];
  }
  function shuffle(values, label = 'shuffle') {
    const result = [...values];
    for (let index = result.length - 1; index > 0; index -= 1) {
      const other = integer(0, index, `${label}:${index}`);
      [result[index], result[other]] = [result[other], result[index]];
    }
    return result;
  }
  return { seed: String(seed), next, integer, pick, shuffle, draws };
}

module.exports = { canonicalize, canonicalJson, hashValue, createRng };
