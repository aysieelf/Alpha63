n = int(input())

for i in range(n):
    print(i+1, end=' ')

num = n
for i in range(n-1):
    num = num - 1
    print(num, end=' ')




n = int(input())
for i in range(n):
    print(i+1, end=" ")
temp = n
for j in range(1, n):
    temp -= 1
    print(temp, end=" ")