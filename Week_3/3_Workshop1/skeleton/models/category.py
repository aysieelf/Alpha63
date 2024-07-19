from models.product import Product

class Category:
    def __init__(self, name: str):
        self.name = name
        self._products: list[Product] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) < 2 or len(value) > 15:
            raise ValueError("Name’s length must be between 3 and 15 symbols.")
        self._name = value

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product: Product) -> None:
        if product in self._products:
            raise ValueError(f"{product.name} already in category.")
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        if product not in self._products:
            raise ValueError(f"Product is not found in {self._name} category.")
        self._products.remove(product)

    def to_string(self) -> str:
        if not self._products:
            return (f"#Category: {self._name}\n"
                    f" #No products in this category")
        products_str = '\n ===\n'.join(product.to_string() for product in self._products)
        return (f"#Category: {self._name}\n"
                f"{products_str}")
