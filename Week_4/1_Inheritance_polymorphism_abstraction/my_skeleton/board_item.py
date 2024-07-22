from datetime import date
from item_status import ItemStatus
from event_log import EventLog


class BoardItem:
    def __init__(self, title: str, due_date: date):
        self.title = title
        self.due_date = due_date
        self._status: ItemStatus = ItemStatus.OPEN
        self._event_logs: list[EventLog] = [EventLog(f'Item created: {self.info()}')]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not value:
            raise ValueError("Title can't be empty.")
        if len(value) < 5 or len(value) > 30:
            raise ValueError("Title should be between 5 and 30 characters inclusive.")
        if hasattr(self, "_title"):
            self._event_logs.append(EventLog(f"Title changed from {self.title} to {value}"))
        self._title = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value: date):
        if value < date.today():
            raise ValueError("Due date can't be in the past.")
        if hasattr(self, "_date"):
            self._event_logs.append(EventLog(f"DueDate changed from {self.due_date} to {value}"))
        self._due_date = value

    @property
    def status(self):
        return self._status

    @property
    def event_logs(self):
        return self._event_logs

    def revert_status(self) -> None:
        previous = self._status
        new = ItemStatus.previous(self.status)
        if previous == new:
            self._event_logs.append(EventLog(f"Cant change status, already at {previous}"))
        else:
            self._status = new
            self._event_logs.append(EventLog(f"Status changed from {previous} to {new}"))

    def advance_status(self) -> None:
        previous = self._status
        new = ItemStatus.next(self.status)
        if previous == new:
            self._event_logs.append(EventLog(f"Can't change status, already at {previous}"))
        else:
            self._status = new
            self._event_logs.append(EventLog(f"Status changed from {previous} to {new}"))

    def info(self) -> str:
        return f'{self.title}, [{self.status} | {self.due_date}]'

    def history(self) -> str:
        result = ''
        for event in self.event_logs:
            result += f'{event.info()}\n'
        return result



