#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer

let intValue;

// handle no args passed
if (process.argv[2] === undefined) {
  intValue = 'Not a number';
// else convert the arg to int
} else {
  intValue = parseInt(process.argv[2]);
}
// handles converted value not a number
if (isNaN (intValue)) {
  intValue = 'Not a number';
}
// print result
console.log(intValue);
