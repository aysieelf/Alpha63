count = int(input())
discount = 0.65
for i in range(count):
    price = float(input())
    new_price = price - (price * discount)
    print (f'{round(new_price,2):.2f}')



n = int(input())

for i in range(n):
    p = float(input())
    d = p * 0.35
    print(f'{d:.2f}')
