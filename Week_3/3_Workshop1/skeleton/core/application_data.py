from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


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

    def create_product(self, name: str, brand: str, price: float, gender: str) -> None:
        if self.product_exists(name):
            raise ValueError(f"Product {name} already exists.")
        self._products.append(Product(name, brand, price, gender))

    def find_product_by_name(self, name: str) -> Product:
        for product in self._products:
            if name == product.name:
                return product
        raise ValueError(f"Product {name} not found.")

    def product_exists(self, name: str) -> bool:
        return name in [pro.name for pro in self.products]

    def create_category(self, name: str) -> None:
        if self.category_exists(name):
            raise ValueError(f"Category {name} already exists.")
        self._categories.append(Category(name))

    def find_category_by_name(self, name: str) -> Category:
        for category in self._categories:
            if name == category.name:
                return category
        raise ValueError(f"Category {name} not found.")

    def category_exists(self, name) -> bool:
        return name in [cat.name for cat in self.categories]

