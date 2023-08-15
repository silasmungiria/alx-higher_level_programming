#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

exports.nbOccurences = function (list, searchElement) {
  // This function calculates the number of occurrences of "searchElement" in the given "list".

  let nOccurrences = 0;
  // Initialize the variable "nOccurrences" to keep track of the number of occurrences.

  for (let i = 0; i < list.length; i++) {
    // Iterate through each element in the "list".
    if (searchElement === list[i]) {
      // If the current element matches the "searchElement",
      // increment the count of occurrences.
      nOccurrences++;
    }
  }

  return nOccurrences;
  // Return the total count of occurrences.
};
