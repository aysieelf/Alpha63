l = ord(input()) - 96
r = int(input())

if (l % 2 == 1 and r % 2 == 1) or (l % 2 == 0 and r % 2 == 0) :
    print('dark')
else:
    print('light')

