#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

if (process.argv.length <= 3) {
  console.log('0');
  // If there are not enough command-line arguments (less than or equal to 3),
  // this line outputs '0' to the console.
} else {
  // If there are enough command-line arguments, this block of code executes.

  const arr = process.argv.slice(2).map(Number);
  // This line creates an array "arr" by slicing the command-line arguments,
  // starting from index 2 and then converting each element to a number.

  const second = arr.sort(function (a, b) { return b - a; })[1];
  // This line sorts the "arr" array in descending order and selects the second,
  // element(index 1) from the sorted array.
  // This effectively finds the second largest number among the provided,
  // command - line arguments.

  console.log(second);
  // This line outputs the value of the "second" variable,
  // (second largest number) to the console.
}
