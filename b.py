def special(x):
    # The function calculates the sum of two square roots of the input x.
    # However, the square root of x is calculated twice, which is redundant.
    return (x**0.5) + (x**0.5)  # This can be optimized by calculating the square root once.