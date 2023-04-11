#!/usr/bin/node
// Prints a square
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let x = '';
    for (let j = 0; j < num; j++) x += 'X';
    console.log(x);
  }
}
