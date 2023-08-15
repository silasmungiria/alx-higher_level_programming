#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

let callCount = 0;
// Initialize the variable "callCount" to 0.

exports.logMe = function (item) {
  console.log(callCount + ': ' + item);
  // Print the value of "callCount" and the provided "item" to the console.

  callCount++;
  // Increment the value of "callCount" by 1 for each call.
};
