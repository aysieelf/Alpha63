import unittest
from unittest.mock import Mock

from errors.application_error import ApplicationError
from models.test_group import TestGroup


class TestGroup_Should(unittest.TestCase):
    def setUp(self):
        self.actual = TestGroup(1, "group name")

    def create_mock_test(self, id: int = 1, info: str = 'test1'):
        test = Mock()
        test.id = id
        test.__str__ = lambda self: info

        return test

    def test_constructor_raisesError_whenNameIsNone(self):
        with self.assertRaises(ApplicationError):
            TestGroup(1, None)

    def test_constructor_raisesError_whenNameIsEmptyStr(self):
        with self.assertRaises(ApplicationError):
            TestGroup(1, '')

    def test_properties_returnCorrectly_whenArgumentsAreValid(self):

        self.assertEqual(1, self.actual.id)
        self.assertEqual("group name", self.actual.name)
        self.assertIsInstance(self.actual.tests, tuple)

    def test_addTest_appendsTestToTests_whenTestNotInTests(self):
        self.actual.add_test(self.create_mock_test())

        self.assertEqual(1, len(self.actual.tests))

    def test_addTest_doesNothing_whenTestAlreadyInTests(self):
        self.actual.add_test(self.create_mock_test())

        # adds the same test a second time
        self.actual.add_test(self.create_mock_test())

        self.assertEqual(1, len(self.actual.tests))

    def test_view_returnsCorrectStringFormat(self):
        self.actual.add_test(self.create_mock_test())
        test = self.create_mock_test(2, "test2")
        self.actual.add_test(test)

        expected = '\n'.join([f'{self.actual}'] + [f'  {test}' for test in self.actual.tests])

        self.assertEqual(expected, self.actual.view())

    def test_strMethod_IsImplemented(self):
        expected = f'#{self.actual.id}. {self.actual.name} ({len(self.actual.tests)} tests)'

        self.assertEqual(expected, str(self.actual))
