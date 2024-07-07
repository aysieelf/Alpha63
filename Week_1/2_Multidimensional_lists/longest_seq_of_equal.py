def longest_equal_seq(lst: list) -> int:
    """
    Finds the length of the maximal sequence of equal elements in an array of N integers.

    :param lst: A list of N integers.

    :return: Integer that represents the length of the maximal sequence of equal elements.
    """
    max_seq = 1
    seq_count = 1
    prev_char = lst[0]

    # iterates through list
    for i in range(1, len(lst)):
        # checks if the current element is equal to previous element
        if lst[i] == prev_char:
            seq_count += 1

        # if the sequence of equal elements has ended
        else:
            # checks if the sequence is bigger than previous sequence
            if seq_count > max_seq:
                max_seq = seq_count

            # reset sequence count and update previous element
            seq_count = 1
            prev_char = lst[i]

    # Final check if the last sequence is bigger than previous sequence
    if seq_count > max_seq:
        max_seq = seq_count

    return max_seq


# reads from input an array of N integers
n = int(input())

# creates a list of integers from the array
numbers = [int(input()) for _ in range(n)]

# prints the length of the maximal sequence of equal elements
print(longest_equal_seq(numbers))
