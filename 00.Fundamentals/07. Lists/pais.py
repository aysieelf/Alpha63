# t_sum = int(input())
# nums = input().split(' ')
# nums_int = []
#
# for i in nums:
#     nums_int.append(int(i))
#
# pairs = 'false'
#
# for i in nums_int:
#     for j in range(len(nums_int)):
#         if i + nums_int[j] == t_sum and j != nums_int.index(nums_int[i]):
#             print(f'{i},{nums_int[j]}')
#             pairs = 'true'

n = int(input())
# Get the next input and split it
nums = input().split(' ')
nums_int = []
# Transform the list of strings to int and save it to lst
for i in nums:
    nums_int.append(int(i))

x = 'false'

for i in range(len(nums_int)):
    for j in range(i+1, len(nums_int)):
        if nums_int[i] + nums_int[j] == n:
            print(f'{nums_int[i]},{nums_int[j]}')
            x = 'true'

if x == 'false':
    print('no pairs')
