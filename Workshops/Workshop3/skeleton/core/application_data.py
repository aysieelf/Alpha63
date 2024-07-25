from models.test import Test
from models.test_group import TestGroup


class ApplicationData:
    def __init__(self):
        self._test_groups: dict[str:TestGroup] = {}

    @property
    def groups(self):
        return tuple(self._test_groups.items())

    def add_test_group(self, test_group: TestGroup) -> None:
        self._test_groups[test_group.id] = test_group

    def find_test_group_by_id(self, id: int) -> TestGroup:
        if id not in self._test_groups:
            raise ValueError(f"Test group with id {id} doesn't exist.")

        return self._test_groups[id]

    def remove_test_group_by_id(self, id: int) -> None:
        if id not in self._test_groups:
            raise ValueError(f"Test group with id {id} doesn't exist.")

        del self._test_groups[id]

    def find_test_by_id(self, id: int) -> Test:
        for test_group in self._test_groups.values():
            test = test_group.get_test_by_id(id)
            if test:
                return test

        raise ValueError(f"Test with id {id} doesn't exist.")

    def to_string(self):
        groups_str = '\n  '.join(group.to_string() for group in self._test_groups.values())
        return (f"Test Reporter System ({len(self._test_groups)} test groups)\n"
                f"  {groups_str}")
