# nput
# 7 2 -2 1 -5 4 5 -3 1
# Output
# -2 -5 -3 7 2 1 4 5 1


numbers = input().split(' ')

negative_num = []
positive_num = []
for i in numbers:
    if int(i) < 0:
        negative_num.append(i)
    elif int(i) >= 0:
        positive_num.append(i)

negative_num.extend(positive_num)
for ii in negative_num:
    print(ii, end=' ')
