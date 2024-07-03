n = int(input())
a = 0
b = 0
for i in range(1, n+1):
    a = i
    print(a, end=' ')
    for ii in range(1, n):
        b = a + ii
        print(b, end=' ')
    print()