import unittest
from unittest.mock import Mock

from commands.add_test import AddTestCommand
from commands.add_test_group import AddTestGroupCommand
from commands.add_test_run import AddTestRunCommand
from commands.remove_group import RemoveGroupCommand
from commands.test_report import TestReportCommand
from commands.view_group import ViewGroupCommand
from commands.view_system import ViewSystemCommand
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError


class CommandFactory_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = Mock()
        self.models_factory = Mock()
        self.command_factory = CommandFactory(self.app_data)

    def test_create_raisesError_invalidCommand(self):
        input_line = "InvalidCommand"

        with self.assertRaises(ApplicationError):
            self.command_factory.create(input_line)

    def test_create_commandCreated_AddTestCommand(self):
        input_line = "addtest"
        actual = self.command_factory.create(input_line)

        self.assertIsInstance(actual, AddTestCommand)

    def test_create_commandCreated_AddTestGroupCommand(self):
        input_line = "addtestgroup"
        actual = self.command_factory.create(input_line)

        self.assertIsInstance(actual, AddTestGroupCommand)

    def test_create_commandCreated_RemoveGroupCommand(self):
        input_line = "removegroup"
        actual = self.command_factory.create(input_line)

        self.assertIsInstance(actual, RemoveGroupCommand)

    def test_create_commandCreated_AddTestRunCommand(self):
        input_line = "addtestrun"
        actual = self.command_factory.create(input_line)

        self.assertIsInstance(actual, AddTestRunCommand)

    def test_create_commandCreated_TestReportCommand(self):
        input_line = "testreport"
        actual = self.command_factory.create(input_line)

        self.assertIsInstance(actual, TestReportCommand)

    def test_create_commandCreated_ViewGroupCommand(self):
        input_line = "viewgroup"
        actual = self.command_factory.create(input_line)

        self.assertIsInstance(actual, ViewGroupCommand)

    def test_create_commandCreated_ViewSystemCommand(self):
        input_line = "viewsystem"
        actual = self.command_factory.create(input_line)

        self.assertIsInstance(actual, ViewSystemCommand)

    def test_create_commandCreated_withNoParamsValidCommand(self):
        input_line = "viewsystem"
        actual = self.command_factory.create(input_line)

        self.assertEqual((), actual.params)

    def test_create_commandCreated_withMultipleParamsValidCommand(self):
        input_line = "viewsystem param0 param1 param2"
        actual = self.command_factory.create(input_line)

        self.assertEqual(3, len(actual.params))
        self.assertEqual("param0", actual.params[0])
        self.assertEqual("param1", actual.params[1])
        self.assertEqual("param2", actual.params[2])

    def test_create_commandHasModelsFactoryAttribute(self):
        input_lines = ["addtest", "addtestgroup", "addtestrun"]

        for i in range(len(input_lines)):
            actual = self.command_factory.create(input_lines[i])
            self.assertIsInstance(actual.models_factory, ModelsFactory)

    def test_create_commandHasAppDataAttribute(self):
        input_lines = ["addtest", "addtestgroup", "addtestrun",
                       "removegroup", "testreport", "viewgroup",
                       "viewsystem"]

        for i in range(len(input_lines)):
            actual = self.command_factory.create(input_lines[i])
            self.assertEqual(self.app_data, actual.app_data)

    def test_create_commandCreated_withDifferentStrings(self):
        input_lines = ["addtest", "AddTest", "ADDTEST"]

        for i in range(len(input_lines)):
            actual = self.command_factory.create(input_lines[i])
            self.assertIsInstance(actual, AddTestCommand)
