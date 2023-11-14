#!/usr/bin/node
/*
 * This script prints out the number of arguments already printed
 * and the new argument
 */
let numArgs = 0;
exports.logMe = function (item) {
  console.log(numArgs++ + ': ' + item);
};
