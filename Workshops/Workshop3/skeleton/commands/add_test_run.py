from commands.base.base_command import BaseCommand
from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData
from models.constants.test_result import TestResult
from models.test_run import TestRun


class AddTestRun(BaseCommand):
    def __init__(self,
                 params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 3)
        super().__init__(params, app_data)

    def execute(self) -> str:
        test_id, test_result, runtime_ms = self.params

        test_id = try_parse_int(test_id)
        test_result = TestResult.validate_result(test_result)
        runtime_ms = try_parse_int(runtime_ms)

        test = self.app_data.find_test_by_id(test_id)
        test.add_test_run(TestRun(test_result, runtime_ms))
        return "TestRun registered"
