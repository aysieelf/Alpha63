input = input()

if input.isdigit() and 2 <= int(input) <= 10:
    print ('yes')
elif input in 'JQKA':
    print ('yes')
else:
    print ('no')


