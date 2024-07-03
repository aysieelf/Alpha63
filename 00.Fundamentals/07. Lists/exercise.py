# products = [
#     'apples', 
#     'bananas', 
#     'coffee', 
#     'cheese', 
#     'sausages', 
#     'spaghetti']

# while True:
#     search = input()
#     if search == '0':
#         break
#     matches = []
#     for product in products:
#         if search in product:
#             matches.append(product)
#     count = len(matches)
#     if count == 0:
#         print(f'No matches found for {search}!')
#     else:
#         print(f'{count} matches found for {search}:')
#         for match in matches:
#             print('  ', match)

# ---------------------------------------------------------

# Read the input
# Sort the letters alphabetically
# Print the sorted letters on the console
 
# Input:
# 5
# b
# c
# a
# d
# e

# count = int(input())
# newlist = []

# for i in range(count):
#     add = input()
#     newlist.append(add)

# print(sorted(newlist))

# ---------------------------------------------------------

# Read the input
# Separate the elements into a list
# Find the duplicate letters
 
# Input:
# a,b,c,a,f,f 

# letters = input().split(',')
# seen = []

# # for i in letter:
# #     if letter.count(i) == 2:
# #         print(f'{i} is found {letter.count(i)} times')
        

# for letter in letters:
#     if letter in seen:
#         print(f'{letter} is duplicate!')
#     else:
#         seen.append(letter)





numbers = [1, 2, 3, 4, 5] 
idx = 3

element = numbers.get(idx)
print(element)

