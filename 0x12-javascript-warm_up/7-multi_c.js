#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  // This block of code checks if the command-line argument is undefined or,
  // not a number.
  // If either condition is true, it outputs 'Missing number,
  // of occurrences' to the console.
} else {
  // If the conditions in the "if" statement are not met,
  // this block of code executes.

  const x = Number(process.argv[2]);
  // This line converts the command-line argument to a number and assigns,
  // it to the variable "x".

  let i = 0;
  // This line initializes a variable "i" to 0, which will be used as a counter.

  while (i < x) {
    // This loop will continue as long as the value of "i" is less than,
    // the value of "x".
    console.log('C is fun');
    // This line outputs the string 'C is fun' to the console.
    i++;
    // This line increments the value of "i" by 1 in each iteration.
  }
}
