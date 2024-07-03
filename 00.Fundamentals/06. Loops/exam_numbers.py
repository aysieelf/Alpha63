x = int(input())
y = int(input())
t = int(input())

for i in range(x,y+1):
    number = str(i)
    working_t = int(number[0]) + int(number[1]) + int(number[2])
    if working_t == t:
        print (number)


x = int(input())
y = int(input())
t = int(input())
 
for i in range(x, y+1):
    number = str(i)
    if (int(number[0]) + int(number[1]) + int(number[2])) == t:
        print(i)