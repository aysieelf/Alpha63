# nput
# 3
# 2
# 5
# 1
# Output
# min=1.00
# max=5.00
# sum=8.00
# avg=2.67

count = int(input())
min = 1000
max = -1000
sum = 0

for i in range(count):
    number = float(input())
    sum = sum + number
    if number < min:
        min = number
    if number > max:
        max = number


avg = sum / count
print(f'''min={min:.2f}
max={max:.2f}
sum={sum:.2f}
avg={avg:.2f}''')