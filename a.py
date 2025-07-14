def calculate_square_root_ratio(x: float) -> float:  
    """
    Process the input `x` and return a specific value based on its value.

    Args:
        x (float): A non-negative number.

    Returns:
        float: Returns 1.0 for any valid input greater than zero, or 0.0 for x = 0.

    Raises:
        ValueError: If the input is negative.
    """
    if x < 0:  
        # Raise an error if the input is negative, as negative values are invalid.
        raise ValueError(f"Input must be a non-negative number. Received: {x}")  
    
    if x == 0:  
        # Special case: return 0.0 explicitly when x is zero.
        return 0.0  

    # For all positive values of x, return 1.0.
    return 1.0