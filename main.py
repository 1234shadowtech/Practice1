from help import special

def sqr(x):  
    return x*x  # Returns the square of the input value `x`.

def mod(x):  
    return x%2  # Returns the remainder when `x` is divided by 2.

a=30  # Assigns the value 10 to the variable `a`.
b=20
print(mod(a))  # Prints the result of the `mod` function when called with `a` as the argument.
print(sqr(b))
print(special(a,b))

