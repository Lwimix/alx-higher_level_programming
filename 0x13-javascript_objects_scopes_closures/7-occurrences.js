#!/usr/bin/node
/*
 * This script prints the number of occurences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { occurences++; }
  }
  return occurences;
};
