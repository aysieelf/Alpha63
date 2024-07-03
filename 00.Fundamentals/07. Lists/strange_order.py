lst = input().split(',')

negative_num = []
zeros = []
positive_num = []

for i in lst:
    if int(i) < 0:
        negative_num.append(i)
    elif int(i) == 0:
        zeros.append(i)
    else:
        positive_num.append(i)


str_order = negative_num + zeros + positive_num
print(','.join(str_order))