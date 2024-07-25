from commands.base.base_command import BaseCommand
from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData


class RemoveGroup(BaseCommand):
    def __init__(self,
                 params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 1)
        super().__init__(params, app_data)

    def execute(self) -> str:
        test_group_id = self.params[0]
        test_group_id = try_parse_int(test_group_id)

        self.app_data.remove_test_group_by_id(test_group_id)
        return f"Group #{test_group_id} removed"
