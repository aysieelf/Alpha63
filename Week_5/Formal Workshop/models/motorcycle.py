from models.validation_helpers import valid_str_len
from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WHEELS_COUNT = 2

    def __init__(self,
                 make: str,
                 model: str,
                 price: float,
                 category: str):

        super().__init__(make, model, price)
        self.category = category

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str) -> None:
        valid_str_len(value,
                      Motorcycle.CATEGORY_LEN_MIN,
                      Motorcycle.CATEGORY_LEN_MAX,
                      Motorcycle.CATEGORY_LEN_ERR)

        self._category = value

    def __str__(self) -> str:
        return (f'{super().__str__()}\n'
                f'Category: {self.category}\n'
                f'{self.comments_str()}')
