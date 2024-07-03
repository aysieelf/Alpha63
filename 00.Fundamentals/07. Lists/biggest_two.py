line = input().split(' ')
lst = []

for i in line:
    lst.append(int(i))

first = -9999
second = -9999

for j in lst:
    if j > first:
        second = first
        first = j
    elif j > second:
        second = j

print(first, second)


# ========================================================


line = input().split(' ')
lst = []

for i in line:
    lst.append(int(i))

lst = sorted(lst, reverse=True)[:2]

for i in lst:
    print(i, end=' ')