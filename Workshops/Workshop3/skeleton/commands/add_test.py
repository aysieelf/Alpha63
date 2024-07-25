from commands.base.base_command import BaseCommand
from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData
from models.test import Test


class AddTest(BaseCommand):
    _id = 0

    @classmethod
    def get_next_id(cls):
        cls._id += 1
        return cls._id + 1

    def __init__(self,
                 params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 2)
        super().__init__(params, app_data)
        self.id = AddTest.get_next_id()

    def execute(self) -> str:
        test_group_id, description = self.params
        test_group_id = try_parse_int(test_group_id)

        test_group = self.app_data.find_test_group_by_id(test_group_id)
        test_group.add_test(Test(self.id, description))
        return f"Test #{self.id} added to group #{test_group_id}"
