from models.constants.test_result import TestResult


class TestRun:
    def __init__(self,
                 test_result: str,
                 runtime_ms: int):

        self._test_result = TestResult.validate_result(test_result)
        self._runtime_ms = runtime_ms

    @property
    def test_result(self) -> str:
        return self._test_result

    @property
    def runtime_ms(self) -> int:
        return self._runtime_ms
