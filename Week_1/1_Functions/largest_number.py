def find_largest(numbers: list) -> int:
    """
    Finds the largest integer in a list of numbers.

    Parameters:
        numbers (list) : List of the integer numbers.

    Returns:
        largest (int) : The largest number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("The list of numbers can't be empty.")

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# Test cases
x = find_largest([1, 2, 3, 4, 5])  # largest should be 5
print(x)
x = find_largest([-10, -2, -3, -6])  # largest should be -2
print(x)
