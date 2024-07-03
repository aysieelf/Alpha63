l = input()
r = input()

if (l >= 'a') and (l <= 'h') and (r >= '1') and (r <= '8'):
    if (r in '1357') and (l in 'aceg'):
        print('dark')
    elif (r in '2468') and (l in 'bdfh'):
        print('dark')
    elif (r in '1357') and (l in 'bdfh'):
        print('light')
    elif (r in '2468') and (l in 'aceg'):
        print('light')
else:
    print('Invalid input!')


label = input()
rank = int(input())

label = ord(label)
# print(label)

if (label % 2) == 1 and (rank % 2) == 1:
    print('dark')
elif (label % 2) == 0 and (rank % 2) == 1:
    print ('light')
elif (label % 2) == 1 and (rank % 2) == 0:
    print ('light')
elif (label % 2) == 0 and (rank % 2) == 0:
    print ('dark')
else:
    print ('Invalid label or rank!')