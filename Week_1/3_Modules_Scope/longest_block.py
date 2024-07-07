# reads an array with letters
letters = input()


def longest_block(string: str) -> str:
    """
    Finds the first substring that is with the length of the largest "block" in the string.
    :param string: str - A string with letters.
    :return: str - A string with the largest "block".
    """

    # 2d list with all blocks that appends the first letter
    blocks = [[string[0]]]
    # counter that keeps the sublist index
    x = 0
    # temporary letter with which the current letter is compared
    temp_letter = string[0]

    # iterates through the list to separate the blocks in the 2d list
    for i in range(1, len(string)):
        if string[i] != temp_letter:
            blocks.append([])
            x += 1
            blocks[x].append(string[i])
            temp_letter = string[i]
        elif string[i] == temp_letter:
            blocks[x].append(string[i])

    # fonds the longest block
    block = max(blocks, key=len)

    return ''.join(block)


print(longest_block(letters))
