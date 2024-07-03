# list_a1 = input()
# list_a2 = input()

# output = ''
# if list_a1 == list_a2:
#     output = 'equal'

# count = min(len(list_a1), len(list_a2))
# if output == '':
#     for i in range(count):
#             if list_a1[i] == list_a2[i]:
#                 continue
#             elif list_a1[i] < list_a2[i]:
#                 output = 'first'
#                 break
#             elif list_a2[i] < list_a1[i]:
#                 output = 'second'
#                 break

# if output == '':
#     if len(list_a1) < len(list_a2):
#         output = 'first'
#     elif len(list_a2) < len(list_a1):
#         output = 'second'
    
# print(output)


a1 = input()
a2 = input()
 
if a1 == a2:
    print('equal')
elif a1 < a2:
    print('first')
else:
    print('second')