from datetime import date
from board_item import BoardItem


class Issue(BoardItem):
    def __init__(self, title: str, description: str, due_date: date):
        
        self._description = description
        
        super().__init__(title, due_date)
        self._log_event(f'Issue created: {super().info()}')

    @property
    def description(self):
        return self._description

    def valid_description(self, value: str)-> str:
        if value == '':
            return "No description"
        return value

    def info(self) -> str:
        return f"Issue ({self.description}) {super().info()}"

