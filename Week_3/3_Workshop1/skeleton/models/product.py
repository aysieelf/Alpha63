class Product:
    gender_types = ("Men", "Women", "Unisex")

    def __init__(self, name: str, brand: str, price: float, gender: str):
        self.name = name
        self.brand = brand
        self.price = price
        self._gender = self._valid_gender(gender)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) < 3 or len(value) > 10:
            raise ValueError("Name’s length must be between 3 and 10 symbols.")
        self._name = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if len(value) < 2 or len(value) > 10:
            raise ValueError("Name’s length must be between 2 and 10 symbols.")
        self._brand = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price should be a positive number.")
        self._price = value

    @property
    def gender(self):
        return self._gender

    def _valid_gender(self, value: str):
        if value not in Product.gender_types:
            raise ValueError("Valid gender types: Men, Women, Unisex")
        return value

    def to_string(self) -> str:
        return (f" #{self.name} {self.brand}\n"
                f" #Price: ${self.price:.2f}\n"
                f" #Gender: {self._gender}")

    def __eq__(self, other) -> bool:
        if isinstance(other, Product):
            return self.name == other.name
        return False


