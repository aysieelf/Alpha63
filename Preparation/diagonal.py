n = int(input())

matrix = [[(2**(j+i)) for j in range(n)] for i in range(n)]

total = 0
x = 1
for sublist in matrix:
    for i in range(x, n):
        total += sublist[i]
    x += 1

print(total)