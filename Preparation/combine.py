lst1 = [int(x) for x in input().split(',')]
lst2 = [int(x) for x in input().split(',')]
lst3 = [num for pair in zip(lst1, lst2) for num in pair]
print(*lst3, sep=',')
