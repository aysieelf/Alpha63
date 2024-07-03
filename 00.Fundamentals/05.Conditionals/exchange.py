# exchanges their values if the first one is greater than the second one.
# Input
# On the first line, you will receive the value of A
# On the second line, you will receive the value of B
# Output
# On the only output line, print the values of the two variables, separated by a whitespace


a = float(input())
b = float(input())

a = int(a) if a.is_integer() else float(a)
b = int(b) if b.is_integer() else float(b)

if a > b:
    print(b, a)
else:
    print(a, b)



a = input()
b = input()

if a > b:
    print (b, a)
else:
    print (a, b)