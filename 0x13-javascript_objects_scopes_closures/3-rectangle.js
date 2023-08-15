#!/usr/bin/node

// This line specifies the path to the interpreter for the script.

class Rectangle {
  constructor (w, h) {
    // This is the constructor of the Rectangle class.
    // It checks if both width (w) and height (h) are greater than 0 before assigning them.
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // This method prints a representation of the rectangle using 'X' characters.
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
// Export the Rectangle class for use in other modules.
