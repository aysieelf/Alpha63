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

        self.name = valid_str_len(name,
                                  Product.NAME_LEN_MIN_NUM,
                                  Product.NAME_LEN_MAX_NUM,
                                  Product.NAME_LEN_ERR)
        # Todo: validate name, brand, price
        self.brand = valid_str_len(brand, 
                                   Product.BRAND_LEN_MIN_NUM,
                                   Product.BRAND_LEN_MAX_NUM,
                                   Product.BRAND_LEN_ERR)
        self._gender = gender
        self.valid_price(price)

    @property
    def price(self):
        return self._price
    
    def valid_price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price can't be negative")

    @property
    def gender(self):
        return self._gender

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender.value}',
            ' ==='
        ])
