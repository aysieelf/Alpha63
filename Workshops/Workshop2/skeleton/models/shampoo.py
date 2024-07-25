from models.product import Product
from models.usage_type import UsageType
from commands.validation_helpers import try_parse_int


class Shampoo(Product):
    def __init__(self, name: str, brand: str, price: float, gender: str, usage_type, milliliters):
        if usage_type.isdigit():
            usage_type, milliliters = milliliters, usage_type
        super().__init__(name, brand, price, gender)
        self._usage_type: UsageType = UsageType.from_string(usage_type)
        self.milliliters: int = try_parse_int(milliliters)

    @property
    def usage_type(self) -> UsageType:
        return self._usage_type

    @property
    def milliliters(self) -> int:
        return self._milliliters

    @milliliters.setter
    def milliliters(self, value: int) -> None:
        if value < 0:
            raise ValueError("Milliliters can't be a negative number.")

        self._milliliters = value

    def to_string(self) -> str:
        return '\n'.join([
            f'{super().to_string()}',
            f' #Milliliters: {self.milliliters}',
            f' #Usage: {self.usage_type}'
        ])