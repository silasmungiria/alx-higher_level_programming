#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

const Rectangle = require('./4-rectangle');
// Import the Rectangle class from the './4-rectangle' module.

class Square extends Rectangle {
  constructor (size) {
    // This is the constructor of the Square class, which extends the Rectangle class.
    // It initializes the Square with the given "size" by passing it to the parent class constructor.
    super(size, size);
  }
}

module.exports = Square;
// Export the Square class for use in other modules.
