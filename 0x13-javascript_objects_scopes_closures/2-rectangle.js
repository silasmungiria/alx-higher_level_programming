#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

class Rectangle {
  constructor (w, h) {
    // This is the constructor of the Rectangle class.
    // It checks if both width (w) and height (h) are greater than,
    // 0 before assigning them.
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
// Export the Rectangle class for use in other modules.
