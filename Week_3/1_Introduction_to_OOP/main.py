from product import Product
from shopping_cart import ShoppingCart

cheese = Product('Cheese', 8.00)
wine = Product('Wine', 12.50)

cart = ShoppingCart()

# we know that this method expects a 'Product'
cart.add_product(cheese)
cart.add_product(wine)
cart.add_product(wine)

# we know this method returns a 'float'
total_price = cart.total_price() 
print(total_price)