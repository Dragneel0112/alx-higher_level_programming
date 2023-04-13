#!/usr/bin/node
/* Imports an array and returns new array
 * new array consists of original values multiplied by index */
const list = require('./100-data').list;
const mulArray = list.map((val, index) => {
  return index * val;
});
console.log(list);
console.log(mulArray);
