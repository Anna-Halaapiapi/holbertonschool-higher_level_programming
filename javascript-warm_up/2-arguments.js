#!/usr/bin/node
// prints a message depending of the number of arguments passed

if (process.argv.length === 2) { // no args passed
  console.log('No argument');
} else if (process.argv.length === 3) { // one arg passed
  console.log('Argument found');
} else { // more than one arg passed
  console.log('Arguments found');
}
