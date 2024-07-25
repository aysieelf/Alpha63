from models.test import Test


class TestGroup:
    def __init__(self,
                 id: int,
                 name: str):

        self._id = id
        self._name = name
        self._tests: dict[id:Test] = {}

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def tests(self) -> tuple:
        return tuple(self._tests.items())

    def add_test(self, test: Test) -> None:
        self._tests[test.id] = test

    def get_test_by_id(self, id: int) -> Test:
        if id in self._tests:
            return self._tests[id]

    def to_string(self) -> str:
        return f"#{self.id}. {self.name} ({len(self._tests)} tests)"

    def all_tests_to_string(self) -> str:
        return '\n  '.join(test.to_string() for test in self._tests.values())

