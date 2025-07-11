from operations.basic import add, subtract  # Importing basic arithmetic operations
from operations.advanced import multiply, power  # Importing advanced arithmetic operations
from utilities.validator import is_positive, is_even  # Importing utility functions for validation

def main():  # Main function to execute the program
    a = 5  # Hardcoded value for variable 'a'
    b = 3  # Hardcoded value for variable 'b'
    
    print(f"{a} + {b} = {add(a, b)}")  # Printing the result of addition
    print(f"{a} - {b} = {subtract(a, b)}")  # Printing the result of subtraction
    print(f"{a} * {b} = {multiply(a, b)}")  # Printing the result of multiplication
    print(f"{a}^{b} = {power(a, b)}")  # Printing the result of exponentiation
    
    print(f"Is {a} positive? {is_positive(a)}")  # Checking if 'a' is positive
    print(f"Is {b} even? {is_even(b)}")  # Checking if 'b' is even

if __name__ == "__main__":  # Entry point of the program
    main()  # Calling the main function