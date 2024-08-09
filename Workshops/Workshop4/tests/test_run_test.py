import unittest

from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from models.test_run import TestRun


class TestRun_Should(unittest.TestCase):

    def setUp(self):
        pass

    def test_constructor_raisesError_whenTestResultIsInvalid(self):
        with self.assertRaises(ValueError):
            TestRun(TestResult('failed'), 1)

    def test_constructor_raisesError_whenRuntimeIsInvalid(self):
        with self.assertRaises(ApplicationError):
            TestRun(TestResult.FAIL, 0)

    def test_propertiesReturnCorrectly_whenArgumentsAreValid(self):
        actual = TestRun(TestResult.FAIL, 1)

        self.assertEqual(TestResult.FAIL, actual.test_result)
        self.assertEqual(1, actual.runtime_ms)
