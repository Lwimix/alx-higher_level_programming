#!/usr/bin/nodejs
/*
 * This script prints the addition of two integers
 */
'use strict';
let firstInt = process.argv[2], secondInt = process.argv[3];
firstInt = parseInt(firstInt);
secondInt = parseInt(secondInt);
console.log(firstInt + secondInt);
