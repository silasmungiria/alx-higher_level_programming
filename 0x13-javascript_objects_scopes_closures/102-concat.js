#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

const fs = require('fs');
// Import the 'fs' module for file system operations.

const fArg = fs.readFileSync(process.argv[2]).toString();
// Read the content of the file specified by the first command-line argument,
// and convert it to a string using the 'toString' method.

const sArg = fs.readFileSync(process.argv[3]).toString();
// Read the content of the file specified by the second command-line argument,
// and convert it to a string using the 'toString' method.

fs.writeFileSync(process.argv[4], fArg + sArg);
// Write the concatenated content of the two input files to the file specified by the third command-line argument.
