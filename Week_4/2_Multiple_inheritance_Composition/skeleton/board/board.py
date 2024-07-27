from __future__ import annotations
import board_items.task
from board_items.board_item import BoardItem
from board_items.item_status import ItemStatus
from user.user import User


class Board:
    def __init__(self):
        self._items: list[BoardItem] = []
        self._users: list[User] = []

    def add_item(self, item: BoardItem):
        if item in self._items:
            raise ValueError(f"Item with title {item.title} already exists.")

        self._items.append(item)

    def remove_item(self, item: BoardItem):
        if item not in self._items:
            raise ValueError(f"Item with title {item.title} doesn't exist.")

        self._items.remove(item)

    @property
    def count(self):
        return len(self._items)

    @property
    def team_capacity(self) -> int:
        return sum(u.capacity for u in self._users)

    def add_user(self, username: str, email: str):
        for user_object in self._users:
            if user_object.username == username:
                raise ValueError(f"Username {username} already exists!")
        u = User(username, email)
        self._users.append(u)
        return u

    def reassign_task(self, task: board_items.task.Task, new_assignee: User):
        for current_assignee in self._users:
            if task in current_assignee.assigned_tasks:
                if current_assignee.username == new_assignee.username:
                    raise ValueError(f"User {new_assignee.username} already has the task.")

                while task.status != ItemStatus.TODO:
                    task.revert_status()

                current_assignee.remove_task(task)
                new_assignee.receive_task(task)
                return

        raise ValueError(f"Task {task.title} does not exist.")
