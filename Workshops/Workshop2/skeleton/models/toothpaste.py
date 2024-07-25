from models.product import Product


class Toothpaste(Product):
    def __init__(self, name: str, brand: str, price: float | str, gender: str, ingredients: list[str] | str):
        super().__init__(name, brand, price, gender)
        self._ingredients: list[str] = self._validate_ingredients(ingredients)

    @property
    def ingredients(self) -> tuple:
        return tuple(self._ingredients)

    def _validate_ingredients(self, value: list[str] | str) -> list[str]:
        if isinstance(value, str):
            value = value.split(',')

        return value

    def to_string(self) -> str:
        return '\n'.join([
            f'{super().to_string()}',
            f' #Ingredients: {f"[{', '.join(ingr for ingr in self._ingredients)}]"}'
        ])
