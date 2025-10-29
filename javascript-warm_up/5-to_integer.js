#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const input = process.argv[2]; // get arg passed
let intInput; // store arg converted to int

if (input === undefined) { // handles no arg passed
  console.log('Not a number');
} else {
  intInput = parseInt(input); // convert to int
  if (isNaN(intInput) === true) { // handles conversion failure
    console.log('Not a number');
  } else {
    console.log('My number:', intInput); // handles print int to stdout
  }
}
