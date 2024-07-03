halfL_bottles = int(input())
oneL_bottles = int(input())

halfL_bottles_deposit = 0.1 * halfL_bottles
oneL_bottles_deposit = 0.25 * oneL_bottles

sum = halfL_bottles_deposit + oneL_bottles_deposit
print(f'{sum:.2f}')