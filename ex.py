# the_dict = {'Steven': 21, 'Alice': 23, 'John': 18}
#
# print(the_dict.items())
# val_sort = sorted(the_dict.items(), key=lambda x: x[1])
# print(val_sort)
# #

# lst_values = sorted(the_dict.values())
# sorted_dict = {}
#
# while lst_values:
#     for key, value in the_dict.items():
#         if not lst_values:
#             break
#         if value == lst_values[0]:
#             sorted_dict[key] = value
#             lst_values.remove(lst_values[0])
#
# sorted_list = [(k, v) for k, v in sorted_dict.items()]
#
# print(sorted_dict)
# print(sorted_list)