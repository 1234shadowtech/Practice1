from first import sqr  # Importing the `sqr` function from the `first` module.

from second import super, s  # Invalid import: `super` is a reserved keyword in Python and cannot be used as an identifier. This will cause a SyntaxError.

b = 10  # Defining a global variable `b` with the value 10.

print(sqr(b))  # Calling the `sqr` function with `b` as an argument and printing the result.

print(super(b))  # Attempting to call `super` (invalid import) with `b` as an argument and printing the result.

print(s(b))  # Calling the `s` function with `b` as an argument and printing the result.