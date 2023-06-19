# 0x0C. Python - Almost a circle

This project is part of the Higher Level curriculum at ALX School. It covers various concepts in Python programming and object-oriented programming (OOP). The project focuses on topics such as import, exceptions, classes, private attributes, getter/setter methods, class methods, static methods, inheritance, unittest module, and reading/writing files.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the concept of unit testing and implement it in a large project
- Serialize and deserialize a class
- Write and read JSON files
- Understand and use *args and **kwargs in Python
- Handle named arguments in functions

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the project folder, is mandatory
- Code should use the pycodestyle (version 2.8.\*) for style checking
- All files must be executable
- File length will be tested using `wc`
- All modules, classes, and functions should be documented

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All files should end with a new line
- All test files should be inside a folder named `tests`
- unittest module must be used
- All test files should be python files (extension: `.py`)
- All test files and folders should start with `test_`
- Test file organization should mirror the project's file structure
- All tests should be executed using `python3 -m unittest discover tests`

## Project Tasks

### 0. If it's not tested it doesn't work

All files, classes, and methods must be unit tested and PEP 8 validated.

### 1. Base class

Create a class `Base` in the file `models/base.py`. The `Base` class will serve as the base for all other classes in this project. It will manage the `id` attribute to avoid code duplication.

### 2. First Rectangle

Create a class `Rectangle` in the file `models/rectangle.py` that inherits from the `Base` class. It represents a rectangle and has private instance attributes for width, height, x, y.

### 3. Validate attributes

Update the `Rectangle` class to validate the attributes passed to the class constructor and the setter methods.

### 4. Area first

Add a method `def area(self):` to the `Rectangle` class that calculates and returns the area of the rectangle.

### 5. Display #0

Add a method `def display(self):` to the `Rectangle` class that prints the rectangle using the `#` character.

### 6. __str__

Override the `__str__` method in the `Rectangle` class to provide a string representation of the rectangle instance.

### 7. Display #1

Update the `display` method in the `Rectangle` class to take into account the `x` and `y` coordinates.

### 8. Update #0

Add a method `def update(self, *args):` to the `Rectangle` class that assigns an argument to each attribute of the rectangle.

### 9. Update #1

Add a method `def update(self, *args, **kwargs):` to the `Rectangle` class that assigns a key/value argument to attributes of the rectangle.

## Getting Started

To get started with the project, you can follow these steps:

1. Clone the repository:

```python
  $ git clone https://github.com/Mugambi12/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle
```

2. Navigate to the project directory:

```python
  $ cd your_repository
```

3. Compile the Python files (if needed):

```python
  $ chmod +x *.py
```

4. Run the unit tests:

```python
  $ python3 -m unittest discover tests
```


5. Start implementing the required classes and methods based on the project tasks.

## File Descriptions

- `models/` directory: Contains the Python files defining the classes for the project.
- `tests/` directory: Contains the Python files for unit tests.
- `models/base.py`: Defines the `Base` class.
- `models/rectangle.py`: Defines the `Rectangle` class.

## Author

- Silas Mugambi: [mugambi12](https://github.com/mugambi12)
