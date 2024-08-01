from models.car import Car
from models.comment import Comment
from models.constants.user_role import UserRole
from models.validation_helpers import valid_str_len
from models.vehicle import Vehicle
import re


class User:
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self,
                 username: str,
                 first_name: str,
                 last_name: str,
                 password: str,
                 user_role: str = UserRole.NORMAL):

        self.username = username
        self.firstname = first_name
        self.lastname = last_name
        self.password = password
        self.user_role = user_role
        self._vehicles: list[Vehicle] = []

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        if not value.isalnum():
            raise ValueError(User.USERNAME_INVALID_SYMBOLS)

        valid_str_len(value,
                      User.USERNAME_LEN_MIN,
                      User.USERNAME_LEN_MAX,
                      User.USERNAME_LEN_ERR)

        self._username = value

    @property
    def firstname(self) -> str:
        return self._first_name

    @firstname.setter
    def firstname(self, value: str) -> None:
        valid_str_len(value,
                      User.FIRSTNAME_LEN_MIN,
                      User.FIRSTNAME_LEN_MAX,
                      User.FIRSTNAME_LEN_ERR)

        self._first_name = value

    @property
    def lastname(self) -> str:
        return self._last_name

    @lastname.setter
    def lastname(self, value: str) -> None:
        valid_str_len(value,
                      User.LASTNAME_LEN_MIN,
                      User.LASTNAME_LEN_MAX,
                      User.LASTNAME_LEN_ERR)

        self._last_name = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        pattern = r'^[a-zA-Z0-9@*\-_]+$'
        if not re.match(pattern, value):
            raise ValueError(User.PASSWORD_INVALID_SYMBOLS)

        valid_str_len(value,
                      User.PASSWORD_LEN_MIN,
                      User.PASSWORD_LEN_MAX,
                      User.PASSWORD_LEN_ERR)

        self._password = value

    @property
    def user_role(self) -> str:
        return self._user_role

    @user_role.setter
    def user_role(self, value: str) -> None:
        self._user_role = UserRole.from_string(value)

    @property
    def is_admin(self) -> bool:
        return self.user_role == UserRole.ADMIN

    @property
    def vehicles(self) -> tuple:
        return tuple(self._vehicles)

    def get_vehicle(self, index: int) -> Vehicle:
        if index >= len(self.vehicles):
            raise ValueError(User.THE_VEHICLE_DOES_NOT_EXIT)

        return self.vehicles[index]

    def add_vehicle(self, vehicle: Vehicle) -> None:
        if self.user_role == UserRole.ADMIN:
            raise ValueError(User.ADMIN_CANNOT_ADD_VEHICLES_ERR)

        if (self.user_role == UserRole.NORMAL and
                len(self._vehicles) == User.NORMAL_ROLE_VEHICLE_LIMIT):
            raise ValueError(User.NORMAL_USER_LIMIT_REACHED_ERR)

        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle not in self._vehicles:
            return

        self._vehicles.remove(vehicle)

    def add_comment(self, comment: str, vehicle: Vehicle) -> None:
        vehicle.add_comment(Comment(comment, self.username))

    def remove_comment(self, comment: Comment, vehicle: Vehicle) -> None:
        if comment.author != self.username:
            raise ValueError(User.YOU_ARE_NOT_THE_AUTHOR)
        vehicle.remove_comment(comment)

    def print_vehicles(self) -> str:
        vehicles = '--NO VEHICLES--'
        if self._vehicles:
            vehicles = '\n'.join(f"{i + 1}. {str(vehicle)}"
                                 for i, vehicle in enumerate(self._vehicles))
        return (f'--USER {self.username}--\n'
                f'{vehicles}')

    def __str__(self) -> str:
        return (f"Username: {self.username}, "
                f"FullName: {self.firstname} {self.lastname}, "
                f"Role: {self.user_role}")