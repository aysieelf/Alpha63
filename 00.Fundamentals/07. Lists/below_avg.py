lst = input().split(',')
new_list = []

for x in lst:
    new_list.append(int(x))

smaller = []
bigger = []
average = sum(new_list) / len(new_list)

for x in new_list:
    if x < average:
        smaller.append(str(x))
    elif x > average:
        bigger.append(str(x))

print(f'avg: {average:.2f}\n'
      f'below: {','.join(smaller)}\n'
      f'above: {','.join(bigger)}')

#===================================================
#
# line = input().split(",")
# lst = []
# below = []
# above = []
#
# for el in line:
#     lst.append(int(el))
# avg_in_lst = sum(lst) / len(lst)
#
# for el in lst:
#     if el > avg_in_lst:
#         above.append(str(el))
#     elif el < avg_in_lst:
#         below.append(str(el))
#
# print(f"avg: {avg_in_lst:.2f}\n"
#       f"below: {','.join(below)}\n"
#       f"above: {','.join(above)}")