#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

const SquareE = require('./5-square');
// Import the SquareE class from the './5-square' module.

class Square extends SquareE {
  constructor (size) {
    // This is the constructor of the Square class, which extends the SquareE class.
    // It initializes the Square with the given "size" by passing it to the parent class constructor.
    super(size);
  }

  charPrint (c) {
    // This method prints a representation of the square using the specified character 'c'.
    // If 'c' is undefined, it defaults to 'X'.
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
// Export the Square class for use in other modules.
