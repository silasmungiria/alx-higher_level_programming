#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

const myObject = {
  type: 'object',
  value: 12
};
// This line creates a constant variable "myObject" and initializes it with,
//  an object containing properties "type" and "value".

console.log(myObject);
// This line outputs the content of the "myObject" to the console.

myObject.value = 89;
// This line updates the value of the "value" property in the "myObject" to 89.

console.log(myObject);
// This line outputs the updated content of the "myObject" to the console.
