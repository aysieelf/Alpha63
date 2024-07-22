from datetime import date
from item_status import ItemStatus
from event_log import EventLog


class BoardItem:
    def __init__(self, title: str, due_date: date, status=ItemStatus.OPEN):
        self.title = title
        self.due_date = due_date
        self._status = status
        self._history = []
        self._log_event(f'Item created: {self.info()}')

    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        self._ensure_valid_string(value, 5, 30, "Title")
        if hasattr(self, "_title"):
            self._log_event(f"Title changed from {self.title} to {value}")
        self._title = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._ensure_valid_due_date(value)
        if hasattr(self, "_date"):
            self._log_event(f"DueDate changed from {self.due_date} to {value}")
        self._due_date = value

    def revert_status(self):
        prev = self._status
        self._status = ItemStatus.previous(self._status)
        self._log_status_change(prev, self._status)

    def advance_status(self):
        prev = self._status
        self._status = ItemStatus.next(self._status)
        self._log_status_change(prev, self._status)

    def info(self):
        return f'{self._title}, [{self._status} | {self._due_date}]'

    def history(self):
        return '\n'.join((log.info() for log in self._history))

    def _log_event(self, description: str):
        self._history.append(EventLog(description))

    def _log_status_change(self, prev: str, current: str):
        if prev == current:
            self._log_event(f'Cant change status, already at {current}')
        else:
            self._log_event(f'Status changed from {prev} to {current}')

    def _ensure_valid_string(self, value, min_num, max_num, param_name):
        if not value:
            raise ValueError(f"{param_name} can't be empty.")
        if len(value) < min_num or len(value) > max_num:
            raise ValueError(f"{param_name}'s length should be [{min_num}:{max_num}]")

    def _ensure_valid_due_date(self, due_date):
        if due_date < date.today():
            raise ValueError('Due date cant be in the past.')
