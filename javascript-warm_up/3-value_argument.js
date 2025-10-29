#!/usr/bin/node
// prints the first argument passed to it

if (process.argv[2] === undefined) {
  console.log('No argument'); // handles no args passed
} else {
  console.log(process.argv[2]); // else prints first arg
}
