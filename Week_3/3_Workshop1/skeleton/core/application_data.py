from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


class ApplicationData:
    def __init__(self):
        self._products = []
        self._categories = []
        self._shopping_cart: ShoppingCart = ShoppingCart()

    @property
    def products(self):
        return tuple(self._products)

    @property
    def categories(self):
        return tuple(self._categories)

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shopping_cart

    def create_product(self, name, brand, price, gender) -> None:
        if self.product_exists(name):
            raise ValueError("Product with the same name already exists.")
        self._products.append(Product(name, brand, price, gender))

    def find_product_by_name(self, name: str) -> Product:
        for product in self._products:
            if name == product.name:
                return product
        raise ValueError("Product not found.")

    def product_exists(self, name) -> bool:
        for product in self._products:
            if name == product.name:
                return True
        return False

    def create_category(self, name: str) -> None:
        if self.category_exists(name):
            raise ValueError("Category with the same name already exists.")
        self._categories.append(Category(name))

    def find_category_by_name(self, name) -> Category:
        for category in self._categories:
            if name == category.name:
                return category
        raise ValueError("Category not found.")

    def category_exists(self, name) -> bool:
        for category in self._categories:
            if name == category.name:
                return True
        return False

