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


# integers = input().split(',')

# n = len(integers)
# for i in range(1, n+1):
#     if not str(i) in integers:
#         print(i, end='')
#         break


# for ii in range (i+1, n+1):
#     if not str(ii) in integers:
#         print(f',{ii}', end='')


# Get the line input - a string containing the values separated by commas (,)
# Then use the split(",") method to split this string into a list of elements.
# # Store the resulting list in the variable line.
# integers = input().split(',')
 
# # Initialize an empty list called res, which will be used to store missing numbers.
# res = []
 
# # Loop to iterate through the numbers from 1 to the length of the line list, inclusive.
# for i in range(1, len(integers)+1):
#     # Check if the string representation of 'i' (str(i)) is not in the 'line' list.
#     if not str(i) in integers:
#         # If 'i' is not found in 'line', it is a missing number, so add its string representation to the 'res' list.
#         res.append(str(i))

# new_res = (",".join(res))
# print(new_res)
# # Join the elements in the 'res' list using commas (,) and print the result.
# # Keep in mind join(',') works with list of strings only

integers = input().split(',')

numbers = []

for i in integers:
    numbers.append(int(i))

output = []
for ii in range(1, len(numbers)+1):
    if ii not in numbers:
        output.append(ii)

output_string = ''
for iii in output:
    output_string = output_string + str(iii) + ','

print(output_string.strip(','))
