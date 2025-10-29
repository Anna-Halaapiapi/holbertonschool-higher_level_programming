#!/usr/bin/node
// prints two arguments passed to it, in the format: “arg1 is arg2”

let argv1, argv2;

// no args passed
if (process.argv.length === 2) {
  argv1 = 'undefined';
  argv2 = 'undefined';
}
// one arg passed
else if (process.argv.length === 3) {
  argv1 = process.argv[2];
  argv2 = 'undefined';
}

// two args passed
else if (process.argv.length === 4) {
  argv1 = process.argv[2];
  argv2 = process.argv[3];
}

// print to stdout
console.log(argv1, 'is', argv2);
