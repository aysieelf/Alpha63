# N for array of numbers
n = [int(num) for num in input().split()]

# creates a list of 3 empty lists (groups)
groups = [[] for _ in range(3)]

# assigns each number to the correct sublist based on remainder
for i in n:
    # checks what is the remainder of each number
    remainder = i % 3
    groups[remainder].append(str(i))

# prints the numbers in the correct group
for group in groups:
    if len(groups) != 0:
        print(" ".join(group))
