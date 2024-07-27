from __future__ import annotations

import board_items.task
from board_items.board_item import BoardItem
from user import user


class Board:
    _usernames: [str] = []

    def __init__(self):
        self._items: list[BoardItem] = []
        self._users: list[user.User] = []

    def add_item(self, item: BoardItem):
        if item in self._items:
            raise ValueError('BoardItem already in the list')

        self._items.append(item)

    @property
    def count(self):
        return len(self._items)

    @classmethod
    def username_exists(cls, user_name: str) -> bool:
        return user_name in cls._usernames

    @property
    def team_capacity(self) -> int:
        return sum(u.capacity for u in self._users)

    def add_user(self, username: str, email: str):
        u = user.User(username, email)
        self._users.append(u)
        Board._usernames.append(username)
        return u

    def reassign_task(self, task: board_items.task.Task, new_assignee: user.User):
        for current_assignee in self._users:
            if task in current_assignee.assigned_tasks:
                if current_assignee.username == new_assignee.username:
                    raise ValueError(f"User {new_assignee.username} already has the task.")

                task.revert_status()
                current_assignee.remove_task(task)
                new_assignee.receive_task(task)
                return

        raise ValueError(f"Task {task.title} does not exist.")
