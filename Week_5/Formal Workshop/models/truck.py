from models.validation_helpers import valid_num_range
from models.vehicle import Vehicle


class Truck(Vehicle):
    WEIGHT_CAP_MIN = 1
    WEIGHT_CAP_MAX = 100
    WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'

    WHEELS_COUNT = 8

    def __init__(self,
                 make: str,
                 model: str,
                 price: float,
                 weight_capacity: int):

        super().__init__(make, model, price)
        self.weight_capacity = weight_capacity

    @property
    def weight_capacity(self) -> int:
        return self._weight_capacity

    @weight_capacity.setter
    def weight_capacity(self, value: int) -> None:
        valid_num_range(value,
                        Truck.WEIGHT_CAP_MIN,
                        Truck.WEIGHT_CAP_MAX,
                        Truck.WEIGHT_CAP_ERR)

        self._weight_capacity = value

    def __str__(self) -> str:
        return (f'{super().__str__()}\n'
                f'Weight Capacity: {self.weight_capacity}t\n'
                f'{self.comments_str()}')
