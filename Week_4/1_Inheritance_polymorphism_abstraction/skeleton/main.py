from datetime import date, timedelta
from board import Board
from board_item import BoardItem
from event_log import EventLog
from issue import Issue
from task import Task


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


# all examples:

# item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
# print(item.title)
# print(item.due_date)
# print(item.status)

# =====================

# item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
# print(item.status) # Open
# item.advance_status()
# print(item.status)
# item.advance_status()
# print(item.status) # In progress
# item.revert_status()
# print(item.status)

# =====================

# item = BoardItem('Refactor this mess', add_days_to_now(2))
# item.due_date += timedelta(days=365 * 2)  # two years in the future
# item.title = 'Not that important'
# item.revert_status()
# item.advance_status()
# item.revert_status()
# print(item.history())
#
# print('\n--------------\n')
#
# anotherItem = BoardItem('Dont refactor anything',  add_days_to_now(2))
# anotherItem.advance_status()
# anotherItem.advance_status()
# anotherItem.advance_status()
# anotherItem.advance_status()
# anotherItem.advance_status()
# print(anotherItem.history())

# =====================

# task = Task('Test the application flow', 'Steven', add_days_to_now(2))
# task.advance_status()
# task.advance_status()
# task.assignee = 'Not Steven'
# print(task.history())

# =====================

# issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
# task = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))
#
# for board_item in [issue, task]:
#     print(board_item.info())