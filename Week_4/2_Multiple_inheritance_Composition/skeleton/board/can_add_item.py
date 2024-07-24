from board_items.board_item import BoardItem


class CanAddItem:
    def add_item(self, item: BoardItem):
        if item in self._items:
            raise ValueError(f"Item with title {item.title} already exists.")
        self._items.append(item)
