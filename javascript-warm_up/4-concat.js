#!/usr/bin/node
// prints two arguments passed to it, in the format: “arg1 is arg2”

let argv1, argv2;

if (process.argv.length === 2) { // no args passed
  argv1 = 'undefined';
  argv2 = 'undefined';
} else if (process.argv.length === 3) { // one arg passed
  argv1 = process.argv[2];
  argv2 = 'undefined';
} else if (process.argv.length === 4) { // two args passed
  argv1 = process.argv[2];
  argv2 = process.argv[3];
}

console.log(argv1, 'is', argv2); // print to stdout
