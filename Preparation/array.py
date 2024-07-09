lst_numbers = [int(x) for x in input().split(',')]

num_max = len(lst_numbers)

missing_numbers = []
for num in range(1, num_max):
    if num not in lst_numbers:
        missing_numbers.append(num)

print(*missing_numbers, sep=',')