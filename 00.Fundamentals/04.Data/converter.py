mpg = int(input())
one_liter = 4.54
one_km = 1.6
km = mpg * one_km
litre = one_liter/km
lpkm = litre * 100
print(f'{int(lpkm)} litres per 100 km')
