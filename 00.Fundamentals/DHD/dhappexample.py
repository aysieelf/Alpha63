
products = ['01.Potato' , '02.Fish', '03.Apple', '04.Orange']
 
print('Here are our products: ')
print(products)
print()
 
# Think and test what is the reason to create these variables outside of the loop?
orders = []
help_requests = []
while True:
    print('''======
          Menu: Dial only one digit:
          1 - create order
          2 - list of your orders
          3 - request help with an order
          0 - leave the program''')
 
    digit_dialed = input()
    if digit_dialed == '1':
        print('Enter 2 digit product code or 00 to finish the order')
        print(f'Here are the products and their codes: {products}')
 
        new_order = ''
 
        while True:
            # We need to update/take the input from the user on each iteration
            input_product_code = input()
            # Now we have to check what is the input and act accordingly
            if input_product_code == '01':
                print('Adding Potato to the order')
            elif input_product_code == '02':
                print('Adding Fish to the order')
            elif input_product_code == '03':
                print('Adding Apple to the order')
            elif input_product_code == '04':
                print('Adding Orange to the order')
            elif input_product_code == '00':
                print('The order is finished')
                # We need to save the new order into orders list and exit this loop
                orders.append(new_order.strip()) # .strip() removes all the spaces before and after the string
                break
            # If none of the above was true then the code is not valid
            else:
                print('Wrong code')
                # We must use continue otherwise the wrong code will be included into the new order
                continue
 
            new_order += input_product_code + ' ' 
 
    elif digit_dialed == '2':
        if not orders: # not orders will return True if it is an empty list []
            print('You have no orders')
        else:
            print('Here are your orders:')
            for i in range(len(orders)):
                print('Order #:', i, 'Order:', orders[i])
    elif digit_dialed == '3':
        print('''Please enter the number of your order 
          which you need help with 
          and one of our representatives will contact you: ''')
        number_of_the_order = int(input()) # TODO validate correct (existing) order number
        help_requests.append(number_of_the_order)
    elif digit_dialed == '0':
        print('Thank you for using our program!')
        print('Summary of your interaction: ')
        print('Orders: ', orders)
        print('Help requests: ', help_requests)
        break
    else:
        print('Wrong command. Please enter a valid command!')