#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

// handles 0 or 1 args passed
if (process.argv.length < 4) {
  console.log('0');
// handles 2+ args passed
} else {
  // get only args from CLI
  const argsArr = process.argv.slice(2);
  // remove dupes
  const uniqueArr = [...new Set(argsArr)];
  // sort in descending order
  uniqueArr.sort((a, b) => b - a);
  // print second largest num
  console.log(uniqueArr[1]);
}
