n = int(input())

output_words = ''
sum = 0

for i in range(n):
    text = input()
    if text.isdigit():
        sum = sum + int(text)
    else:
        output_words = output_words + text + '-'


if output_words == '':
    output_words = 'no words-'

print (f'{output_words[:-1:]}\n{sum}')

n = int(input())

output_words = ""
sum = 0

for i in range(n):
    text = input()
    if text.isdigit():
        sum += int(text)
    else:
        output_words += text + "-" 

if len(output_words) == 0:
    output_words = "no words"
 
print(f'{output_words.strip("-")}\n{sum}')
