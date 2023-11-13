#!/usr/bin/nodejs
/*
 * This script computes and prints the factorial of
 * the first argument recursively in a function
 */
'use strict';
function factorial (num) {
  if (num < 0) { return; }
  if (num === 0 || num === 1) { return 1; } else { return num * (factorial(num - 1)); }
}
const number = parseInt(process.argv[2]);
if (isNaN(number)) { console.log(1); } else { console.log(factorial(number)); }
