#!/usr/bin/node
/*
 * This script creates a Square class that inherits from Square
 */
const Square = require('./5-square');
  Square.prototype.charPrint = function(c) {
    let printed = 'X';
    if (c === undefined) {
      printed = 'X';
    } else { printed = c; }
    for (let i = 0; i < this.size; i++) { console.log(printed.repeat(this.size)); }
  }
module.exports = Square;
