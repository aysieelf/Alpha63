from models.product import Product
from commands.validation_helpers import valid_str_len


class Category:
    NAME_LEN_MIN_NUM = 3
    NAME_LEN_MAX_NUM = 10
    NAME_LEN_ERR = 'Category name should be between 3 and 10 symbols.'

    def __init__(self,
                 name: str) -> None:

        self._name = valid_str_len(name,
                                   Category.NAME_LEN_MIN_NUM,
                                   Category.NAME_LEN_MAX_NUM,
                                   Category.NAME_LEN_ERR)

        self._products: list[Product] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def products(self) -> tuple:
        return tuple(self._products)

    def add_product(self, product: Product) -> None:
        if product in self._products:
            raise ValueError(f'Product {product.name} already exists!')

        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        if product not in self._products:
            raise ValueError(f'Product {product.name} does not exists!')

        self._products.remove(product)

    def to_string(self):
        new_line = '\n'
        if len(self._products) > 0:
            product_strings = [p.to_string() for p in self._products]
            return f'#Category: {self.name}{new_line}{new_line.join(product_strings)}'
        else:
            return f'#Category: {self.name}{new_line} #No products in this category'
