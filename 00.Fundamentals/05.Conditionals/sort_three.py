# a = int(input())
# b = int(input())
# c = int(input())

# if a >= b and a >= c:
#     if b >=c:
#         print (a, b, c)
#     else:
#         print (a, c, b)
# elif b >= a and b >= c:
#     if a >= c:
#         print (b, a, c)
#     else: 
#         print (b, c, a)
# elif c >= a and c >= b:
#     if a >= b:
#         print (c, a, b)
#     else:
#         print (c, b, a)


# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
 

n1 = 1
n2 = 2
n3 = 3

first = -1000
second = -1000
third = -1000
 
if n1 > first:
    third = second
    second = first
    first = n1
elif n1 > second:
    third = second
    second = n1
elif n1 > third:
    third = n1
 
if n2 > first:
    third = second
    second = first
    first = n2
elif n2 > second:
    third = second
    second = n2
elif n2 > third:
    third = n2
 
if n3 > first:
    third = second
    second = first
    first = n3
elif n3 > second:
    third = second
    second = n3
elif n3 > third:
    third = n3
 
# Print the new values of the three variables
print(first, second, third)