#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

console.log(process.argv[2] + ' is ' + process.argv[3]);
// This line accesses command-line arguments using the "process.argv" array.
// It concatenates the value at index 2 with the string ' is ' and the value,
// at index 3, then outputs the resulting string to the console.
// This can be used to display a custom message using command-line arguments.
