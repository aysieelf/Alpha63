def set_board(r: int, c: int) -> list:
    """
    Creates a board with the size of the parameters.

    Parameters:
        r (int): Rows of the board.
        c (int): Columns of the board.

    Returns:
        board (list): A 2d list that represents the board.
    """
    board = [[0 for column in range(c)] for row in range(r)]
    return board


print()

def calculate_points(board: list) -> int:
    """
    Calculates the points for each player.

    Parameters:
        board (list): A 2d list representing the board.

    Returns:
        int: Sum of points representing how many boats a player has on the board.
    """
    points = 0
    for _ in board:
        for p in _:
            points += p
    return points


def shoot(board: list, turn: str) -> bool:
    """
    Checks if a shoot is a miss or a kill and changes the board.

    Parameters:
        board (list): A 2d list that represents the board.
        turn (str): A string with the input of the player.

    Return:
        prints a message
        bool: True if it's a hit, False if it's a miss.
    """
    _, r, c = turn.split()
    r, c = int(r), int(c)
    if board[r][c] == 1:
        board[r][c] = "x"
        print("Booom")
        return True
    elif board[r][c] == "x":
        print("You already shot there!")
        return False
    else:
        board[r][c] = "x"
        print("Missed")
        return False


def battle_boats(points1: int, points2: int, board1: list, board2: list) -> str:
    """
    A game of battle boats, where each player tries to shoot a boat on other player's board.

    Parameters:
        points1 (int): The points (boats) that are left of player 1.
        points2 (int): The points (boats) that are left of player 2.
        board1 (list): A 2d list representing the first player's board.
        board2 (list): A 2d list representing the second player's board.

    Returns:
        str: A string with the points (boats) left for each player, P1:P2.
    """

    # the game terminates if a player is left with no points (boats)
    # or if the input reads "END"
    while points1 != 0 and points2 != 0:

        # first player shoots
        p1_turn = input()
        if p1_turn == "END":
            return f"{points1}:{points2}"
        else:
            change2 = shoot(board2, p1_turn)
            if change2:
                points2 -= 1

        # second player shoots
        p2_turn = input()
        if p2_turn == "END":
            return f"{points1}:{points2}"
        else:
            change1 = shoot(board1, p2_turn)
            if change1:
                points1 -= 1

        if points1 == 0 or points2 == 0:
            return f"{points1}:{points2}"


# define size of boards
rows, columns = input().split()
rows = int(rows)
columns = int(columns)

# create boards
board_p1 = set_board(rows, columns)
board_p2 = set_board(rows, columns)

# player 1 sets boats
for i in range(rows):
    board_p1[i] = [int(x) for x in input().split()]

# player 2 sets boats
for j in range(rows, 0, -1):
    temp_boats = [int(x) for x in input().split()]
    temp_boats.reverse()
    board_p2[j] = temp_boats

# player 1 points
points_p1 = calculate_points(board_p1)

# player 2 points
points_p2 = calculate_points(board_p2)

# players take turns until the game ends
print(battle_boats(points_p1, points_p2, board_p1, board_p2))
