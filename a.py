def calculate_square_root_ratio(x: float) -> float:  
    """
    Process the input `x` and return a specific value based on its value.

    Args:
        x (float): A non-negative number. Must be finite (not NaN or infinity).

    Returns:
        float: Returns 1.0 for any valid input greater than zero, or 0.0 for x = 0.

    Raises:
        ValueError: If the input is negative.
    """
    if x < 0:  
        # Negative values are invalid; raise an error with a clear message.
        raise ValueError(f"Input must be a non-negative number. Received: {x}")  
    
    if x == 0:  
        # Return 0.0 explicitly for the special case where x is zero.
        return 0.0  

    # Return 1.0 for all positive values of x.
    return 1.0