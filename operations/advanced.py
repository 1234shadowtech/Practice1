from operations.basic import add

def multiply(a, b):  
    result = 0  
    for _ in range(b):  # Iterates 'b' times, adding 'a' to 'result' in each iteration.  
        result = add(result, a)  # Uses the 'add' function from 'operations.basic' to perform addition.  
    return result  # Returns the product of 'a' and 'b'.  

def power(base, exponent):  
    result = 1  
    for _ in range(exponent):  # Iterates 'exponent' times, multiplying 'result' by 'base' in each iteration.  
        result = multiply(result, base)  # Uses the 'multiply' function to perform multiplication.  
    return result  # Returns 'base' raised to the power of 'exponent'.