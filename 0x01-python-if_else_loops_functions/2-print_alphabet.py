#!/usr/bin/python3
# 2-print_alphabet.py

"""
Print the alphabet in lowercase, not followed by a new line.
"""

# loop through the ASCII values for lowercase letters (97-122)
for letter in range(97, 123):
    # use chr() to convert each value to its corresponding char and print it
    print("{}".format(chr(letter)), end="")

# print a new line character at the end
print()
