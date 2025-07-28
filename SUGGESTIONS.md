### Suggestions for `app.py`

- **STYLE:** The function names `Sq` and `Sqr` are not descriptive enough. Consider renaming them to `square` and `square_root` for better readability and adherence to Python naming conventions.
- **STYLE:** The inline comments are helpful but could be more concise or removed if the function names are improved to be self-explanatory.
- **IMPROVEMENT:** Add type hints for the return values in the function definitions to ensure clarity and compatibility with static type checkers.
- **IMPROVEMENT:** Consider adding input validation to the `Sqr` function to handle cases where the input is negative, as the square root of a negative number is not defined for real numbers.
- **IMPROVEMENT:** Use the `math.sqrt` function from the `math` module for calculating square roots, as it is more precise and conveys intent clearly.

