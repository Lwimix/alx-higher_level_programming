#!/usr/bin/nodejs
/*
 * This script prints out a square comprising of "X"'s.
 */
'use strict';
let numTimes = parseInt(process.argv[2]); let i; let theXs = 'X';
if (process.argv[2] === undefined || isNaN(numTimes)) { console.log('Missing size'); } else
  if (numTimes <= 0) { numTimes = 0; }
theXs = theXs.repeat(numTimes);
for (i = 0; i < numTimes; i++) { console.log(theXs); }
