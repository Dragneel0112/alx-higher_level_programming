#!/usr/bin/node
// Exports function that increments and calls function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
