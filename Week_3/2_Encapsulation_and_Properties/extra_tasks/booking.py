from room import Room
from datetime import datetime

class Booking:
    def __init__(self, room: Room, guest_name: str, check_in_date: datetime, check_out_date: datetime):
        self.room = room
        self._guest_name = self._valid_name(guest_name)
        self._check_in_date = self._valid_check_in_date(check_in_date)
        self._check_out_date = self._valid_check_out_date(check_out_date)

    @property
    def guest_name(self):
        return self._guest_name

    def _valid_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Names must be string objects.")
        return value.capitalize()

    @property
    def check_in_date(self):
        return self._check_in_date

    def _valid_check_in_date(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Check-in date must be a datetime object.")
        return value

    @property
    def check_out_date(self):
        return self._check_out_date

    def _valid_check_out_date(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Check-out date must be a datetime object.")
        if value < self.check_in_date:
            raise ValueError("Check-out date must be after the check-in date")
        return value


    def __str__(self):
        return (f"Guest name: {self.guest_name}\nRoom:\n{self.room}\n"
                f"Check in: {self.check_in_date}\nCheck out: {self.check_out_date}")