lst = input().split(',')

check_lst = [] 

for i in lst:
    if i not in check_lst:
        check_lst.append(i)

print(','.join(check_lst))


