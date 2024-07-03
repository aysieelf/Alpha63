info = input()
output = 0

if info[0].isdigit() or info[1].isdigit():
    if '.' in info:
        output = float(info) + 1
    else:
        output = int(info) + 1
else:
    output = info[::-1]

print(output)



info = input()
 
if info[-1].isdigit():
    temp = float(info) // 1
    if (float(info) - temp) == 0:
        output = int(info) + 1
        print(output)
    else:
        output = float(info) + 1
        print(output)
else:
    for i in range(len(info)):
        print(info[-1-i], end="")
 