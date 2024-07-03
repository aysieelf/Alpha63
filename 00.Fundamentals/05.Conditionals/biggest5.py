a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())

if (a >= b) and (a >= c) and (a >= d) and (a >= f):
    print (a)
elif (b >= a) and (b >= c) and (b >= d) and (b >= f):
    print (b)
elif (c >= a) and (c >= b) and (c >= d) and (c >= f):
    print (c)
elif (d >= a) and (d >= b) and (d >= c) and (d >= f):
    print (d)
else:
    print (f)