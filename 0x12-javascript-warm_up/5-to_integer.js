#!/usr/bin/nodejs
'use strict';
let arg = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(arg))
	console.log("Not a number");
else
	console.log("My number:", arg);
