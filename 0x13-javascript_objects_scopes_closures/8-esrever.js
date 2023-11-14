#!/usr/bin/node
/*
 * This script reverses a list
 */
exports.esrever = function (list) {
  for (let i = 0, j = list.length - 1; i < j; i++, j--) { [list[j], list[i]] = [list[i], list[j]]; }
  return list;
};
