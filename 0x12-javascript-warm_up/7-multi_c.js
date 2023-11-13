#!/usr/bin/nodejs
/*
 * This script prints out "C is fun" x number of times
 * where x is an argument that can be converted to number
 */
'use strict';
let numTimes = parseInt(process.argv[2]), i;
if (process.argv[2] === undefined || isNaN(numTimes))
	console.log("Missing number of occurences");
else
	for (i = 0; i < numTimes; i++)
		console.log("C is fun");
