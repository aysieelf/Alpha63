count = int(input())
max_number = -200

for i in range(count):
    number = int(input())
    if number > max_number:
        max_number = number

print(max_number)
