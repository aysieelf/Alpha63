from datetime import date, timedelta
from board_item import BoardItem
from item_status import ItemStatus
from board import Board
from event_log import EventLog
from task import Task


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


task = Task('Test the application flow', 'Steven', add_days_to_now(2))
print(task.title)      # Test the application flow
print(task.due_date)   # 2022-03-18
print(task.status)
print(task.assignee)