from datetime import date, timedelta
from board_item import BoardItem
from item_status import ItemStatus
from board import Board
from event_log import EventLog


def add_days_to_now(d):
    return date.today() + timedelta(days=d)