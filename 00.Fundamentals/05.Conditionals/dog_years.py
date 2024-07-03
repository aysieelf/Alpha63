hy = int(input())

if hy >= 1 and hy <= 15:
    if hy == 1:
        print(10)
    elif hy == 2:
        print(20)
    elif hy > 2:
        print((hy - 2) * 4 + 20)
else:
    print('Invalid number!')




    # or

dog_years = int(input())

if 1 <= dog_years <= 2:
    human_years = dog_years * 10
else:
    human_years = (dog_years - 2) * 4 + 20

print(human_years)