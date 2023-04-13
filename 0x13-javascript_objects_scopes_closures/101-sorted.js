#!/usr/bin/node
/* Imports dictionary of ocurrences by user id and computes a
 * new dictionary of user ids by ocurrence */
const dict = require('./101-data').dict;

const dictNew = {};
for (const [key, value] of Object.entries(dict)) {
  if (dictNew[value] === undefined) {
    dictNew[value] = [key];
  } else {
    dictNew[value].push(key);
  }
}
console.log(dictNew);
