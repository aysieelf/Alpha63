from datetime import date, timedelta
from user.user import User
from board_items.task import Task
from board.board import Board
from board_items.issue import Issue
from board.edible_board import EditableBoard
from board.readonly_board import ReadonlyBoard
from board_items.item_status import ItemStatus


def add_days_to_now(d):
    return date.today() + timedelta(days=d)

board = Board()
steven = board.add_user("Steven", "steven@asd.bg")
task1 = Task('Test the application flow', steven, add_days_to_now(2))
steven.receive_task(task1)
board.add_item(task1)
print(f"Capacity of the team: {board.team_capacity}")
peter = board.add_user("Peter", "peter@asd.bg")
print(f"Capacity of the team: {board.team_capacity}")
print("============================================")

task2 = Task('Fix authentication', steven, add_days_to_now(2))
board.add_item(task2)
peter.receive_task(task2)
print(f"Capacity of the team: {board.team_capacity}")
print(task1.status)
steven.advance_task_status(task1)
print(task1.status)
board.reassign_task(task1, peter)
print(f"Steven assigned tasks: {steven.assigned_tasks}")
print(f"Peter assigned tasks: {[task.info() for task in peter.assigned_tasks]}")
print(task1.status)
peter.advance_task_status(task1)
print(task1.status)
peter.advance_task_status(task1)
print(task1.status)
print(f"Capacity of the team: {board.team_capacity}")
print(task1.history())

# =============================
#
# issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
#
# readonly_board = ReadonlyBoard()
# steven = readonly_board.add_user("Steven", "steven@asd.bg")
# task = Task("Don't refactor anything", steven, add_days_to_now(2))
# #
# readonly_board.add_item(issue)  # method from CanAddItem
# readonly_board.add_item(task)
# print(readonly_board.count)  # 2     # property from Board
#
# editable_board = EditableBoard()
# editable_board.add_item(issue)  # method from CanAddItem
# editable_board.remove_item(issue)  # method from CanRemoveItem
# print(editable_board.count)  # 0     # property from Board
#
