# 0x07. Python - Test-driven development

This repository contains solutions to the tasks assigned in the project **0x07. Python - Test-driven development**. This project focuses on test-driven development (TDD) in Python programming.

## Table of Contents
* [Concepts](#concepts)
* [Background Context](#background-context)
* [Resources](#resources)
* [Learning Objectives](#learning-objectives)
* [Requirements](#requirements)
* [Tasks](#tasks)
    * [Task 0: Integers addition](#task-0-integers-addition)
    * [Task 1: Divide a matrix](#task-1-divide-a-matrix)
    * [Task 2: Say my name](#task-2-say-my-name)
    * [Task 3: Print square](#task-3-print-square)
    * [Task 4: Text indentation](#task-4-text-indentation)
    * [Task 5: Max integer - Unittest](#task-5-max-integer---unittest)
    * [Task 6: Matrix multiplication](#task-6-matrix-multiplication)
    * [Task 7: Lazy matrix multiplication](#task-7-lazy-matrix-multiplication)
    * [Task 8: CPython #3: Python Strings](#task-8-cpython-3-python-strings)

## Concepts
* Never forget a test

## Background Context
In this project, the focus is on test-driven development (TDD) in Python programming. The project emphasizes writing tests and documentation before writing the actual code. The intranet checks for Python projects will not be released before the first deadline, allowing for a stronger focus on TDD and considering all possible edge cases. It is encouraged to work together on test cases to ensure comprehensive coverage.

## Resources
Read or watch:
* [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
* [doctest – Testing through documentation](https://pymotw.com/3/doctest/index.html)
* [Unit Tests in Python](https://www.youtube.com/watch?v=6tNS--WetLI)
* [Unittest module](https://docs.python.org/3/library/unittest.html)
* [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html#interactive-and-non-interactive-tests)

## Learning Objectives
Upon completion of this project, you should be able to explain to anyone, without the help of Google:
* Why Python programming is awesome
* What an interactive test is
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

## Requirements
### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.\*) style
* All your files must be executable
* The length of your files will be tested using wc

### Python Test Cases
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project: ex: for task 0, the tests folder should contain a file tests/test\_0.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test\_0.py
* We strongly encourage you to work together on test cases so that you don't miss any edge case – The Checker is checking for tests!

## Tasks
### Task 0: Integers addition
Write a function that adds 2 integers.
 - Prototype: `def add_integer(a, b=98):`
 - `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
 - `a` and `b` must be first casted to integers if they are float
 - Returns an integer: the addition of `a` and `b`
 - You are not allowed to import any module

### Task 1: Divide a matrix
Write a function that divides all elements of a matrix.
 - Prototype: `def matrix_divided(matrix, div):`
 - `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
 - Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
 - `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
 - `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
 - All elements of the matrix should be divided by `div`, rounded to 2 decimal places
 - Returns a new matrix
 - You are not allowed to import any module

### Task 2: Say my name
 - Write a function that prints `"My name is " followed by the first and last name.`
 - Prototype: `def say_my_name(first_name, last_name=""):`
 - `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
 - You are not allowed to import any module

### Task 3: Print square
Write a function that prints a square with the character `#`.
 - Prototype: `def print_square(size):`
 - `size` is the size length of the square
 - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
 - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
 - if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
 - You are not allowed to import any module

### Task 4: Text indentation
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.
 - Prototype: `def text_indentation(text):`
 - `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
 - There should be no space at the beginning or at the end of each printed line
 - You are not allowed to import any module

### Task 5: Max integer - Unittest
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):.`

 - Your test file should be inside a folder `tests`
 - You have to use the `unittest module`
 - Your test file should be python files (extension: `.py`)
 - Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
 - All tests you make must be passable by the function below
 - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Task 6: Matrix Multiplication
Write a function that multiplies two matrices.

- Read: [Matrix multiplication - only Matrix product (two matrices)](https://en.wikipedia.org/wiki/Matrix_multiplication)
- Prototype: `def matrix_mul(m_a, m_b):`
- `m_a` and `m_b` must be validated with these requirements in this order
`m_a` and `m_b` must be lists of lists containing integers or floats.
  - If `m_a` or `m_b` is not a list, raise a `TypeError` exception with the message "m_a must be a list" or "m_b must be a list".
  - If `m_a` or `m_b` is not a list of lists, raise a `TypeError` exception with the message "m_a must be a list of lists" or "m_b must be a list of lists".
  - If `m_a` or `m_b` is empty (i.e., `[]` or `[[]]`), raise a `ValueError` exception with the message "m_a can't be empty" or "m_b can't be empty".
  - If an element in `m_a` or `m_b` is not an integer or a float, raise a `TypeError` exception with the message "m_a should contain only integers or floats" or "m_b should contain only integers or floats".
  - If `m_a` or `m_b` is not a rectangle (i.e., all rows should have the same size), raise a `TypeError` exception with the message "each row of m_a must be of the same size" or "each row of m_b must be of the same size".

 - If `m_a` and `m_b` cannot be multiplied, raise a `ValueError` exception with the message "m_a and m_b can't be multiplied".
- You are not allowed to import any module.

### Task 7: Lazy matrix multiplication
Write a function that multiplies 2 matrices by using the module `NumPy`
To install it: `pip3 install numpy==1.15.0`

 - Prototype: `def lazy_matrix_mul(m_a, m_b):`
 - Test cases should be the same as `100-matrix_mul` but with new exception type/message

### Task 8: CPython #3: Python Strings
Create a function that prints Python strings.

 - Prototype: `void print_python_string(PyObject *p);`
 - Format: see example
 - If `p` is not a valid string, print an error message (see example)
 - Read: `Unicode HOWTO`
About:

 - Python version: 3.4
 - You are allowed to use the C standard library
 - Your shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

---

*For more detailed information, you can check the [project repository on GitHub](https://github.com/mugambi12/alx-higher_level_programming/tree/main/0x07-python-test_driven_development).*
