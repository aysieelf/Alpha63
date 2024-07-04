n, m = input().split()
n, m = int(n), int(m)

lst_2d = []
a = [[2**(i+j) for j in range(m)] for i in range(n)]


len_row = len(a) - 1
len_clm = len(a[0]) - 1

prev_row = 0
prev_clm = 0
row = 0
clm = 0

ttl = 0
while True:
    if ((row == 0 and clm == 0) or
            (row == 0 and clm == len_clm) or
            (row == len_row and clm == 0) or
            (row == len_row and clm == len_clm)):
        ttl += a[row][clm]
        print(ttl)
        break
    else:
        ttl += a[row][clm]
        if row == 0 or (prev_row <= row and row != len_row):
            prev_row = row
            row += 1
        elif row == len_row or (prev_row > row and row != 0):
            prev_row = row
            row -= 1
        if clm == 0 or (prev_clm <= clm and clm != len_clm):
            prev_clm = clm
            clm += 1
        elif clm == len_clm or (prev_clm > clm and clm != 0):
            prev_clm = clm
            clm -= 1