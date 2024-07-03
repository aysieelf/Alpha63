# ============================================ ex 1

# moves = input()
# lst = []
#
# for i in moves:
#     lst.append(i)
#
# x = 0
# y = 0
# for j in lst:
#     if j == 'L':
#         x = x - 1
#     elif j == 'R':
#         x = x + 1
#     elif j == 'D':
#         y = y - 1
#     elif j == 'U':
#         y = y + 1
#
# print(f'({x}, {y})')

# ============================================ ex 2
# #
# lst1 = input().split(',')
# lst2 = input().split(',')
#
# output = ''
# for i in lst1:
#     num = lst2.index(i)
#     for j in range(num+1, len(lst2)):
#         if int(lst2[num]) < int(lst2[j]):
#             output = output + lst2[j] + ','
#             break
#     else:
#         output = output + '-1' + ','
#
#
# print(output.strip(','))

# ============================================ ex 3
#
# title = input()
# lst_title = list(title)
# n = int(input())
#
# for i in range(n):
#     word = input()
#     found = True
#     temp_title = lst_title.copy()
#     title_index = 0
#
#     for el in word:
#         while title_index < len(temp_title) and temp_title[title_index] != el:
#             title_index += 1
#
#         if title_index < len(temp_title) and temp_title[title_index] == el:
#             temp_title[title_index] = None  # Mark for removal
#             title_index += 1
#         else:
#             found = False
#             break
#
#     if found:
#         new_lst_title = []
#         for char in temp_title:
#             if char is not None:
#                 new_lst_title.append(char)
#         print(''.join(lst_title))
#     else:
#         print('No such title found!')

# =====================================================================
# line1 = input().split(',')
# line2 = input().split(',')
#
# lst1 = []
# for q in line1:
#     lst1.append(int(q))
#
# lst2 = []
# for w in line2:
#     lst2.append(int(w))
#
# output = ''
#
# for e in lst1:
#     for r in range(len(lst2)):
#         if e == lst2[r]:
#             for t in lst2[r:]:
#                 if t > e:
#                     output = output + str(t) + ','
#                     break
#             else:
#                 output = output + '-1' + ','
#
#
# print(output.strip(','))


# =========================================================
#
# line = list(input())
# n = int(input())
#
# for i in range(n):
#     word = input()
#     temp_line = line.copy()
#     point = 0
#     x = True
#     for el in word:
#         while point < len(temp_line) and el != temp_line[point]:
#             point += 1
#         if point < len(temp_line) and el == temp_line[point]:
#             temp_line[point] = None
#             point += 1
#         else:
#             x = False
#             break
#
#     if x:
#         line = [char for char in temp_line if char is not None]
#         print(''.join(line))
#     else:
#         print("No such title found!")

line = list(input())
n = int(input())

for i in range(n):
    word = input()
    temp_line = line.copy()
    index = 0
    x = True
    for el in word:
        while index < len(temp_line) and el != temp_line[index]:
            index += 1
        if index < len(temp_line) and el == temp_line[index]:
            temp_line[index] = None
            index += 1
        else:
            x = False
            break

    if x:
        line = [char for char in temp_line if char is not None]
        print(''.join(line))
    else:
        print('No such title found!')