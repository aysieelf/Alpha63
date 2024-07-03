# Longest Sequence of Equal
# Description
# length of the maximal sequence of equal elements in an array of N integers.


# Print the length of the maximal sequence

# Sample tests
# Input
# 10
# 2
# 1
# 1
# 2
# 3
# 3
# 2
# 2
# 2
# 1
# Output
# 3

n = int(input())

lst = []
max_seq = 0
count = 0
 
for _ in range(n):
    lst.append(input())
 
bucket = []
for i in lst:
    if bucket == i:
        count += 1
        if max_seq <= count:
            max_seq = count
    else:
        bucket = i
        count = 1
 
print(max_seq)

# =================================================================================

n = int(input())
 
max_seq = 0
count = 1
bucket = ''

for i in range(n):
    number = input()
    if bucket == number:
        count = count + 1
        if count > max_seq:
            max_seq = count
    else:
        bucket = number
        count = 1

 
print(max_seq)