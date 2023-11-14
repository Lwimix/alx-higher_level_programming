#!/usr/bin/node
/*
 * This script sorts a dictionary according to id
 */
const dict = require('./101-data.js').dict;
const myDict = {}; const keys = Object.keys(dict);
for (let i = 0; i < keys.length; i++) {
  if (myDict[dict[keys[i]]]) { myDict[dict[keys[i]]].push(keys[i]); } else { myDict[dict[keys[i]]] = [].concat(keys[i]); }
}
console.log(myDict);
