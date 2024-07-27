from __future__ import annotations
from board_items.task import Task  # importing class
from board_items.item_status import ItemStatus


class User:
    CAPACITY = 3

    def __init__(self, username: str, email: str):
        self._username = self.valid_username(username)
        self.email = email
        self._assigned_tasks: list[Task] = []

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def assigned_tasks(self) -> tuple:
        return tuple(self._assigned_tasks)

    @property
    def capacity(self) -> int:
        capacity = User.CAPACITY
        for task in self._assigned_tasks:
            if (task.status == ItemStatus.TODO or
                    task.status == ItemStatus.IN_PROGRESS):
                capacity -= 1

        return capacity

    def valid_username(self, value: str) -> str:
        if value == '':
            raise ValueError("Username should not be an empty string")

        return value

    def advance_task_status(self, task: Task) -> None:  # removed type annotation Task
        if not self._task_exists(task):
            raise ValueError(f"Task {task.title} is not assigned to {self.username}!")
        task.advance_status()

    def receive_task(self, task: Task):
        if self.capacity <= 0:
            raise ValueError(f"User {self.username} can't receive any more tasks!")
        if self._task_exists(task):
            raise ValueError(f"Task {task.title} already assigned to {self.username}!")
        task.assignee = self
        self._assigned_tasks.append(task)

    def remove_task(self, task: Task):  # removed type annotation Task
        if not self._task_exists(task):
            raise ValueError(f"Task {task.title} is not assigned to {self.username}!")
        self._assigned_tasks.remove(task)

    def _task_exists(self, task: Task):  # removed type annotation Task
        return any(t.title == task.title for t in self.assigned_tasks)

    def __str__(self):
        return self.username
