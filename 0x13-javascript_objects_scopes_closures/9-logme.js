#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

let narg = 0;
// Initialize the variable "narg" to keep track of the number of function calls.

exports.logMe = function(item) {
  // This function logs the "item" along with the current value of "narg" to the console.

  console.log(narg + ': ' + item);
  // Output the concatenation of "narg" and "item" to the console.

  narg++;
  // Increment "narg" to track the number of function calls.
};
