def array_symmetry(arr: list) -> str:
    """
    Compares if two sides of an array are symmetric.

    Parameters:
        arr (list): List of numbers.

    Return:
        str: "Yes" if the list is symmetric, "No" otherwise.
    """

    array_length = len(arr) // 2
    for j in range(array_length):
        if arr[j] != arr[-j - 1]:
            return "No"
    return "Yes"


# N for how many arrays are going to be checked
n = int(input())

# iteration that checks for each list if it's symmetric
for _ in range(n):
    # splits the str input and creates a list
    array = input().split()

    # prints Yes or No
    print(array_symmetry(array))