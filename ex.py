class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items: list[Product] = []

    def add_product(self, product: Product):
        pass
