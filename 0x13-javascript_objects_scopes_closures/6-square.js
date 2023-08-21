#!/usr/bin/node

const SquareE = require('./5-square');

class Square extends SquareE {
  // Class method to print the square with a specified character
  charPrint (c) {
    // If character 'c' is undefined, set it to 'X'
    if (c === undefined) {
      c = 'X';
    }
    // Loop through each row of the square's height
    for (let i = 0; i < this.height; i++) {
      let s = '';
      // Loop through each column of the square's width
      for (let j = 0; j < this.width; j++) {
        // Add the character 'c' to the current row
        s += c;
      }
      // Print the row
      console.log(s);
    }
  }
}

// Export the Square class for use in other modules
module.exports = Square;
