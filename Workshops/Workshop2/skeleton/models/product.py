from models.gender import Gender
from commands.validation_helpers import try_parse_float


class Product:
    def __init__(self, name: str, brand: str, price: float | str, gender: str):
        self.name = name
        self.brand = brand
        self.price = try_parse_float(price)
        self._gender = Gender.from_string(gender)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) < 3 or len(value) > 10:
            raise ValueError('Name should be between 3 and 10 symbols.')

        self._name = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        if len(value) < 2 or len(value) > 10:
            raise ValueError('Brand should be between 2 and 10 symbols.')

        self._brand = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: str | float) -> None:
        if value < 0:
            raise ValueError('Price should not be negative.')

        self._price = value

    @property
    def gender(self) -> str:
        return self._gender

    def to_string(self) -> str:
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
        ])
