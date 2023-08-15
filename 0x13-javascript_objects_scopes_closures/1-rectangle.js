#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

class Rectangle {
  constructor (w, h) {
    // This is the constructor of the Rectangle class.
    // It initializes the width and height properties based on the,
    // provided arguments.
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
// Export the Rectangle class for use in other modules.
