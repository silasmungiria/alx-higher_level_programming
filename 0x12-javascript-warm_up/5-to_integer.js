#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
  // If the command-line argument is not a number or is undefined,
  // print 'Not a number'.
} else {
  console.log('My number:', parseInt(process.argv[2]));
  // If the argument is a valid number, print 'My number:' followed by,
  // the parsed integer value.
}
