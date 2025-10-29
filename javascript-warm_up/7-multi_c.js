#!/usr/bin/node
// prints x times 'C is fun'

const x = process.argv[2]; // stores x
let intX; // stores x converted to int

// handle no x arg passed or x can't be converted to int
if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
// else convert to int and print x times
} else {
  intX = parseInt(x);
  for (let i = 0; i < intX; i++) {
    console.log('C is fun');
  }
}
