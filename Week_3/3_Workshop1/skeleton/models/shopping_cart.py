from models.product import Product

class ShoppingCart:
    def __init__(self):
        self._products: list[Product] = []

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product: Product):
        if not product:
            raise ValueError("No product.")
        self._products.append(product)

    def remove_product(self, product: Product):
        if not product:
            raise ValueError("No product.")
        if product in self._products:
            self._products.remove(product)

    def contains_product(self, product: Product) -> bool:
        if product in self._products:
            return True
        return False

    def total_price(self) -> float:
        price = 0
        for product in self._products:
            price += product.price
        return price
