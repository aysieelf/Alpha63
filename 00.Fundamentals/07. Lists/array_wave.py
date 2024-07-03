line = input().split(' ')
lst = []

for i in line:
    lst.append(int(i))

x = 'yes'
lenght = len(lst)
for j in range(1, lenght -1):
    if not (lst[j-1] > lst[j] < lst[j+1]) and not (lst[j-1] < lst[j] > lst[j+1]):
        x = 'no'

print(x)




line = [int(el) for el in input().split()]
output = ""

el_0 = line[0]
 
for el in line[1:]:
    if el > el_0:
        output += "+"
    else:
        output += "-"
    el_0 = el
 
# After processing all elements in line, it checks if there are consecutive "+" or "--" in the output string. If any are found, it prints "no" because it indicates that the sequence is not strictly increasing. Otherwise, it prints "yes," indicating that the sequence is strictly increasing.
if "--" in output or "++" in output:
    print("no")
else:
    print("yes")