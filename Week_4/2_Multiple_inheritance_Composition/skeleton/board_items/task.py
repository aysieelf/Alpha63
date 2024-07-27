from __future__ import annotations
from user import user
from board_items.board_item import BoardItem
from datetime import date
from board_items.item_status import ItemStatus


class Task(BoardItem):
    def __init__(self, title: str, assignee: user.User, due_date: date):
        self.assignee = assignee
        super().__init__(title, due_date, ItemStatus.TODO)

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value: user.User):
        if hasattr(self, "_assignee"):
            self._log_event(f'Assignee changed from {self._assignee} to {value}')

        self._assignee = value

    def info(self):
        return f'Task (assigned to: {self.assignee}) {super().info()}'
