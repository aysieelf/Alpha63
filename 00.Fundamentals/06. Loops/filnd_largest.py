# input
# 6
# 9
# 11
# 3
# 2
# 1
# 8
# Output
# 11, 9 and 8


count = int(input())

number = 0
largest = -500
second_largest = -500
third_largest = -500

for i in range(count):
    number = int(input())
    if number >= largest:
        third_largest = second_largest
        second_largest = largest
        largest = number
    elif number >= second_largest:
        third_largest = second_largest
        second_largest = number
    elif number >= third_largest:
        third_largest = number

print(f'{largest}, {second_largest} and {third_largest}')
        

