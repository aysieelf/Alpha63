count = int(input())
previous_number = int(input())
numbers = {}

for i in range(count-1):
    numbers[i] = int(input())

for i in numbers:
    if i < (count-1):
        next_number = numbers.get(i)
        if previous_number < next_number:
            print (f'{previous_number}<', end='')
        elif previous_number == next_number:
            print (f'{previous_number}=', end='')
        else:
            print (f'{previous_number}>', end='')
        previous_number = next_number

print(next_number)


count = int(input())
previous_number = int(input())
 
output = str(previous_number)
 
for i in range(count-1):
    next_number = int(input())
    if previous_number == next_number:
        output = output + "="
    elif previous_number > next_number:
        output = output + ">" 
    else:
        output = output + "<"
    output = output + str(next_number)
    previous_number = next_number

print(output)