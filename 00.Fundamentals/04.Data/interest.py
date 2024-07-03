n = int(input()) #deposit

year1 = n * 1.05
year2 = year1 * 1.05
year3 = year2 * 1.05

print(f'{round(year1,2):.2f}')
print(f'{round(year2,2):.2f}')
print(f'{round(year3,2):.2f}')
