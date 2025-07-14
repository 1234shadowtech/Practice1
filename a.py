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
    import math  # Import moved to the top of the file for better organization.

    # Validate that the input is a finite number and non-negative.
    if not isinstance(x, (int, float)) or not math.isfinite(x):  
        # Combine the error message for non-finite and invalid types for clarity.
        raise ValueError(f"Input must be a finite number. Received: {x}")

    # Check if the input is negative; raise an error with a clear message.
    if x < 0:  
        # This check is redundant since the above condition already ensures x is non-negative.
        raise ValueError(f"Input must be non-negative. Received: {x}")  
    
    # Return 0.0 for the special case where x is zero; otherwise, return 1.0.
    return 0.0 if x == 0 else 1.0  # Simplified return logic.