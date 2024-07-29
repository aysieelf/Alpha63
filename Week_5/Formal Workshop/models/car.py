from models.comment import Comment
from models.validation_helpers import valid_num_range
from models.vehicle import Vehicle


class Car(Vehicle):
    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    WHEELS_COUNT = 4

    def __init__(self,
                 make: str,
                 model: str,
                 price: float,
                 seats: int):

        super().__init__(make, model, price)
        self.seats = seats

    @property
    def seats(self) -> int:
        return self._seats

    @seats.setter
    def seats(self, value: int) -> None:
        valid_num_range(value,
                        Car.CAR_SEATS_MIN,
                        Car.CAR_SEATS_MAX,
                        Car.CAR_SEATS_ERR)

        self._seats = value

    def __str__(self) -> str:
        return (f'{super().__str__()}\n'
                f'Seats: {self.seats}\n'
                f'{self.comments_str()}')