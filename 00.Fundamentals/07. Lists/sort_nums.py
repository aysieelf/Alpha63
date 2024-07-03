line = input().split(', ')
newlst = []

for i in line:
    newlst.append(int(i))

lst = sorted(newlst, reverse=True)

lst_str = []

for j in lst:
    lst_str.append(str(j))

print(', '.join(lst_str))
