string = ''
# lenght = 0
longest_lenght = 0
# longest_food = ''

while string != 'END':
    string = input()
    lenght = len(string)
    if lenght >= longest_lenght and string != 'END':
        longest_lenght = lenght
        longest_food = string

print(longest_food)



# string = input()
# longest_lenght = 0
# longest_food = ""
 
# while not string == "END":
#     if len(string) >= longest_lenght:
#         lenght = len(string)
#         longest_food = string
#     string = input()
 
# print(longest_food)