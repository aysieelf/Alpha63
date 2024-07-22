class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'
    _item_status_list = (OPEN, TODO, IN_PROGRESS, DONE, VERIFIED)

    @classmethod
    def next(cls, current) -> str:
        index = cls._item_status_list.index(current)
        if index + 1 == len(cls._item_status_list):
            return current
        return cls._item_status_list[index+1]

    @classmethod
    def previous(cls, current) -> str:
        index = cls._item_status_list.index(current)
        if index - 1 < 0:
            return current
        return cls._item_status_list[index-1]
