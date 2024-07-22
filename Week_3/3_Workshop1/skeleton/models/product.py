from models.gender import Gender
from commands.validation_helpers import try_parse_float


class Product:

    def __init__(self, name: str, brand: str, price: float, gender: str):
        self.name = name
        self.brand = brand
        self.price = price
        self._gender = Gender.from_string(gender)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) < 3 or len(value) > 10:
            raise ValueError("Name’s length must be between 3 and 10 symbols.")
        self._name = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        if len(value) < 2 or len(value) > 10:
            raise ValueError("Brand’s length must be between 2 and 10 symbols.")
        self._brand = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        num = try_parse_float(value)
        if num < 0:
            raise ValueError("Price should be a positive number.")
        self._price = value

    @property
    def gender(self) -> str:
        return self._gender

    def to_string(self) -> str:
        return (f" #{self.name} {self.brand}\n"
                f" #Price: ${self.price:.2f}\n"
                f" #Gender: {self._gender}")

    def __eq__(self, other) -> bool:
        if isinstance(other, Product):
            return self.name == other.name
        return False


