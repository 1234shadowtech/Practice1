```python
def SQR_ADD(x, y):  # Function to calculate the square root of x and add it to y
    return (x**0.5) + y  # Raises an error if x is negative; no input validation

a = 10  # Variable 'a' with a value of 10
b = 20  # Variable 'b' with a value of 20

print(SQR_ADD(a, b))  # Prints the result of SQR_ADD(10, 20)
print(SQR_ADD(b, a))  # Prints the result of SQR_ADD(20, 10)
```