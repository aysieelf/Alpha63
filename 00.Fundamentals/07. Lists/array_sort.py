line = input().split(',')
lst = []
zeros = []
for i in range(len(line)):
    if int(line[i]) != 0:
        lst.append(line[i])
    else:
        zeros.append(line[i])

new_list = lst + zeros

print(','.join(new_list))