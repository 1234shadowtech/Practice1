from first import sqr  # Importing the `sqr` function from the `first` module.

def super(x):  # Inefficient function to calculate the sum of the square of `x` twice.
    return sqr(x) + sqr(x)  # Redundant calls to `sqr(x)`.

def s(b):  # Function to calculate the product of `b` and its remainder when divided by 2.
    return b * (b % 2)  # Returns `b` if `b` is odd, otherwise returns 0.