product_one = '01.Potato'
product_two = '02.Fish'
product_three = '03.Apple'

menu = ('''Menu:
                     1 - Create Order''')
print(menu)

choice_in_menu = int(input('Dial only one digit:'))

print(f'''Here are our products:
      {product_one}
      {product_two}
      {product_three}''')

choosing_products = 'Enter the 2 digit product code to add it to the order.'
print(choosing_products)

code_from_the_user_input1 = input()
print(f'Product {code_from_the_user_input1} was added to the order!')
code_from_the_user_input2 = input()
print(f'Product {code_from_the_user_input2} was added to the order!')
code_from_the_user_input3 = input()
print(f'Product {code_from_the_user_input3} was added to the order!')

print()

thank_you = "Thank you for using our program!"
summary = "Summary of your interaction:"
print(thank_you)
print(summary)

print (f'Orders: 1 order containing {code_from_the_user_input1}, {code_from_the_user_input2}, {code_from_the_user_input3}')
