#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

const dict = require('./101-data').dict;
// Import the "dict" object from the './101-data.js' module.

const totalist = Object.entries(dict);
// Convert the "dict" object into an array of key-value pairs.

const vals = Object.values(dict);
// Get an array of all the values in the "dict" object.

const valsUniq = [...new Set(vals)];
// Remove duplicate values from the array of values to get unique values.

const newDict = {};
// Initialize an empty object to store the new dictionary.

for (const j in valsUniq) {
  // Iterate through each unique value.

  const list = [];
  // Initialize an empty list to store keys associated with the current value.

  for (const k in totalist) {
    // Iterate through each key-value pair.

    if (totalist[k][1] === valsUniq[j]) {
      // Check if the value of the current key-value pair matches the current unique value.

      list.unshift(totalist[k][0]);
      // Add the key to the beginning of the list for the current value.
    }
  }

  newDict[valsUniq[j]] = list;
  // Assign the list of keys to the new dictionary using the current unique value as the key.
}

console.log(newDict);
// Output the newly created dictionary to the console.
