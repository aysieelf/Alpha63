n = int(input())

for i in range(n):
    x = 'Yes'
    line = input().split(' ')
    length = len(line)
    for j in range(length):
        if line[j] != line[length -1 -j]:
            x = 'No'
    print(x)
    