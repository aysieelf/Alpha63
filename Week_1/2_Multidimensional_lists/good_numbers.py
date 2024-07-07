n1, n2 = input().split()
n1, n2 = int(n1), int(n2)

counter = 0
for num in range(n1, n2+1):
    num = str(num)
    x = True
    for i in num:
        if i != "0":
            if int(num) % int(i) != 0:
                x = False
    if x:
        counter += 1
print(counter)
