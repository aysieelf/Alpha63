type_input = input()
value_input = input()

if type_input == 'integer' or type_input == 'real':
    value_input = float(value_input) + 1
    if value_input.is_integer():
        print(int(value_input))
    else:
        print(f'{value_input:.2f}')
elif type_input == 'text':
    value_input = value_input + '*'
    print(value_input)