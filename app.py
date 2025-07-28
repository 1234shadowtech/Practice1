print("hi, welcome")  # Prints a welcome message.

def Sq(x: int) -> int: 
    # Returns the square of the input integer.
    # Suggest renaming to 'square' for better readability.
    return x * x 

def Sqr(x: int) -> float:  # Updated return type to float for accuracy.
    # Returns the square root of the input integer.
    # Suggest renaming to 'square_root' for better readability.
    # Consider using math.sqrt for better precision and clarity.
    # Add input validation to handle negative numbers.
    return x**0.5

a = 10  # Assigns the value 10 to variable 'a'.
print(Sq(a))  # Prints the square of 'a'.
print(Sqr(a))  # Prints the square root of 'a'.