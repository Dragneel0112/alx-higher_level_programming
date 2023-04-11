#!/usr/bin/node
// Function adds numbers from args
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(process.argv[2], process.argv[3]);
