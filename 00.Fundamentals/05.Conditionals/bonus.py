# Write a program that applies bonus score to given score 
# in the range [1…9] by the following rules:

# If the score is between 1 and 3, the program multiplies it by 10.
# If the score is between 4 and 6, the program multiplies it by 100.
# If the score is between 7 and 9, the program multiplies it by 1000.
# If the score is less than or equal to 0 or more than 9, the program prints 
# "invalid score".

score = int(input())

if 1 <= score <= 3:
    print (score * 10)
elif 4 <= score <= 6:
    print (score * 100)
elif 7 <= score <= 9:
    print (score * 1000)
else:
    print ("invalid score")

