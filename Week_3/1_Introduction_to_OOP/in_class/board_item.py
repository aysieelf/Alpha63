from datetime import date, timedelta
from item_status import ItemStatus
from event_log import *


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


class BoardItem:
    def __init__(self, title: str, due_date: date):
        if 5 <= len(title) <= 30:
            self._title = title
        self._due_date = due_date
        self._status = ItemStatus.OPEN
        self.events = []
        self.events.append(EventLog(f"Item created: {BoardItem.info(self)}"))

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if value < date.today():
            raise ValueError("Date cannot be in the past")
        else:
            memo_date = self._due_date
            self._due_date = value
            # self._due_date += timedelta(value)
            self.events.append(EventLog(f"DueDate changed from {memo_date} to {self._due_date}"))

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if 5 <= len(title) <= 30:
            memo_title = self._title
            self._title = title
            self.events.append(EventLog(f"Title changed from {memo_title} to {title}"))
        else:
            raise ValueError("Illegal title length [5:30]")

    @property
    def status(self):
        return self._status

    def revert_status(self):
        memo_stat = self._status
        if self._status == ItemStatus.OPEN:
            self.events.append(EventLog(f"Cant change status, already at {self._status}"))

        else:
            self._status = ItemStatus.previous(self._status)
            self.events.append(EventLog(f"Status changed form {memo_stat} to {self._status}"))

    def advance_status(self):
        memo_stat = self._status
        if self._status == ItemStatus.VERIFIED:
            self.events.append(EventLog(f"Cant change status, already at {self._status}"))

        else:
            self._status = ItemStatus.next(self._status)
            self.events.append(EventLog(f"Status changed form {memo_stat} to {self._status}"))

    def info(self):
        return f"{self.title}, [{self._status} | {self.due_date}]"

    def history(self) -> str:
        msg = ''
        for i in self.events:
            msg += f"{i}\n"
        return msg
