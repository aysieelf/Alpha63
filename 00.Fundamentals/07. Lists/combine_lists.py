# first = input()
# second = input()

# list1 = first.split(',')
# list2 = second.split(',')

# output = ''
# for i in range(len(list1)):
#     output = output + list1[i] + ',' + list2[i] + ','

# print(output.strip(','))

l1 = input().split(',')
l2 = input().split(',')
output = []
for i in range(len(l1)):
    output.append(l1[i])
    output.append(l2[i])

print(','.join(output))
