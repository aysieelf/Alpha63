from eventlog import EventLog
from room import Room
from booking import Booking
class Hotel:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self._rooms = []
        self._event_log = EventLog()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self.validate_name(value):
            self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if self.validate_capacity(value):
            self._capacity = value

    @property
    def rooms(self):
        return tuple(self._rooms)

    @property
    def event_log(self):
        return self._event_log

    def validate_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string object.")
        return True

    def validate_capacity(self, value):
        if not isinstance(value, int):
            raise TypeError("Capacity must be an integer number.")
        return True

    def add_room(self, room: Room):
        if self.capacity > 0:
            self._rooms.append(room)
            self.capacity -= 1

    def book_room(self, room_number, guest_name, check_in_date, check_out_date):
        for room in self._rooms:
            if room._room_num == room_number:
                if not room.is_booked:
                    room.book_room()
                    Booking(room, guest_name, check_in_date, check_out_date)
                    self._event_log.add_event(f"{room.room_num} is booked by {guest_name} "
                                       f"from {check_out_date} until {check_in_date}")

    def release_room(self, room_number):
        for room in self._rooms:
            if room.room_num == room_number:
                if room.is_booked:
                    room.release_room()
                    self.event_log.add_event(f"{room.room_num} is now available.")

    def list_rooms(self):
        all_info = ''
        for room in self._rooms:
            all_info += f"{room}" + '\n-------------------------\n'
        print(f"{all_info}")

    def list_available_rooms(self):
        all_info = ''
        for room in self._rooms:
            if not room.is_booked:
                all_info += f"{room}" + '\n-------------------------\n'
        print(f"{all_info}")

    def get_event_log(self):
        return self._event_log._event_log_list
