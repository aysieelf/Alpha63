from models.gender import Gender


class Product:
    def __init__(self, name: str, brand: str, price: float, gender: Gender):
        # Todo: validate name, brand, price
        self._gender = gender

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
