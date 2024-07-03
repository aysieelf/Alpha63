product1 = '01. Potato'
product2 = '02. Fish'
product3 = '03. Apple'
product4 = '04. Orange'
product5 = '05. Milk'
product6 = '06. Music'

#MAIN MENU

print('''Main menu:
      1. Make an order
      2. List all user orders 
      3. Request help with an order 
      4. Request to cancel an order
      0. Exit the main menu and the program''')

menu_choice = input('Please enter a digit to proceed: ')

length_menu_choice = len(menu_choice) == 1
digits_menu_choice = menu_choice.isdigit()

if not length_menu_choice:
    print('Please, enter only 1 digit.')

if not digits_menu_choice:
    print('Please, enter only digits from 0 to 4')

if int(menu_choice) < 0 or int(menu_choice) > 4:
    print('Please, enter only digits from 0 to 4')

#1. MAKE AN ORDER

if menu_choice == '1':
    print()
    print('Enter a 2 digit product code or 00 to finish the order')
    print()
    print('''Here are the products and their codes:
          01. Potato
          02. Fish
          03. Apple
          04. Orange
          05. Milk
          06. Music''')

product_choice = input('Please enter a 2 digit code:')
