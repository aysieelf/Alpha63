# # # 5,3,2,1
# # # 2
# # # Output
# # # 2,1,5,3

# numbers = input().split(',')
# n = int(input())

# if n > len(numbers):
#     n = n - len(numbers)

# new_list = []
# zero = 0
# for i in range(len(numbers)):
#     if (i + n) < len(numbers):
#         new_list.insert(i, numbers[i+n])
#     elif (i + n) == len(numbers):
#         new_list.insert(i, numbers[zero])
#     else:
#         zero = zero + 1
#         new_list.insert(i, numbers[zero])

# # print(','.join(new_list))

# lst = input().split(",")
# rota = int(input())
 
# for i in range(rota):
#     lst = lst[1:] + [lst[0]]
 
# print(",".join(lst))


numbers = input().split(',')
n = int(input())

for i in range(n):
    numbers = numbers[1:] + [numbers[0]]

print(','.join(numbers))

