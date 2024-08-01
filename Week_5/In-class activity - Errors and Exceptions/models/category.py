from models.product import Product


class Category:
    def __init__(self, name: str):
        # Todo: Apply name validation
        self._products: list[Product] = []


    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product: Product):
        # Todo: Validate that this product not already added before adding it
        raise NotImplementedError

    def remove_product(self, product: Product):
        # Todo: Validate that this product exists and if yes - then remove it
        raise NotImplementedError

    def to_string(self):
        new_line = '\n'
        if len(self._products) > 0:
            product_strings = [p.to_string() for p in self._products]
            return f'#Category: {self.name}{new_line}{new_line.join(product_strings)}'
        else:
            return f'#Category: {self.name}{new_line} #No products in this category'
