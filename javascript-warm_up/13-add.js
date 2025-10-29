#!/usr/bin/node

// function that adds two ints
function add (a, b) {
    return a + b;
}
// make add visible from outside
module.exports = { add }

const add = require('./13-add').add; // import add function to test works
console.log(add(3, 5)); // print 8 to stdout
