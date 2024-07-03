# n = int(input())
# numbers = []
# frequency = []
# best_num = 0
#
# for i in range(n):
#     numbers.append(int(input()))
#
# for j in numbers:
#     temp_freq = numbers.count(j)
#     frequency.append(temp_freq)
#
# max_frequency = 0
#
# for x in range(len(frequency)):
#     if frequency[x] > max_frequency:
#         best_num = numbers[x]
#         max_frequency = frequency[x]
#
# print(best_num)
# #============================================================================================

# Prompt the user to input an integer 'n'
n = int(input())
numbers = []
for i in range(10):
    numbers.append(0)

for i in range(n):
    next_num = int(input())
    numbers[next_num - 1] += 1

max_value = max(numbers)
best_num = 10

for j in range(10):
    if numbers[j] == max_value and best_num > j + 1:
        best_num = j + 1

print(best_num)