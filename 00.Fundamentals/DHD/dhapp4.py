products = ['01.Potato', '02.Fish', '03.Apple', '04.Orange']

order_list = []
help_request = []
menu_choice = ''

while True:
    print('''Menu:
Please enter only one digit: 
    1 - create order
    2 - list of your orders
    3 - request help with an order
    0 - leave the program''')
    menu_choice = int(input())

    if menu_choice == 1:
        print(f'Here are our products and their codes: {products}')
        print('Enter 2 digit product code or 00 to finish the order')
        
        while True:
            order = input()
            if order == '00':
                if order_list == []:
                    print('You have no orders.')
                else:
                    print('Here are your orders:', ','.join(order_list))
                    print()
                    break
            elif order not in ['01', '02', '03', '04', '00'] or order == 0:
                print('Wrong code')
            else:
                for i in products:
                    if order in i:
                        order_list.append(order)
                        print(f'Adding {i} to the order')

    elif menu_choice == 2:
        print('Doing list command')
    elif menu_choice == 3:
        print('''Which order do you need help with?
    01. Potato
    02. Fish
    03. Apple
    04. Orange''')
        print('Enter 2 digit product code or 00 to finish with requesting help')
        while True:
            order = input()
            if order == '00':
                if order_list == []:
                    print('You have not added any orders to the list.')
                else:
                    print('Here are your orders that you need assistance with:', ','.join(order_list))
                    print()
                    break
            elif order not in ['01', '02', '03', '04', '00'] or order == 0:
                print('Wrong code')
            else:
                for i in products:
                    if order in i:
                        order_list.append(order)
                        print(f'Adding {i} to the request help list')
    
    elif menu_choice == 0:
        print('Thank you for using our program!')
        print(f'''Summary of your interaction:
    Your order is: {','.join(order_list)}
    You requested help with: {','.join(help_request)}
    ''')
    else:
        print('Wrong command. Please enter a valid command!')


