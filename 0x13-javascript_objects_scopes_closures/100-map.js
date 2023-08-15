#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

const list = require('./100-data.js').list;
// Import the "list" array from the './100-data.js' module.

console.log(list);
// Output the original "list" array to the console.

console.log(list.map((item, index) => item * index));
// Output a new array resulting from applying the map function to each element of "list"
// where each element is multiplied by its index.
