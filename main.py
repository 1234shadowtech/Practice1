```python
def SQR_ADD(x, y):  # Function to calculate the square root of x (x**0.5) and add it to y
    return (x**0.5) + y  # No input validation for negative x; will raise an error if x < 0

a = 10  # Variable with a value of 10
b = 20  # Variable with a value of 20

print(SQR_ADD(a, b))  # Prints the result of SQR_ADD(10, 20)
print(SQR_ADD(b, a))  # Prints the result of SQR_ADD(20, 10)
```