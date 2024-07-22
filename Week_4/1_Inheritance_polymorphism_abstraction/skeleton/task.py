from board_item import BoardItem
from datetime import date
from item_status import ItemStatus
from event_log import EventLog


class Task(BoardItem):
    def __init__(self, title: str, assignee: str, due_date: date):
        self.assignee = assignee
        super().__init__(title, due_date, ItemStatus.TODO)

    @property
    def assignee(self):
        return self._assignee
    
    @assignee.setter
    def assignee(self, value: str) -> None:
        self._ensure_valid_string(value, 5, 30, "Assignee")
        if hasattr(self, "_assignee"):
            self._log_event(f"Assignee changed from {self._assignee} to {value}")
        self._assignee = value

    def _log_event(self, description: str):
        self._history.append(EventLog(description))

    def info(self) -> str:
        return f"Task (assigned to: {self.assignee}) {super().info()}"