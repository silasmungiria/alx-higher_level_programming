#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

function add (a, b) {
  // This line defines a function named "add" that takes two,
  // parameters "a" and "b".
  const c = a + b;
  // This line calculates the sum of the parameters "a" and "b" and assigns,
  // it to the variable "c".
  console.log(c);
  // This line outputs the value of the variable "c" to the console.
}

add(Number(process.argv[2]), Number(process.argv[3]));
// This line calls the "add" function, passing the parsed integer values,
// of the command - line arguments as its parameters.
