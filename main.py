def binary_search(arr, target):
    low = 0  # Initialize the starting index of the search range
    high = len(arr) - 1  # Initialize the ending index of the search range

    while low <= high:  # Continue searching while the range is valid
        mid = (low + high) // 2  # Calculate the middle index of the current range

        if arr[mid] == target:  # Check if the middle element is the target
            return mid  # Return the index if the target is found
        elif arr[mid] < target:  # If the target is greater than the middle element
            low = mid + 1  # Narrow the search range to the upper half
        else:  # If the target is less than the middle element
            high = mid - 1  # Narrow the search range to the lower half

    return -1  # Return -1 if the target is not found in the array
 
a = [1, 2, 4, 6, 10, 13, 14]  # Example sorted array

print(binary_search(a, 10))  # Test case: Target is in the array
print(binary_search(a, 9))  # Test case: Target is not in the array