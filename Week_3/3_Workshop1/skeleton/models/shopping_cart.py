from models.product import Product


class ShoppingCart:
    def __init__(self):
        self._products: list[Product] = []

    @property
    def products(self) -> tuple:
        return tuple(self._products)

    def add_product(self, product: Product) -> None:
        if not product:
            raise ValueError("No product.")
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        if not product:
            raise ValueError("No product.")
        if product in self._products:
            self._products.remove(product)

    def contains_product(self, product: Product) -> bool:
        return product in self._products

    def total_price(self) -> float:
        return sum(p.price for p in self.products)
