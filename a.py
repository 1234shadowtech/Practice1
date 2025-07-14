def calculate_square_root_ratio(x: float) -> float:  
    """
    Process the input `x` and return a specific value based on its value.

    Args:
        x (float): A non-negative number. Must be finite (not NaN or infinity).

    Returns:
        float: Returns 1.0 for any valid input greater than zero, or 0.0 for x = 0.

    Raises:
        ValueError: If the input is negative, NaN, or infinity.
    """
    # Check if the input is negative; raise an error with a clear message.
    if x < 0:  
        raise ValueError(f"Input must be a non-negative number. Received: {x}")  
    
    # Check if the input is NaN (not a number); raise an error for invalid input.
    if x != x:  # NaN is not equal to itself.
        raise ValueError("Input must be a finite, non-negative number. Received: NaN")
    
    # Check if the input is infinity; raise an error for invalid input.
    if x == float('inf'):  
        raise ValueError("Input must be a finite, non-negative number. Received: Infinity")
    
    # Return 0.0 explicitly for the special case where x is zero.
    if x == 0:  
        return 0.0  
    
    # Return 1.0 for all positive values of x.
    return 1.0