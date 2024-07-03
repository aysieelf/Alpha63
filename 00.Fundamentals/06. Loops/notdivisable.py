# Input	Output
# 10	1 2 4 5 8 10
# 3	1 2

count = int(input())
number = 0
for i in range(count):
    number = number + 1
    if number % 3 == 0:
        continue
    elif number % 7 == 0:
        continue
    else:
        print (number, end=' ')