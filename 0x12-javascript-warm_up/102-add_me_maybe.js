#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

exports.addMeMaybe = function (number, theFunction) {
  // This line exports a function named "addMeMaybe" that takes two,
  // parameters: "number" and "theFunction".

  theFunction(++number);
  // This line calls the "theFunction" parameter with the incremented,
  // value of "number".
  // The "++number" expression increments "number" before passing it to,
  // the "theFunction".
};
// This function increments the input number and passes it to another,
// provided function.
