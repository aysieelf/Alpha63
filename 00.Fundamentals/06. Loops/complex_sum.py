count = int(input())
x = float(input())
s = 1
factorial = 1

for n in range(1, count+1):
    factorial = factorial * n
    s = s + factorial/(x**n)

print (f'{s:.5f}')
