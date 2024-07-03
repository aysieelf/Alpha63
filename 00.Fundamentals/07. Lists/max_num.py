n = int(input())
temp_sum = 0
max_sum = 0

for i in range(n):
    temp_num = int(input())
    temp_sum = temp_sum + temp_num
    if temp_sum < 0:
        temp_sum = 0
    if temp_sum >= max_sum:
        max_sum = temp_sum

print(max_sum)
