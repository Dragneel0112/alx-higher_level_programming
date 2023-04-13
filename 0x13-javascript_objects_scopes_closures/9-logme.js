#!/usr/bin/node
/* Function that logs arguments
 * prints number of args already printed
 * and the new arg value */
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count = count + 1;
};
