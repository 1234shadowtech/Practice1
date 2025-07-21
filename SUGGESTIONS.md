### Suggestions for `main.py`

- **IMPROVEMENT:** The calculation of `mid` using `(low + high) // 2` could potentially lead to an integer overflow in languages where integers have fixed sizes. While Python handles large integers gracefully, it is a good practice to use `low + (high - low) // 2` to avoid this issue and make the code more portable and robust.
- **STYLE:** The function could benefit from a docstring to explain its purpose, parameters, and return value. This would improve code readability and maintainability.
- **STYLE:** The variable names `low` and `high` are clear, but adding a comment to explain their roles (e.g., `low` is the start index, `high` is the end index) would make the code more beginner-friendly.
- **POTENTIAL ISSUE:** The function assumes that the input array `arr` is sorted. If an unsorted array is passed, the function will not behave as expected. Consider adding a check or documenting this assumption explicitly.

