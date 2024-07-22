from board_item import BoardItem
from datetime import date
from item_status import ItemStatus
from event_log import EventLog


class Task(BoardItem):
    def __init__(self, title: str, assignee: str, due_date: date):
        super().__init__(title, due_date, ItemStatus.TODO)
        self.assignee = assignee
        self._event_logs: list[EventLog] = [EventLog(f'Item created: {self.info()}')]

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        self.validate_length(value, 5, 30, "Assignee")
        if hasattr(self, "_assignee"):
            self._event_logs.append(EventLog(f"Assignee changed from {self._assignee} to {value}"))
        self._assignee = value

    def info(self) -> str:
        return f'{self.title}, Assignee: {self.assignee} [{self.status} | {self.due_date}]'