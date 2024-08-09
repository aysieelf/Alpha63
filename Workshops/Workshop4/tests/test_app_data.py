import unittest
from unittest.mock import Mock

from core.application_data import ApplicationData


class ApplicationData_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()

        self.group = Mock()
        self.group.id = 1

        self.test = Mock()
        self.test.id = 1
        self.group.tests = [self.test]

    def test_propertyGroups_returnsTuple(self):
        self.assertIsInstance(self.app_data.groups, tuple)

    def test_addGroup_addsGroupAndReturnsTrue_whenTestGroupNotExisting(self):
        actual = self.app_data.add_group(self.group)

        self.assertTrue(actual)
        self.assertEqual(1, len(self.app_data.groups))

    def test_addGroup_returnsFalse_whenTestGroupAlreadyExists(self):
        self.app_data.add_group(self.group)
        actual = self.app_data.add_group(self.group)

        self.assertFalse(actual)
        self.assertEqual(1, len(self.app_data.groups))

    def test_removeGroup_removesGroupAndReturnsTrue_whenTestGroupExists(self):
        self.app_data.add_group(self.group)
        actual = self.app_data.remove_group(1)

        self.assertTrue(actual)
        self.assertEqual(0, len(self.app_data.groups))

    def test_removeGroup_returnsFalse_whenTestGroupDoesNotExist(self):
        actual = self.app_data.remove_group(1)

        self.assertFalse(actual)
        self.assertEqual(0, len(self.app_data.groups))

    def test_findGroup_returnsGroup_whenTestGroupExists(self):
        self.app_data.add_group(self.group)
        actual = self.app_data.find_group(1)

        self.assertEqual(self.group, actual)

    def test_findGroup_returnsNone_whenTestGroupDoesNotExist(self):
        actual = self.app_data.find_group(1)

        self.assertIsNone(actual)

    def test_findTest_returnsTest_whenTestExists(self):
        self.app_data.add_group(self.group)
        actual = self.app_data.find_test(1)

        self.assertEqual(self.test, actual)

    def test_findTest_returnsTest_whenTestDoesNotExist(self):
        actual = self.app_data.find_test(1)

        self.assertIsNone(actual)
