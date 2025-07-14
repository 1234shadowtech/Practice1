from first import sqr  # Importing the `sqr` function from the `first` module.

def super(x):  # This function calculates the sum of the square of `x` twice.
    return sqr(x) + sqr(x)  # Calls the `sqr` function twice and adds the results.

def s(b):  # This function calculates the product of `b` and the remainder of `b` divided by 2.
    return b * (b % 2)  # Multiplies `b` by the result of `b % 2`.