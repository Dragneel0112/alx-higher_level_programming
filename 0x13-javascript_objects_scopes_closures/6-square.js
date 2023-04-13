#!/usr/bin/node
/* Creates class Square
 * Square inherits from Rectangle (4-rectangle) */
const Rectangle = require('./5-square');

class Square extends Rectangle {
  // Instantiates Square with size
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    // Method print
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
