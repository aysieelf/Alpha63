# read input
digits_n1, digits_n2 = input().split()
digits_n1, digits_n2 = int(digits_n1), int(digits_n2)

# create a list
n1 = [[int(x)] for x in input().split()]
n2 = [[int(x)] for x in input().split()]


def ttl_number(n1: list):
    """
    Summarises numbers in each nested lists, by adding tens to the next one.

    Parameters:
        n1 (list): A 2d list, each nested list contains one-digit numbers.
    """
    tens = 0
    for row in range(len(n1)):
        new_row = sum(n1[row]) + tens
        if new_row >= 10:
            tens = 1
            new_row -= 10
        else:
            tens = 0
        n1[row] = new_row
    if tens == 1:
        n1.append(1)
    return n1


if len(n1) < len(n2):
    n1, n2 = n2, n1

# creates a 2d list
for i in range(len(n2)):
    n1[i].append(*n2[i])

# gets the total number
ttl_number(n1)

# converts the elements of the n1 list to strings for output
output_num = [str(x) for x in n1]

# print the result
print(' '.join(output_num))
