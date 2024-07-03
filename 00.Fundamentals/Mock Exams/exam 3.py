# n = int(input())
#
# reps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# for i in range(1, n+1):
#     num = int(input())
#     reps[num] = reps[num] + 1
#
# max_reps = max(reps)
#
# for j in range(11):
#     if reps[j] == max_reps:
#         print(j)
#         break

# =============================== ex2

# num = input()
#
# lst = []
# for i in num:
#     lst.append(int(i))
#
# evens_sum = 0
# odds_sum = 0
# for j in lst:
#     if j % 2 == 0:
#         evens_sum = evens_sum + j
#     else:
#         odds_sum = odds_sum + j
#
# if evens_sum > odds_sum:
#     print(f'{evens_sum} energy drinks')
# elif odds_sum > evens_sum:
#     print(f'{odds_sum} cups of coffee')
# else:
#     print(f'{evens_sum} of both')

# =============================== ex3
#
# Alone Numbers
# array
# target == alone
# alone if  a != alone != b

line = input().split(', ')
target = int(input())

lst = []
for _ in line:
    lst.append(int(_))

new_list = [lst[0]]
for i in range(1, len(lst)-1):
    if lst[i] != target:
        new_list.append(lst[i])
    elif lst[i] == lst[i-1] or lst[i] == lst[i+1]:
        new_list.append(lst[i])
    else:
        new_list.append(max(lst[i-1], lst[i+1]))

if len(lst) > 1:
    new_list.append(lst[-1])


print(new_list)

