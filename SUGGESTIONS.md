### Suggestions for `app.py`

### SUGGESTIONS:
- `BUG:` The function `sqr` is incorrectly named. It calculates the square root, not the square. Consider renaming it to `sqrt` for clarity.
- `BUG:` The function `fool` has a typo in its definition (`de` instead of `def`). This will cause a syntax error.
- `BUG:` The variable `x` in `print(mod(x))` is undefined. This will raise a `NameError`.
- `IMPROVEMENT:` Add type hints to the function definitions to improve code readability and maintainability.
- `STYLE:` The variable `a` is defined globally but could be passed as an argument to the functions for better encapsulation and reusability.

### COMMENTED CODE:
def sqr(x):  # Calculates the square root of x (consider renaming to sqrt for clarity)
    return x**0.5

de fool(x):  # Syntax error: 'de' should be 'def'
    return x//2  # Returns the integer division of x by 2

def mod(x):  # Returns the remainder when x is divided by 2
    return x%2

a=10  # Global variable used for function calls

print(sqr(a))  # Prints the square root of a
print(fool(a))  # Prints the integer division of a by 2
print(mod(x))  # Error: x is undefined

