from product import Product


class ShopingCartItem:
    def __init__(self, product: Product, quantity=1):
        self.product = product
        self.quantity = quantity


class ShoppingCart:
    def __init__(self):
        self.items: list[ShopingCartItem] = []

    def add_product(self, product: Product):
        existing_item = None

        for item in self.items:
            if item.product.name == product.name:
                existing_item = item

        if existing_item is not None:
            existing_item.quantity += 1
        else:
            new_item = ShopingCartItem(product)
            self.items.append(new_item)

    def total_price(self) -> float:
        total = 0
        for item in self.items:
            # intellisense: `item` has `.product`, product has `.price`
            # it will work perfectly fine without Type Hints, but we will need to remember every method and every property
            total += (item.product.price * item.quantity)

        return total
