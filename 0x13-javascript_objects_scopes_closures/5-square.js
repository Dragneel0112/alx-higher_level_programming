#!/usr/bin/node
/* Creates class Square
 * Square inherits from Rectangle (4-rectangle) */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // Instantiates Square with size
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
