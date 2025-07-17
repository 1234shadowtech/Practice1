### Suggestions for `main.py`

- **IMPROVEMENT:** Add type hints to the function definitions for better readability and to ensure type safety. For example, `def sqr(x: int) -> int:` and `def mod(x: int) -> int:`.
- **STYLE:** Use consistent spacing around operators for better readability. For example, `return x * x` instead of `return x*x` and `return x % 10` instead of `return x%10`.
- **IMPROVEMENT:** Include docstrings instead of comments directly above the functions to follow Python's best practices for documentation. For example:
  ```python
  def sqr(x: int) -> int:
      """Calculate the square of a number."""
      return x * x
  ```
- **POTENTIAL ISSUE:** The variable `a` is hardcoded as `10`. Consider making it dynamic or accepting user input to improve flexibility and usability.

