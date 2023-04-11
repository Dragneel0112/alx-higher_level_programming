#!/usr/bin/node
// Prints number found in arguments
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
