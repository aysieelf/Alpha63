from commands.base.base_command import BaseCommand
from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData
from models.test_group import TestGroup


class AddTestGroup(BaseCommand):
    _id = 0

    @classmethod
    def get_next_id(cls):
        cls._id += 1
        return cls._id + 1

    def __init__(self,
                 params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 1)
        super().__init__(params, app_data)
        AddTestGroup._id += 1
        self.id = AddTestGroup.get_next_id()

    def execute(self) -> str:
        name = self.params[0]
        self.app_data.add_test_group(TestGroup(self.id, name))
        return f"Group #{self.id} created"
