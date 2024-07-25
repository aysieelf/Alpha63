from models.category import Category
from models.product import Product
from models.shampoo import Shampoo
from models.shopping_cart import ShoppingCart
from models.toothpaste import Toothpaste
from models.cream import Cream


class ApplicationData:
    def __init__(self):
        self._products: list[Product] = []
        self._categories: list[Category] = []
        self._shopping_cart: ShoppingCart = ShoppingCart()

    @property
    def products(self) -> tuple:
        return tuple(self._products)

    @property
    def categories(self) -> tuple:
        return tuple(self._categories)

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shopping_cart

    def find_product_by_name(self, name: str) -> Product:
        for product in self._products:
            if product.name == name:
                return product

        raise ValueError(f'Product {name} does not exist!')

    def find_category_by_name(self, name: str) -> Category:
        for category in self._categories:
            if category.name == name:
                return category

        raise ValueError(f'Category {name} does not exist!')

    def create_category(self, name: str) -> None:
        if self.category_exists(name):
            raise ValueError(f'Category {name} already exists!')

        category = Category(name)
        self._categories.append(category)

    def create_shampoo(self, name: str, brand: str, price: str | float, gender: str, usage_type, milliliters) -> Shampoo:
        if self.product_exists(name):
            raise ValueError(f'Shampoo {name} already exists!')

        shampoo = Shampoo(name, brand, price, gender, usage_type, milliliters)
        self._products.append(shampoo)

        return shampoo

    def create_toothpaste(self, name: str, brand: str, price: str | float, gender: str, ingredients: str | list[str]) \
            -> Toothpaste:
        if self.product_exists(name):
            raise ValueError(f'Toothpaste {name} already exists!')

        toothpaste = Toothpaste(name, brand, price, gender, ingredients)
        self._products.append(toothpaste)

        return toothpaste

    def create_cream(self, name: str, brand: str, price: str | float, gender: str, scent: str) -> Cream:
        if self.product_exists(name):
            raise ValueError(f'Cream {name} already exists!')

        cream = Cream(name, brand, price, gender, scent)
        self._products.append(cream)

        return cream

    def category_exists(self, name: str) -> bool:
        return name in [c.name for c in self._categories]

    def product_exists(self, name: str) -> bool:
        return name in [p.name for p in self._products]
