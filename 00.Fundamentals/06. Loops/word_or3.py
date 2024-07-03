n = int(input())

output_words = ''
sum = 0
previous_text = input()

if previous_text.isdigit():
    sum = int(previous_text)
else:
    output_words = previous_text

for i in range(1, n):
    text = input()
    if text[-1].isdigit():
        if not previous_text[-1].isdigit():
            print(output_words)
            output_words = ''
        sum = sum + int(text)
    else:
        if previous_text[-1].isdigit():
            print(sum)
            sum = 0
            output_words = text
        elif not previous_text[-1].isdigit():
            output_words = output_words + '-' + text
    previous_text = text

if (output_words != ''):
    print(output_words)
else:
    print(sum)




# n = int(input())

# output_words = ""
# sum = 0  
# previous_text = input()
# counter = n - 1

# while counter:
#     text = input()  
#     counter = counter - 1  # Decrement the counter by 1

#     if previous_text[-1].isdigit() and text[-1].isdigit():
#         previous_text = str(int(previous_text) + int(text))
#     elif previous_text[-1].isdigit() and text[-1].isalpha():
#         print(previous_text)
#         previous_text = text
#     elif previous_text[-1].isalpha() and text[-1].isalpha():
#         previous_text += "-" + text
#     elif previous_text[-1].isalpha() and text[-1].isdigit():
#         print(previous_text)
#         previous_text = text
#     elif not text.isalnum():
#         print(previous_text)
#         print(text)
#         previous_text = input()
#         counter -= 1  # Decrement the counter by 1

# print(previous_text)