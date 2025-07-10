### Suggestions for `main.py`

1. **[Severity: Low, Tag: Naming Convention]**: The function name `SQRT` does not follow Python's naming conventions (PEP 8). Function names should be in lowercase with words separated by underscores (e.g., `sqrt`).
2. **[Severity: Low, Tag: Readability]**: Variable names `a` and `b` are not descriptive. Using more meaningful names would improve code readability.
3. **[Severity: Low, Tag: Unused Variable]**: The variable `b` is declared but not used, which may confuse readers or indicate incomplete logic.
4. **[Severity: Low, Tag: Type Hinting]**: The function `SQRT` does not include type hints for its parameter or return value. Adding type hints would make the code more self-documenting.
5. **[Severity: Low, Tag: Edge Case Handling]**: The function does not handle edge cases, such as when `x` is negative, which would result in a `ValueError` for real numbers.

