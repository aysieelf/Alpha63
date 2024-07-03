import  math

a = float(input())
b = float(input())
c = float(input())

d = (b * b) - (4 * a * c)

x1 = (-b - math.sqrt(d)) / (2 * a)
x2 = (-b + math.sqrt(d)) / (2 * a)

x1 = x1 + 0
x2 = x2 + 0

print(f'x1={x1:.1f}')
print(f'x2={x2:.1f}')