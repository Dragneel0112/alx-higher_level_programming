#!/usr/bin/node
// Prints message based on number of args
const count = process.argv.length;
if (count === 3) {
  console.log('Argument found');
} else if (count > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
