#!/usr/bin/node
// Export functio that executes x times a function
exports.callMeMoby = function (x, theFunction) {
  for (let a = 0; a < x; a++) theFunction();
};
