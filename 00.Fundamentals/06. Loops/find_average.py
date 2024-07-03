# Input
# On the first line, you will receive N - the number of the values you must read
# On the next N lines you will receive numbers.
# Output
# On the only line of output, print the average with two digits after the decimal point.

# Input
# 3
# 2.5
# 1.25
# 3
# Output
# 2.25

count = int(input())
total = 0

for i in range(count):
    n = float(input())
    total = total + n

average = total / count
print(f'{average:.2f}')