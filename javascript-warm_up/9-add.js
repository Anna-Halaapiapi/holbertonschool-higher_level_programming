#!/usr/bin/node
// prints the addition of 2 ints

// define add function
function add(a, b) {
  return a + b;
}

const x = parseInt(process.argv[2]); // first num
const y = parseInt(process.argv[3]); // second num
let sum; // stores sum of first and second nums

if (process.argv.length < 4) { // handle no args or only one arg passed
  console.log('NaN');
} else { // else sum and print numbers
  sum = add(x, y);
  console.log(sum);
}
