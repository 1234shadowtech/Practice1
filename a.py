def calculate_square_root_ratio(x: float) -> float:  
    """
    Process the input `x` and return a specific value based on its value.

    Args:
        x (float): A non-negative number. Must be finite (not NaN or infinity).

    Returns:
        float: Returns 1.0 for any valid input greater than zero, or 0.0 for x = 0.

    Raises:
        ValueError: If the input is negative, NaN, infinity, or not a number.
    """
    import math  # Move this import to the top of the file for better practice.

    # Validate that the input is a number and finite in a single step.
    if not isinstance(x, (int, float)) or not math.isfinite(x):  
        raise ValueError(f"Input must be a finite, non-negative number. Received: {x}")

    # Check if the input is negative; raise an error with a clear message.
    if x < 0:  
        raise ValueError(f"Input must be non-negative. Received: {x}")  
    
    # Return 0.0 for the special case where x is zero; otherwise, return 1.0.
    return 0.0 if x == 0 else 1.0  # Simplified return logic.