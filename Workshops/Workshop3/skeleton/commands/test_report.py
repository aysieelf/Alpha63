from commands.base.base_command import BaseCommand
from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData


class TestReport(BaseCommand):
    def __init__(self,
                 params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 1)
        super().__init__(params, app_data)

    def execute(self) -> str:
        test_id = self.params[0]
        test_id = try_parse_int(test_id)

        test = self.app_data.find_test_by_id(test_id)
        return (f"{test.to_string()}\n"
                f"- Passing: {test.passing_run_counts}\n"
                f"- Failing: {test.failing_run_counts}\n"
                f"- Total runtime: {test.total_runtime}ms\n"
                f"- Average runtime: {test.avg_run_time}ms")

