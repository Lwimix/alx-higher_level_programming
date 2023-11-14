#!/usr/bin/node
/*
 * This script creates a Square class that inherits from Rectangle
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let printed = 'X';
    if (c === undefined) {
      printed = 'X';
    } else { printed = c; }
    for (let i = 0; i < this.size; i++) { console.log(printed.repeat(this.size)); }
  }
}
module.exports = Square;
