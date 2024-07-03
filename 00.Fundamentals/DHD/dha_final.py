# -answers calls from customers

products = ['01. Sunrise Special Burger',
            '02. Morning Glory Veggie Burger',
            '03. Bacon & Egg Breakfast Burger',
            '04. Classic Cheeseburger',
            '05. Breakfast Burrito Burger',
            '06. Signature Breakfast Shake']

all_orders = []
one_order = ''
help_requests = []
cancel_requests = []
menu_choice_x = 'false'

print('Welcome to Sunrise Burgers!')
while menu_choice_x == 'false':
    print('''This is the Main Menu.
Please, enter only one digit to select a command:
  1. Make an order
  2. List all orders
  3. Request help with an order
  4. Request to cancel an order
  0. To exit Menu and the program''')
    menu_choice = int(input())
    if menu_choice not in [1, 2, 3, 4, 0]:
        print('Please, enter a valid number!')
    else:
        menu_choice_x = 'true'

    y = 'true'
    if menu_choice == 1:
        print('''Enter 2 digit product code 
or 00 to finish the order.''')
        print('Here are the products and their codes:')
        for x in products:
            print(x)
        while y == 'true':
            temp_order = input()
            if temp_order not in ['01', '02', '03', '04', '05', '06', '00']:
                print('Please, enter a valid two-digit code!')
            elif temp_order in ['01', '02', '03', '04', '05', '06']:
                if temp_order == '01':
                    print(f'You added {products[0]} to the order.')
                    one_order = one_order + '01' + ' '
                elif temp_order == '02':
                    print(f'You added {products[1]} to the order.')
                    one_order = one_order + '02' + ' '
                elif temp_order == '03':
                    print(f'You added {products[2]} to the order.')
                    one_order = one_order + '03' + ' '
                elif temp_order == '04':
                    print(f'You added {products[3]} to the order.')
                    one_order = one_order + '04' + ' '
                elif temp_order == '05':
                    print(f'You added {products[4]} to the order.')
                    one_order = one_order + '05' + ' '
                elif temp_order == '06':
                    print(f'You added {products[5]} to the order.')
                    one_order = one_order + '06' + ' '
            elif temp_order == '00':
                print('Thank you for your order!')
                all_orders.append(one_order.strip(' '))
                one_order = ''
                y = 'false'
                menu_choice_x = 'false'
                print()

    elif menu_choice == 2:
        if len(all_orders) == 0:
            print('You have no orders.')
        else:
            print('Here are your orders:')
            for i in range(1, len(all_orders) + 1):
                print(f'Order #: {i} Order: "{all_orders[i - 1]}"')
            menu_choice_x = 'false'
            print()

    elif menu_choice == 3:
        z = 'false'
        print('''Please, enter the number of your order 
which you need help with and one of 
our representatives will contact you:''')
        print()
        print('Here are your orders:')
        for ii in range(1, len(all_orders) + 1):
            print(f'Order #: {ii} Order: "{all_orders[ii - 1]}"')
        while z == 'false':
            temp_help = input('Order #: ')
            if int(temp_help) > (len(all_orders) + 1):
                print('Please, enter a valid number of your order.')
            elif int(temp_help) < (len(all_orders) + 1):
                print(f'Help with order # {temp_help} requested!')
                help_requests.append(temp_help)
                print()
                menu_choice_x = 'false'
                z = 'true'

    elif menu_choice == 4:
        xx = 'false'
        print('''Please, enter the number of your order 
        which you want to cancel and one of our
        representatives will review and remove it for you:''')
        print()
        print('Here are your orders:')
        for iii in range(1, len(all_orders) + 1):
            print(f'Order #: {iii} Order: "{all_orders[iii - 1]}"')
        while xx == 'false':
            temp_cancel = input('Order #: ')
            if int(temp_cancel) > (len(all_orders) + 1):
                print('Please, enter a valid number of your order.')
            elif int(temp_cancel) < (len(all_orders) + 1):
                print(f'Cancellation of order # {temp_cancel} requested!')
                cancel_requests.append(temp_cancel)
                print()
                menu_choice_x = 'false'
                xx = 'true'

    elif menu_choice == 0:
        print('Thank you for using our program!')
        print('Summary of your interaction:')
        print()
        print('Here are your orders:')
        for j in range(1, len(all_orders) + 1):
            print(f'Order #: {j} Order: "{all_orders[j - 1]}"')
        if len(help_requests) > 0:
            print()
            print('Here are the orders you requested help with:')
            for k in help_requests:
                print(f'Order #: {k}')
        if len(cancel_requests) > 0:
            print()
            print('Here are the orders you requested to be removed:')
            for o in cancel_requests:
                print(f'Order #: {o}')

# Implement the Request Order Cancellation command
# Print message: "Please enter the number of your order which you want to cancel and one of our
# representatives will review and remove it for you: "
# Valid order number is required - (see the previous command)
# Add it to the list of cancellation requests

# Implement the Exit the Program command
# Print "Thank you for using our program!",
# "Summary of your interaction: "
# and then the orders,
# help requests,
# and cancellation requests made by the user.
