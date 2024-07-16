from datetime import date, timedelta
from item_status import ItemStatus


class BoardItem:
    def __init__(self, title: str, due_date: date):
        if len(title) < 5 or len(title) > 30:
            raise ValueError("Title should be between 5 and 30 characters inclusive.")
        if due_date < date.today():
            raise ValueError("Due date should be in future.")

        self.title = title
        self.due_date = due_date
        self.status = ItemStatus.OPEN

    def revert_status(self) -> None:
        self.status = ItemStatus.previous(self.status)

    def advance_status(self) -> None:
        self.status = ItemStatus.next(self.status)

    def info(self) -> str:
        return f'{self.title}, [{self.status} | {self.due_date}]'

