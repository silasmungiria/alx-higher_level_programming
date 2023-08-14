#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  // This block of code checks if the argument provided in the command line,
  // is not a number or if no argument is provided.
  // If either condition is true, it outputs 'Not a number' to the console.
} else {
  // If the conditions in the "if" statement are not met, this block,
  // of code executes.
  console.log('My number:', parseInt(process.argv[2]));
  // This line outputs the message 'My number:' followed by the parsed integer,
  // value of the command - line argument.
}
