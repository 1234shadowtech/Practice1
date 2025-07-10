def SQr(x):  
    # Function to calculate the square root of x.
    # Note: This will raise a ValueError for negative values of x.
    return x**0.5  

def SQ(x):  
    # Function to calculate x raised to the power of itself (x**x).
    # This is an unusual operation and may not be intuitive to users.
    # Note: This will raise an error for x = 0 or x < 0.
    return x**x  

def car(x):  
    # Function to calculate the integer division of x by 2.
    # The name "car" is not descriptive of the function's purpose.
    return x//2