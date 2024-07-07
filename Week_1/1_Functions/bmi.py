def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculates BMI given weight and height of a person.

    Parameters:
        weight (float) : Weight in kilograms.
        height (float) : Height in meters.

    Returns:
        bmi (float) - BMI rounded to two decimal places.

    Raises:
        ValueError: If weight or height is less than or equal to zero.
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be greater than 0")
    bmi = weight / (height**2)
    return round(bmi, 2)


# Test cases
x = calculate_bmi(70, 1.75)
print(x)
x = calculate_bmi(85, 1.8)
print(x)
