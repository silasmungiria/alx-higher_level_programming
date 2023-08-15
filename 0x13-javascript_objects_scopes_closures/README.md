
---

# 0x13. JavaScript - Objects, Scopes, and Closures

![JavaScript Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/240px-JavaScript-logo.png)

This repository contains solutions for a series of tasks related to JavaScript objects, scopes, and closures. The tasks aim to help you practice creating classes, working with objects, understanding closures, and more.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
- [License](#license)

## Description

This project is part of an educational exercise focusing on JavaScript programming concepts. It covers topics such as object creation, class definitions, inheritance, closures, and more. The goal is to provide you with hands-on experience in working with JavaScript's object-oriented features.

## Installation

To run and test the project, ensure you have Node.js 14.x installed. If you don't have it installed, you can follow these steps to set it up:

1. Install Node.js 14 using NodeSource:

   ```bash
   curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   ```

2. Install Node.js and npm:

   ```bash
   sudo apt-get install -y nodejs
   ```

3. Install the `semistandard` coding style:

   ```bash
   sudo npm install semistandard --global
   ```

4. Clone this repository:

   ```bash
   git clone https://github.com/mugambi12/alx-higher_level_programming.git
   ```

5. Navigate to the project directory:

   ```bash
   cd alx-higher_level_programming/0x13-javascript_objects_scopes_closures
   ```

## Usage

To run the code for each task, navigate to the specific task directory and execute the corresponding JavaScript file using Node.js. For example:

```bash
cd 0-rectangle
node 0-main.js
```

Ensure you have execution permission on the JavaScript files:

```bash
chmod +x *.js
```

## Tasks

The project contains a series of tasks, each located in its respective directory. Each task involves creating or working with JavaScript classes, objects, and closures. The repository structure is organized as follows:

-  [**0-rectangle:**](./0-rectangle.js) Empty class definition for a rectangle.
- [**1-rectangle:**](./1-rectangle.js) Rectangle class with constructor to set width and height.
- [**2-rectangle:**](./2-rectangle.js) Rectangle class with constructor that validates dimensions.
- [**3-rectangle:**](./3-rectangle.js) Rectangle class with a print method to display the rectangle.
- [**4-rectangle:**](./4-rectangle.js) Rectangle class with methods to print, rotate, and double.
- [**5-square:**](./5-square.js) Square class that inherits from Rectangle.
- [**6-square:**](./6-square.js) Square class that inherits from Square and adds a charPrint method.
- [**7-occurrences:**](./7-occurrences.js) Function to count occurrences in a list.
- [**8-esrever:**](./8-esrever.js) Function to reverse a list without using the built-in reverse method.
- [**9-logme:**](./9-logme.js) Function to print the number of arguments and their values.
- [**10-converter:**](./10-converter.js) Function to convert a number to a different base.
- [**100-data:**](./100-map.js) Sample data for advanced task 11.
- [**100-map:**](./100-map.js) Script to compute a new array using map and the sample data.
- [**101-sorted:**](./101-sorted.js) Script to compute a dictionary of user ids by occurrence using the sample data.
- [**102-concat:**](./102-concat.js) Script to concatenate two files and save the result in a destination file.

Each task folder contains its corresponding JavaScript file along with a brief description of the task's requirements and expected output.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
