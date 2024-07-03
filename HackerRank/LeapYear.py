def is_leap(variable):
    leap = False
    if variable % 4 == 0:
        if variable % 100 != 0:
            leap = True
        else:
            if variable % 400 == 0:
                leap = True
    return leap


year = int(input())
print(is_leap(year))
