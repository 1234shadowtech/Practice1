### Suggestions for `app.py`

- **STYLE:** Rename function `Sq` to `square` for better readability and adherence to Python naming conventions.
- **STYLE:** Rename function `Sqr` to `square_root` for better readability and adherence to Python naming conventions.
- **IMPROVEMENT:** Add input validation in the `Sqr` function to handle negative numbers, as taking the square root of a negative number can lead to unexpected behavior.
- **IMPROVEMENT:** Use `math.sqrt` in the `Sqr` function for better precision and clarity, as it is the standard library function for square root calculations.
- **STYLE:** Add type hints for the return type of `Sq` and `Sqr` functions in the docstrings for consistency and clarity.
- **STYLE:** Add comments explaining why certain choices (e.g., using `x**0.5` instead of `math.sqrt`) were made, if applicable.

