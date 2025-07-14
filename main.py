from first import sqr  # Importing the `sqr` function from the `first` module. Ensure the module exists and the function is correctly implemented.

from second import super, s  # Invalid import: `super` is a reserved keyword in Python and cannot be used as an identifier.

b = 10  # Defining a global variable. Consider encapsulating this in a function or class for better scope control.

print(sqr(b))  # Calling the `sqr` function with `b` as an argument. Ensure `sqr` is implemented correctly in the `first` module.

print(super(b))  # Attempting to call `super` with `b` as an argument. This will fail due to the invalid import of `super`.

print(s(b))  # Calling the `s` function with `b` as an argument. Ensure `s` is implemented correctly in the `second` module.