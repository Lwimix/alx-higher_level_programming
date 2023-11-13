#!/usr/bin/nodejs
/*
 * This script returns the addition of 2 integers.
 * It uses a function that is visible from outside
 */
'use strict';
exports.add = function add(num1, num2) {
	return (num1 + num2);
}
