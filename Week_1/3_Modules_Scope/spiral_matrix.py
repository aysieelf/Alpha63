# reads integer input for the size of the matrix
n = int(input())

# creates an n * n matrix with placeholder zeros
matrix = [[0 for _ in range(n)] for _ in range(n)]


def spiral_nums(number):
    """
    Fills a number * number matrix in a spiral order with numbers starting from 1.

    :param number: int - The size of the matrix.
    :return: None - The function directly modifies the global 'matrix' variable.
    """

    wall = number - 1
    direction_rows = 0
    direction_cols = 1
    row = 0
    col = 0
    temp_number = 1

    # variable to track the minimum index position
    x = 0

    while temp_number <= number ** 2:
        # fills the current cell with the number
        matrix[row][col] += temp_number
        temp_number += 1

        # updates directions at the corners of the spiral
        if row == x + 1 and col == x:
            direction_rows = 0
            direction_cols = 1
            wall -= 1
            x += 1
        elif row == x and col == wall:
            direction_rows = 1
            direction_cols = 0
        elif row == wall and col == wall:
            direction_rows = 0
            direction_cols = -1
        elif row == wall and col == x:
            direction_cols = 0
            direction_rows = -1

        # moves to the next cell
        row += direction_rows
        col += direction_cols


# fills the matrix with numbers in spiral order
spiral_nums(n)


# output the matrix
for row in matrix:
    row_str = ' '.join(str(i) for i in row)
    print(row_str)



