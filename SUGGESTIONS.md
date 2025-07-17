### Suggestions for `main.py`

- **IMPROVEMENT:** The function name `mod` is not descriptive enough. Consider renaming it to something more meaningful, such as `modulo_two`, to improve code readability.
- **IMPROVEMENT:** Add type hints to the function definitions for better clarity and to help with static analysis tools. For example, `def sqr(x: int) -> int` and `def mod(x: int) -> int`.
- **STYLE:** The code lacks a newline at the end of the file, which is a common style guideline in Python.
- **POTENTIAL ISSUE:** The `mod` function assumes that the input `x` is an integer. If a non-integer (e.g., a float or string) is passed, it will raise a `TypeError`. Consider adding input validation or documenting the expected input type.

