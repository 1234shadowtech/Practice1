### Suggestions for `first.py`

- **IMPROVEMENT:** The variable name `Open_AI_Key` does not follow Python's naming conventions (PEP 8). Consider renaming it to `open_ai_key` for consistency.
- **POTENTIAL ISSUE:** Storing sensitive information like API keys directly in the code is a security risk. It is recommended to use environment variables or a secure secrets management system instead.
- **STYLE:** The value assigned to `Open_AI_Key` is not formatted or validated. Consider adding checks to ensure the key meets expected patterns or length.

