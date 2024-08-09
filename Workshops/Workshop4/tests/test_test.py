import unittest
from unittest.mock import Mock

from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from models.test import Test


class Test_Should(unittest.TestCase):
    def setUp(self):
        self.actual = Test(1, "test name")
        self.testrun1 = self.create_mock_test_run()
        self.testrun2 = self.create_mock_test_run()
        self.testrun3 = self.create_mock_test_run(result=TestResult.FAIL)

    def create_mock_test_run(self,
                             result: TestResult = TestResult.PASS,
                             runtime: int = 1):
        test_run = Mock()
        test_run.test_result = result
        test_run.runtime_ms = runtime

        return test_run

    def test_constructor_raisesError_whenDescriptionIsNone(self):
        with self.assertRaises(ApplicationError):
            Test(1, None)

    def test_constructor_raisesError_whenDescriptionIsEmptyStr(self):
        with self.assertRaises(ApplicationError):
            Test(1, '')

    def test_idProperty_returnsCorrectValue_whenIdIsValid(self):
        self.assertEqual(1, self.actual.id)

    def test_descriptionProperty_returnsCorrectValue_whenDescriptionIsValid(self):
        self.assertEqual("test name", self.actual.description)

    def test_testRunsProperty_returnsTuple(self):
        self.assertIsInstance(self.actual.test_runs, tuple)

    def test_addTestRun_addsTestRunToTestRuns(self):
        self.actual.add_test_run(self.testrun1)

        self.assertEqual(1, len(self.actual.test_runs))

    def test_passingTestRunsProperty_returnsTupleOfTestRuns_whenPassingTestRunsExist(self):
        self.actual._test_runs = [self.testrun1, self.testrun2, self.testrun3]

        self.assertEqual((self.testrun1, self.testrun2), self.actual.passing_test_runs)

    def test_passingTestRunsProperty_returnsEmptyTuple_whenPassingTestRunsDoesNotExist(self):
        self.actual._test_runs = []

        self.assertEqual((), self.actual.passing_test_runs)

    def test_failingTestRunsProperty_returnsTupleOfTestRuns_whenFailingTestRunsExist(self):
        self.actual._test_runs = [self.testrun1, self.testrun2, self.testrun3]

        self.assertEqual((self.testrun3,), self.actual.failed_test_runs)

    def test_failingTestRunsProperty_returnsEmptyTuple_whenFailingTestRunsDoesNotExist(self):
        self.actual._test_runs = []

        self.assertEqual((), self.actual.failed_test_runs)

    def test_totalRuntimeProperty_returnsSumOfRuntime_whenTestRunsExist(self):
        self.actual._test_runs = [self.testrun1, self.testrun2, self.testrun3]

        self.assertEqual(3, self.actual.total_runtime)

    def test_totalRuntimeProperty_returns0_whenTestRunsDoesNotExist(self):
        self.actual._test_runs = []

        self.assertEqual(0, self.actual.total_runtime)

    def test_avgRuntimeProperty_returnsAverageRuntime_whenTestRunsExist(self):
        self.actual._test_runs = [self.testrun1, self.testrun2, self.testrun3]

        self.assertEqual(1.0, self.actual.avg_runtime)

    def test_avgRuntimeProperty_returns0_whenTestRunsDoesNotExist(self):
        self.actual._test_runs = []

        self.assertEqual(0.0, self.actual.avg_runtime)

    def test_generateReport_returnsCorrectFormat_whenRunTestsExist(self):
        self.actual._test_runs = [self.testrun1, self.testrun2, self.testrun3]
        expected = '\n'.join([
            f'{self.actual}',
            f'- Passing: {len(self.actual.passing_test_runs)}',
            f'- Failing: {len(self.actual.failed_test_runs)}',
            f'- Total runtime: {self.actual.total_runtime}ms',
            f'- Average runtime: {self.actual.avg_runtime:.1f}ms'])

        self.assertEqual(expected, self.actual.generate_report())

    def test_generateReport_returnsCorrectFormat_whenNoRunTests(self):
        self.actual._test_runs = []
        expected = str(self.actual)

        self.assertEqual(expected, self.actual.generate_report())

    def test_strMethod_IsImplemented(self):
        expected = (f'#{self.actual.id}. '
                    f'[{self.actual.description}]: '
                    f'{len(self.actual.test_runs)} runs')

        self.assertEqual(expected, str(self.actual))
