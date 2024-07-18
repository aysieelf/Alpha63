class Room:
    types = "Single", "Double", "Suite"
    def __init__(self, room_num: int, room_type: str, price: float):
        self.room_num = room_num
        self.room_type = room_type
        self.room_price = price
        self.is_booked = False

    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        if not isinstance(value, int):
            raise TypeError("Room number must be an integer number.")
        self._room_num = value

    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        if value not in Room.types:
            raise ValueError("Types are Single, Double, Suite.")
        self._room_type = value

    @property
    def room_price(self):
        return self._room_price

    @room_price.setter
    def room_price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float number.")
        if value < 0:
            raise ValueError("Price must be a positive number.")
        self._room_price = value

    def book_room(self):
        self.is_booked = True

    def release_room(self):
        self.is_booked = False

    def __str__(self):
        is_available = "available"
        if self.is_booked:
            is_available = "not available"
        return (f"Room num. {self.room_price}:\nType: {self.room_type}\n"
                f"Price: {self.room_price}\n The room is {is_available}.")



