#!/usr/bin/node
// computes and prints factorial (using recursion)

function factorial (n) {
// define base case (0, 1 or NaN)
  if (n === 0 || n === 1 || isNaN(n) === true) {
    return 1;
  }
  // recursive case: multiply current n by factorial of n
  return n * factorial(n - 1);
}

// convert passed arg to an int for calc
const num = parseInt(process.argv[2]);
// pass int to factorial function and print result
console.log(factorial(num));
