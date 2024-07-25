from models.product import Product
from models.scent import Scent


class Cream(Product):
    def __init__(self, name: str, brand: str, price: float, gender: str, scent: str):
        super().__init__(name, brand, price, gender)
        self._scent = Scent.from_string(scent)

    @Product.name.setter
    def name(self, value: str) -> None:
        if len(value) < 3 or len(value) > 15:
            raise ValueError('Name should be between 3 and 15 symbols.')

        Product._name = value

    @Product.brand.setter
    def brand(self, value: str) -> None:
        if len(value) < 3 or len(value) > 15:
            raise ValueError('Brand should be between 3 and 15 symbols.')

        Product._brand = value

    @property
    def scent(self) -> str:
        return self._scent

    def to_string(self) -> str:
        return '\n'.join([
            f'{super().to_string()}',
            f' #Scent: {self.scent}'
        ])
