count = int(input())

first_line_list = []
second_line_list = []
# first line of array input
for i in range(count):
    first_line_list.append(input())

# second line of array input
for i in range(count):
    second_line_list.append(input())

if first_line_list == second_line_list:
    print('equal')
else:
    print('not equal')


n = int(input())
 
list1 = []
list2 = []
flag = True 
 
for i in range(n):
    list1.append(input())
 
for i in range(n):
    list2.append(input())
 
for i in range(n):
    if list1[i] == list2[i]:
        continue
    else:
        flag = False
 
if flag == True:
    print('equal')
else:
    print('not equal')
