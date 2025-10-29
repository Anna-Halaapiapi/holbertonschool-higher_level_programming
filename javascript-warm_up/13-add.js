#!/usr/bin/node

// function that adds two ints
function add (a, b) {
    return a + b;
}
// make add visible from outside
module.exports = { add }
