#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

exports.esrever = function (list) {
  // This function reverses the elements in the given "list".

  let len = list.length - 1;
  // Initialize the variable "len" to the last index of the list.
  let i = 0;
  // Initialize the variable "i" to 0, representing the first index.

  while ((len - i) > 0) {
    // Execute the loop as long as the remaining unswapped elements are more than 1.
    const aux = list[len];
    // Store the value of the element at the end of the list in the variable "aux".
    list[len] = list[i];
    // Replace the element at the end with the element at the start.
    list[i] = aux;
    // Replace the element at the start with the value stored in "aux".
    i++;
    // Increment "i" to move towards the center.
    len--;
    // Decrement "len" to move towards the center.
  }

  return list;
  // Return the reversed list.
};
