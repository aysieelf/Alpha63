from models.gender import Gender
from commands.validation_helpers import valid_str_len


class Product:
    NAME_LEN_MIN_NUM = 3
    NAME_LEN_MAX_NUM = 10
    NAME_LEN_ERR = 'Product name should be between 3 and 10 symbols.'

    BRAND_LEN_MIN_NUM = 2
    BRAND_LEN_MAX_NUM = 10
    BRAND_LEN_ERR = 'Product brand should be between 2 and 10 symbols.'

    def __init__(self,
                 name: str,
                 brand: str,
                 price: float,
                 gender: Gender) -> None:

        self._name = valid_str_len(name,
                                   Product.NAME_LEN_MIN_NUM,
                                   Product.NAME_LEN_MAX_NUM,
                                   Product.NAME_LEN_ERR)
        self._brand = valid_str_len(brand,
                                    Product.BRAND_LEN_MIN_NUM,
                                    Product.BRAND_LEN_MAX_NUM,
                                    Product.BRAND_LEN_ERR)
        self._gender = gender
        self._price = self.valid_price(price)

    @property
    def name(self) -> str:
        return self._name

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def price(self) -> float:
        return self._price

    @staticmethod
    def valid_price(value: float) -> float:
        if value < 0:
            raise ValueError("Price can't be negative")
        return value

    @property
    def gender(self) -> Gender:
        return self._gender

    def to_string(self) -> str:
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender.value}',
            ' ==='])
