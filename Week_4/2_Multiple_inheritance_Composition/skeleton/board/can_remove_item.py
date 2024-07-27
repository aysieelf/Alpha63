from board.board import Board
from board_items.board_item import BoardItem


class CanRemoveItem:
    def remove_item(self, item: BoardItem):
        Board.remove_item(item)
