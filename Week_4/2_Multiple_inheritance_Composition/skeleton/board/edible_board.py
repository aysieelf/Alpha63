from board.can_add_item import CanAddItem
from board.can_remove_item import CanRemoveItem
from board.board import Board


class EditableBoard(Board, CanAddItem, CanRemoveItem):
    pass
