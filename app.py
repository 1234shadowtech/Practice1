def sqr(x):
    # BUG: This function calculates the square root, not the square. Consider renaming it to `sqrt`.
    return x**0.5

# CRITICAL ISSUE: Syntax error. Replace `de` with `def`.
def div(x):
    # SUGGESTION: Consider renaming this function to `divide_by_two` for clarity.
    return x // 2  # STYLE: Add a comment explaining the use of floor division.

# STYLE: Add spaces around the assignment operator for better readability.
a = 10

# SUGGESTION: Add a comment explaining what the output of these print statements represents.
print(sqr(a))  # This prints the square root of `a`.

print(div(a))  # This prints the result of dividing `a` by 2 using floor division.