three_digit_number = input('Please, enter a three digit number: ')

if three_digit_number.isdigit() == False :
    print('Input must contain digits only!')
elif len(three_digit_number) != 3:
    print('Invalid number of characters in the input: must be 3.')
else:
    print('Input accepted.')