from datetime import date, timedelta
from board_item import BoardItem
from item_status import ItemStatus
from board import Board
from event_log import EventLog


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


#
#
item1 = BoardItem("Fix login bug", add_days_to_now(2))
print(item1)
item2 = BoardItem("Encrypt user data", add_days_to_now(10))
print(item2)

board = Board()
board.items.append(item1)
board.items.append(item2)

for board_item in board.items:
    board_item.advance_status()
    print(board_item.status)
#
self.assertEqual(board.items[0].status, ItemStatus.TODO)
self.assertEqual(board.items[1].status, ItemStatus.TODO)
#
# results = [board_item.info() for board_item in board.items]
#
# self.assertEqual(results[0], f"Fix login bug, [TODO | {add_days_to_now(2)}]")
# self.assertEqual(results[1], f"Encrypt user data, [TODO | {add_days_to_now(10)}]")
