from datetime import datetime


class EventLog:
    def __init__(self, description: str):
        self._description = self.valid_description(description)
        self._timestamp: datetime = datetime.now()

    @property
    def description(self):
        return self._description

    @property
    def timestamp(self):
        return self._timestamp

    def info(self) -> str:
        return f"[{self._timestamp.strftime("%m/%d/%Y, %H:%M:%S")}] {self._description}"

    @staticmethod
    def valid_description(value: str):
        if not value:
            raise ValueError("Description can't be empty.")
        return value
