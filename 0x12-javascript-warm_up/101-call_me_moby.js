#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

exports.callMeMoby = function (x, theFunction) {
  // This line exports a function named "callMeMoby" that takes two,
  // parameters: "x" and "theFunction".

  for (let i = 0; i < x; i++) {
    // This loop will iterate "x" times.
    theFunction();
    // In each iteration, the "theFunction" parameter (a function) is called.
  }
};
// This function allows you to call the provided function "x" times.
