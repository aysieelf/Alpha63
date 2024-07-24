from board_items.board_item import BoardItem
from datetime import date


class Issue(BoardItem):
    def __init__(self, title: str, description: str, due_date: date):
        self._description = self.valid_description(description)
        super().__init__(title, due_date)

    @property
    def description(self):
        return self._description

    def valid_description(self, value: str) -> str:
        return "No description" if value == '' else value

    def info(self) -> str:
        return f"Issue ({self.description}) {super().info()}"
