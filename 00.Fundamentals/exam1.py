
# 0 - tails - Beers!
#
# 1 - heads - Party
#
# 2 - coin falls and stays on its edge - Work on the project
#
# 3 - coin does not fall and floats in the air - May the DSA Force be with you!
#
# Input
# 3 3 1 1 3 3 1 1 2
# Output
# 5: May the DSA Force be with you!
# Input
# 1 1 3 3 0 0 2 2 2
# Output
# 9: Work on the project

flips = input().split()
flips = [int(num) for num in flips]

zeros = 0
ones = 0
twos = 0
threes = 0
index = 0
for flip in flips:
    if flip == 0:
        zeros = zeros + 1
        index = index + 1
    elif flip == 1:
        ones = ones + 1
        index = index + 1
    elif flip == 2:
        twos = twos + 1
        index = index + 1
    elif flip == 3:
        threes = threes + 1
        index = index + 1

    if zeros == 3:
        print(f'{index}: Beers!')
        break
    elif ones == 3:
        print(f'{index}: Party')
        break
    elif twos == 3:
        print(f'{index}: Work on the project')
        break
    elif threes == 3:
        print(f'{index}: May the DSA Force be with you!')
        break