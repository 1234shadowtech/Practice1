from operations.basic import add, subtract
from operations.advanced import multiply, power
from utilities.validator import is_positive, is_even

def main():
    a = 5
    b = 3
    
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a}^{b} = {power(a, b)}")
    
    print(f"Is {a} positive? {is_positive(a)}")
    print(f"Is {b} even? {is_even(b)}")

if __name__ == "__main__":
    main()