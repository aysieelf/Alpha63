import unittest

from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from models.test import Test
from models.test_group import TestGroup
from models.test_run import TestRun

GROUP_NAME = "group name"
TEST_NAME = "test name"


class ModelsFactory_Should(unittest.TestCase):
    def setUp(self):
        self.models_factory = ModelsFactory()

    def test_createGroup_createsCorrectIds(self):
        group1 = self.models_factory.create_group(GROUP_NAME)
        group2 = self.models_factory.create_group(GROUP_NAME)

        self.assertIsInstance(group1, TestGroup)
        self.assertEqual(1, group1.id)
        self.assertEqual(2, group2.id)

    def test_createTest_createsCorrectIds(self):
        test1 = self.models_factory.create_test(TEST_NAME)
        test2 = self.models_factory.create_test(TEST_NAME)

        self.assertIsInstance(test1, Test)
        self.assertEqual(1, test1.id)
        self.assertEqual(2, test2.id)

    def test_createTestRun_raisesError_whenTestResultInvalid(self):
        with self.assertRaises(ApplicationError):
            self.models_factory.create_test_run("failed", "1")

    def test_createTestRun_raisesError_whenRuntimeInvalid(self):
        with self.assertRaises(ApplicationError):
            self.models_factory.create_test_run("fail", "a")

    def test_createTestRun_createsSuccessfully(self):
        testrun1 = self.models_factory.create_test_run("fail", "1")

        self.assertIsInstance(testrun1, TestRun)
        self.assertEqual(TestResult.FAIL, testrun1.test_result)
        self.assertEqual(1, testrun1.runtime_ms)
