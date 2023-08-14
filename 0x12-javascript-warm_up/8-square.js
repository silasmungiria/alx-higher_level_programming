#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
  // If the command-line argument is undefined or not a number, print 'Missing size'.
} else {
  const size = parseInt(process.argv[2]);
  // Convert the command-line argument to an integer and assign it to the "size" variable.

  for (let i = 0; i < size; i++) {
    // Loop through rows based on the "size".
    console.log('X'.repeat(size));
    // Print a line consisting of 'X' repeated "size" times for each row.
  }
}
