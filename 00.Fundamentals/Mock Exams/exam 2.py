# # =========================== ex1
# n = input()
# lst = []
# for i in n:
#     lst.append(int(i))
#
# best_num = 0
#
# temp_num = lst[0] + lst[1] + lst[2]
# if temp_num > best_num:
#     best_num = temp_num
# temp_num = lst[0] * lst[1] + lst[2]
# if temp_num > best_num:
#     best_num = temp_num
# temp_num = lst[0] * lst[1] * lst[2]
# if temp_num > best_num:
#     best_num = temp_num
# temp_num = lst[0] + lst[1] * lst[2]
# if temp_num > best_num:
#     best_num = temp_num
#
# print(best_num)

# # =========================== ex2
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(input())
#
# # merging
# first_num = lst[0]
# for j in lst[1:]:
#     print(f"{first_num[1]}{j[0]}", end=' ')
#     first_num = j
# print()
#
# # squashing
# first_num = lst[0]
# for j in lst[1:]:
#     middle_sum = str(int(first_num[1]) + int(j[0]))
#     print(f"{first_num[0]}{middle_sum[-1]}{j[1]}", end=' ')
#     first_num = j

# # =========================== ex3
# w = word
# n = count of words in list
# anagrams = n counts
#
# For each word from WORDS print either:
# "Yes", if the word is an anagram of W;
# "No", if the word is NOT an anagram of W;

w = input()
n = int(input())
lst = []
for x in w:
    lst.append(x)

for i in range(n):
    temp_list = lst.copy()
    anagram = input()
    for j in anagram:
        if j not in temp_list:
            continue
        elif j in temp_list:
            temp_list.remove(j)
    if len(temp_list) == 0:
        print("Yes")
    else:
        print("No")
