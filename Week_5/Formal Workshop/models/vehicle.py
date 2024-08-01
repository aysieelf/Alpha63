from models.comment import Comment
from models.validation_helpers import valid_str_len, valid_num_range


class Vehicle:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    WHEELS_COUNT = 0

    def __init__(self,
                 make: str,
                 model: str,
                 price: float):

        self.make = make
        self.model = model
        self._wheels: int = self.__class__.WHEELS_COUNT
        self.price = price
        self._comments: list[Comment] = []

    @property
    def make(self) -> str:
        return self._make

    @make.setter
    def make(self, value: str) -> None:
        valid_str_len(value,
                      self.__class__.MAKE_LEN_MIN,
                      self.__class__.MAKE_LEN_MAX,
                      self.__class__.MAKE_LEN_ERR)

        self._make = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        valid_str_len(value,
                      self.__class__.MODEL_LEN_MIN,
                      self.__class__.MODEL_LEN_MAX,
                      self.__class__.MODEL_LEN_ERR)

        self._model = value

    @property
    def wheels(self) -> int:
        return self._wheels

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        valid_num_range(value,
                        self.__class__.PRICE_MIN,
                        self.__class__.PRICE_MAX,
                        self.__class__.PRICE_ERR)

        self._price = value

    @property
    def comments(self) -> tuple:
        return tuple(self._comments)

    def add_comment(self, comment: Comment) -> None:
        self._comments.append(comment)

    def get_comment(self, index: int) -> Comment:
        if index >= len(self._comments):
            raise ValueError("There is no comment on this index.")

        return self._comments[index]

    def remove_comment(self, comment: Comment) -> None:

        if comment not in self._comments:
            return

        self._comments.remove(comment)

    def comments_str(self):
        comments = "--NO COMMENTS--"
        if self._comments:
            comments = (f"--COMMENTS--\n"
                        f"{"\n".join(str(comment) for comment in self._comments)}\n"
                        f"--COMMENTS--")

        return comments

    def __str__(self):
        return (f'{self.__class__.__name__}:\n'
                f'Make: {self.make}\n'
                f'Model: {self.model}\n'
                f'Wheels: {self.__class__.WHEELS_COUNT}\n'
                f'Price: ${self.price:.2f}')
