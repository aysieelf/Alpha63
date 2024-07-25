from commands.base.base_command import BaseCommand
from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData


class ViewSystem(BaseCommand):
    def __init__(self,
                 params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 0)
        super().__init__(params, app_data)

    def execute(self) -> str:
        return self.app_data.to_string()
