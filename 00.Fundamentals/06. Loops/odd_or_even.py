# Input
# 5
# 2 1 1 6 3
# Output
# yes 6
# Explanation
# The elements are: 2 1 1 6 3
# The indexes are:  1 2 3 4 5
# The products are: 2 * 1 * 3 and 1 * 6. Both are equal to 6.

# Input
# 5
# 4 3 2 5 2
# Output
# no 16 15

count = int(input())
numbers = input().split()
odd_numbers = 1
even_numbers = 1
number = 0

for i in range(1, count+1):
    number = int(numbers[i-1])
    if i % 2 == 1:
        odd_numbers = odd_numbers * number
    elif i % 2 == 0:
        even_numbers = even_numbers * number

if odd_numbers == even_numbers:
    print(f'yes {odd_numbers}')
else:
    print(f'no {odd_numbers} {even_numbers}')

# n = int(input())
 
 
# # Initialize variables for odd and even products, both starting at 1
# odd = 1
# even = 1
 
# # Loop for i in range(1, n+1) to get the numbers
# for i in range(1, n+1):
#     # Get the current number and parse it to int
#     current_number = int(input())
#     # Check if the current value of i (the variable of the for loop) is even
#     if i % 2 == 0:
#         # If i is even, multiply the even product by current number
#         even *= current_number
 
#     else:
#         # If i is odd, multiply the odd product by current number
#         odd *= current_number


# # Check if the odd product is equal to the even product
# if odd == even:
#     # If they are equal, print "yes" and the value of either odd or even (they are the same)
#     print("yes", odd)
 
# else:
#      # If they are not equal, print "no" and both the odd and even products
#     print("no", odd, even)