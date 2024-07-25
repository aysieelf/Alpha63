from models.constants.test_result import TestResult
from models.test_run import TestRun


class Test:
    def __init__(self,
                 id: int,
                 description: str):

        self._id = id
        self._description = description
        self._test_runs: list[TestRun] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def description(self) -> str:
        return self._description

    @property
    def test_runs(self) -> tuple:
        return tuple(self._test_runs)

    def add_test_run(self, test_run: TestRun) -> None:
        self._test_runs.append(test_run)

    @property
    def passing_run_counts(self) -> int:
        return sum(1 for run in self.test_runs if run.test_result == TestResult.PASS)

    @property
    def failing_run_counts(self) -> int:
        return sum(1 for run in self.test_runs if run.test_result == TestResult.FAIL)

    @property
    def total_runtime(self) -> int:
        total_runtime = 0
        for test_run in self.test_runs:
            total_runtime += test_run.runtime_ms

        return total_runtime

    @property
    def avg_run_time(self) -> float:
        if not self.test_runs:
            return 0
        return round(self.total_runtime / len(self._test_runs), 1)

    def to_string(self) -> str:
        return f"#{self.id}. [{self.description}]: {len(self.test_runs)} runs"
