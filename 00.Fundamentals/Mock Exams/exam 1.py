# # ========================= ex1
# n = input()
#
# sum_digits = 0
# x = 'false'
#
# while x == 'false':
#     for i in n:
#         if i != '-' and i != '.':
#             sum_digits = sum_digits + int(i)
#     if sum_digits < 10:
#         x = 'true'
#     else:
#         n = str(sum_digits)
#         sum_digits = 0
#
# print(sum_digits)

# ========================= ex2 - primes

n = int(input())

list1 = []
for i in range(1, n+1):
    list1.append(i)

list_primes = []
for j in list1:
    if j == 1:
        list_primes.append(j)
    else:
        for k in range(2, (j//2)+1):
            if (j % k) == 0:
                break
        else:
            list_primes.append(j)

for x in list_primes:
    for y in range(1, x+1):
        if y in list_primes:
            print(1, end='')
        else:
            print(0, end='')
    print()

# ========================= ex3
#
# A balanced number is a 3-digit number whose second digit
# is equal to the sum of the first and last digit.
# You should stop when an unbalanced number is given.
counter = 0
x = 'balanced'
lst = []
sum_of_nums = 0
while counter < 1000 and x == 'balanced':
    counter = counter + 1
    num = input()
    lst = []
    for i in num:
        lst.append(i)
    if int(lst[0]) + int(lst[2]) == int(lst[1]):
        sum_of_nums = sum_of_nums + int(num)
    elif int(lst[0]) + int(lst[2]) != int(lst[1]):
        print(sum_of_nums)
        x = 'not balanced'





# докато x стане, че не е балансд