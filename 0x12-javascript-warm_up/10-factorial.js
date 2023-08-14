#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

function factorial (n) {
  // This line defines a recursive function named "factorial" that calculates,
  // the factorial of a given number "n".

  if (n < 0) {
    return (-1);
    // If "n" is negative, the function returns -1 to indicate an invalid input.
  }
  if (n === 0 || isNaN(n)) {
    return (1);
    // If "n" is 0 or not a number (NaN), the function returns 1,
    // as the factorial of 0 is 1.
  }

  return (n * factorial(n - 1));
  // If none of the above conditions apply, the function returns the,
  // product of "n" and the result of recursively calling the,
  // "factorial" function with "n - 1".
}

console.log(factorial(Number(process.argv[2])));
// This line calls the "factorial" function, passing the parsed integer value,
// of the command - line argument as its parameter,
// and outputs the result to the console.
