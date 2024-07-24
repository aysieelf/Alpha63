from board.can_add_item import CanAddItem
from board.board import Board


class ReadonlyBoard(Board, CanAddItem):
    pass
