#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

exports.converter = function (base) {
  // This function returns a new function that converts a number to a string representation in the given base.

  return function (num) {
    // This inner function takes a number "num" and converts it to a string in the specified base.

    return num.toString(base);
    // Convert the number to a string representation using the specified base.
  };
};
