#!/usr/bin/node
// prints a square of x size

const x = process.argv[2]; // store square size
let intX; // store x converted to int

// handle no x or x can't be converted to int
if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing size');
} else { // else convert x to int and print square
  intX = parseInt(x);
  for (let i = 0; i < intX; i++) { // handles rows
    let row = '';
    // handles columns
    for (let j = 0; j < intX; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
