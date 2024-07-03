t = int(input())
n = int(input())

output = ''
average = 0

for i in range(n):
    word = input()
    sum = 0
    for ii in word.upper():
        sum = sum + ord(ii) - 64
    result = abs(t - sum)
    output = output + word + ' ' + str(result) + '\n'
    average = average + result

average = round(average/n, 2)

print(f'{output}{average:.2f}')



# t = int(input())
# n = int(input())
 
# total_sum = 0
# for i in range(n):
#     word = input()
#     sum = 0
#     for ii in word.upper():
#         sum = sum + ord(ii) - 64
#     print(f"{word} {abs(t - sum)}")
#     sum = sum + abs(t - sum)
 
# print(f"{(sum / n):.2f}")