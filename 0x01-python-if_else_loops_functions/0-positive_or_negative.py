#!/usr/bin/python3
import random

# generate a random integer between -10 and 10
number = random.randint(-10, 10)

# check if the number is positive, zero, or negative, and print a message accordingly
if number > 0:
	print(number, "is positive")
elif number == 0:
	print(number, "is zero")
else:
	print(number, "is negative")

# print a new line at the end
print()
