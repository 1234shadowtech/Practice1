```python
# Define the first number (Consider using a more descriptive variable name, e.g., num1)
a = 10  # PEP 8: Add spaces around the assignment operator

# Define the second number (Consider using a more descriptive variable name, e.g., num2)
b = 20  # PEP 8: Add spaces around the assignment operator

# Print the sum of the two numbers
print(a + b)  # Consider encapsulating this in a function for reusability
```

### REVISED CODE (Optional):
```python
# This script calculates the sum of two numbers and prints the result.

# Define the first number
num1 = 10  # Using descriptive variable names improves readability.

# Define the second number
num2 = 20  # Using descriptive variable names improves readability.

# Function to calculate and print the sum of two numbers
def print_sum(a, b):
    """Prints the sum of two numbers."""
    print(a + b)  # Encapsulating logic in a function improves reusability.

# Call the function
print_sum(num1, num2)  # Function call makes the code more modular.
```