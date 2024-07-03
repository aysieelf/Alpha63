# Input
# 3
# 1,2,3,4,5
# 1,2,8,9,9
# 1,2,2,3,2
# Output
# true
# true
# false

# n = int(input())

# for i in range(n):
#     line = input().split(",")
#     length = len(line)
#     prev_num = 0
#     for j in range(len(line)):
#         if int(line[j]) < prev_num:
#             print("false")
#             break
#         elif int(line[j]) >= prev_num and (j+1) == length:
#             print("true")
#         prev_num = int(line[j])


n = int(input())
for i in range(n):
    x = 'true'
    line = input().split(",")
    prev_num = int(line[0])
    for j in line[1:]:
        next_num = int(j)
        if next_num < prev_num:
            x = 'false'
        prev_num = int(j)
    print(x)
