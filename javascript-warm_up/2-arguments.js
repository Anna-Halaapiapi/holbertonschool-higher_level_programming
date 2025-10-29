#!/usr/bin/node
// prints a message depending of the number of arguments passed

// no args passed
if (process.argv.length === 2) {
    console.log('No argument');
}
// one arg passed
else if (process.argv.length === 3) {
    console.log('Argument found');
}
// more than one arg passed
else {
    console.log('Arguments found');
}
