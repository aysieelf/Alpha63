n = int(input())

numbers = [input() for _ in range(n)]

unique_numbers = set()
for el in numbers:
    unique_numbers.add(el)

count = 0
number = 0
for num in unique_numbers:
    if numbers.count(num) > count:
        count = numbers.count(num)
        number = num

print(f"{number} ({count} times)")


