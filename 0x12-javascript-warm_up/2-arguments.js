#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

if (process.argv.length === 2) {
  // This condition checks if there are exactly 2
  // elements in the process.argv array.
  // If true, it means no additional command-line arguments were provided
  // besides the script name.
  console.log('No argument');
  // Outputs the string 'No argument' to the console.
} else if (process.argv.length === 3) {
  // This condition checks if there are exactly 3 elements in the process.argv.
  // If true, it means one additional command-line argument was provided.
  console.log('Argument found');
  // Outputs the string 'Argument found' to the console.
} else {
  // If neither of the above conditions is met, it means
  // more than one additional command-line argument was provided.
  console.log('Arguments found');
  // Outputs the string 'Arguments found' to the console.
}
