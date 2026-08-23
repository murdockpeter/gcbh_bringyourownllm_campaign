'use strict';

class GeneratorError extends Error {
  constructor(code, message, details = []) {
    super(message);
    this.name = 'GeneratorError';
    this.code = code;
    this.details = Array.isArray(details) ? details : [details];
  }
}

function formatError(error) {
  if (!(error instanceof GeneratorError)) return error?.stack || String(error);
  const details = error.details.length ? `\n${error.details.map((item) => `  - ${item}`).join('\n')}` : '';
  return `[${error.code}] ${error.message}${details}`;
}

module.exports = { GeneratorError, formatError };
