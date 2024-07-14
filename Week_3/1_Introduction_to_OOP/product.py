class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def advertise(self):
        msg = f'Lovely {self.name} for only {self.price}!'
        return msg

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)

