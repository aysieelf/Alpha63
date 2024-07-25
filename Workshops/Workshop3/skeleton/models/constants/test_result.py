class TestResult:
    PASS = 'pass'
    FAIL = 'fail'

    @classmethod
    def validate_result(cls, value: str) -> str:
        if value.lower() in [cls.PASS, cls.FAIL]:
            return value.lower()
        raise ValueError("Accepted results are: 'pass', 'fail'.")