### Suggestions for `operations/basic.py`

1. The `add` function has an unexpected behavior due to the `+1` added to the result. This could lead to incorrect calculations if the function is intended to perform a standard addition. Consider clarifying the purpose of this adjustment or removing it if unintentional.  
2. The function names `add` and `subtract` are clear, but adding docstrings to explain their purpose and any specific behavior (e.g., the `+1` in `add`) would improve code readability and maintainability.  
3. Consider adding type hints to the function signatures for better clarity and to help with static analysis tools. For example: `def add(a: int, b: int) -> int:`

