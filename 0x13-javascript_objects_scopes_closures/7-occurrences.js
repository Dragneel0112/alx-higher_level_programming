#!/usr/bin/node
/* Function that returns the number of occurances
 * of a specific element in a list */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
