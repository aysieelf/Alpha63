# ============================== ex 1
# Input

# The number of small 1 liter bottles in the warehouse - integer number
# The number of big 5 liter bottles in the warehouse - integer number
# The capacity of the truck - integer number

# Output

# the number of small bottles he will deliver.
# -1 if not possible to fill completely the truck.
#
# Sample Tests
# Input
# 3
# 1
# 8

# Output
# 3
#
# s_bottles = int(input())
# b_bottles = int(input())
# capacity = int(input())
#
# if capacity >= b_bottles*5:
#     capacity = capacity - b_bottles*5
# elif capacity < b_bottles*5:
#     taken_b_bottles = capacity // 5
#     capacity = capacity - taken_b_bottles*5
#
# if capacity == s_bottles:
#     print(s_bottles)
# elif capacity > s_bottles:
#     print('-1')
# else:
#     print(capacity)

# ===================================== ex2
# The sentence consists of words, separated by only one space.
# Every word is composed only of lower or uppercase letters.
#
# The rules of Chicken Latin are:
#
#       If a word begins with a vowel (a, e, i, o, u or A, E, I, O, U),
# remove the first letter and append it to the end, then add "che".
# If you have the word “orange” It translates to “rangeoche”
#       If a word begins with a consonant (i.e. not a vowel),
# append "che" to the end of the word.
# For example, the word "chicken" becomes "chickenche".
#       If the word has even number of letters append one more "e" to the end of it.
# Print the translated sentence.
#
# Input

# Hello there Amy

# Output

# Helloche thereche myAche

# Constraints
# The sentence contains only uppercase, lowercase and spaces. Exactly one space between each word.

# Sample tests
# Input
# Welcome to Chepelare
# Output
# Welcomeche tochee Chepelareche
# Input
# He is no spring chicken anymore
# Output
# Hechee sichee nochee springchee chickenche nymoreache

# line = input().split(' ')
# vowels = "a, e, i, o, u, A, E, I, O, U".split(', ')
#
# output = ''
# for word in line:
#     if word[0] in vowels:
#         temp_vowel = word[0]
#         output = output + word[1:] + temp_vowel + 'che'
#     else:
#         output = output + word + 'che'
#
#     if len(word) % 2 == 0:
#         output = output + 'e'
#     output = output + ' '
#
# print(output)


# =================================== ex3
# heaviness is determined by summing all the letters in it.
# The letter value corresponds to the position in the English alphabet -
# where a is 1 and z is 26.
# For example, the word alpha has a weight of 1 + 12 + 16 + 8 + 1 = 38.
# Treat lower- and uppercase letters the same, so a and A both have the value 1.
#
#
# Input
# On the first line, N - the number of words to follow.
# n = int(input())
#
# heaviest_sum = 0
# heaviest_word = ''
# for i in range(n):
#     temp_sum = 0
#     word = input()
#     for j in word.lower():
#         temp_sum = temp_sum + (ord(j) - 96)
#     if temp_sum > heaviest_sum:
#         heaviest_sum = temp_sum
#         heaviest_word = word
#
# print(heaviest_sum, heaviest_word)
