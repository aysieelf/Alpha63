# reads the number sublists (rows) from input
sublist_count = int(input())

# creates a 2d list (matrix)
matrix = []
for _ in range(sublist_count):
    row = [int(x) for x in input().split()]
    matrix.append(row)

# saves the coordinates in a list
coord = [int(x) for x in input().split()]

max_sum = float('-inf')
wall_rows = sublist_count - 1
wall_cols = len(matrix[0]) - 1


def matrix_sum(st_row: int, r_row: int, st_col: int, r_col: int) -> int:
    """
    Finds the sum between two given coordinates in a matrix.

    :param st_row: int - The starting row.
    :param r_row: int - The row we want to reach.
    :param st_col: int - The starting column.
    :param r_col: int - The column we want to reach.

    :return: int - The sum between coordinates in a matrix.
    """
    ttl = 0

    # sums the numbers on the starting row
    if st_col <= r_col:
        ttl += sum(matrix[st_row][st_col:r_col+1])
    else:
        ttl += sum(matrix[st_row][st_col:r_col:-1]) + matrix[st_row][r_col]

    # sums the numbers in the column
    if st_row <= r_row:
        for i in range(start_row + 1, r_row + 1):
            ttl += matrix[i][r_col]
        # i = st_row+1
        # while i <= r_row:
        #     ttl += matrix[i][r_col]
        #     i += 1
    else:
        # i = st_row-1
        # while i >= 0:
        #     ttl += matrix[i][r_col]
        #     i -= 1
        for i in range(start_row - 1, r_row - 1, -1):
            ttl += matrix[i][r_col]

    return ttl


# creates different conditions depending on coordinates
for row, col in zip(coord[::2], coord[1::2]):
    if row >= 0 and col >= 0:
        start_row, reach_row = row - 1, 0
        start_col, reach_col = 0, col - 1

    elif row < 0 <= col:
        start_row, reach_row = abs(row) - 1, 0
        start_col, reach_col = wall_cols, col - 1

    elif row >= 0 > col:
        start_row, reach_row = row - 1, wall_rows
        start_col, reach_col = 0, abs(col) - 1

    elif row < 0 and col < 0:
        start_row, reach_row = abs(row) - 1, wall_rows
        start_col, reach_col = wall_cols, abs(col) - 1

    # sums the numbers according to the coordinates
    temp_sum = matrix_sum(start_row, reach_row, start_col, reach_col)

    # updates max sum if the temporary sum is bigger
    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)
