# Array Search
# Given an array of integers, some elements appear twice and others appear once.
# Each integer is in the range of [1, N], where N is the number of elements in the array.
#
# Find all the integers of [1, N] inclusive that do NOT appear in this array.
#
# Input
# Read from the standard input:
#
# There is one line of input, containing N amount of integers, seperated by a comma (",")
# Output
# Print to the standard output:
#
# There is one line of output, containing the sorted integers, seperated by a comma (",")
# Constraints
# N will always be in the range of [5, 1000]
# Sample Tests
# Input
# 1,2,3,3,5
# Output
# 4
# Input
# 4,3,2,7,8,2,3,1
# Output
# 5,6
# Input
# 1,1,1,1,1,1,1,1
# Output
# 2,3,4,5,6,7,8


lst_numbers = [int(x) for x in input().split()]

num_max = max(lst_numbers)

lst_all_numbers = [i for i in range(1, num_max)]


