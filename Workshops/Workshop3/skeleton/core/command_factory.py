from commands.add_test import AddTest
from commands.add_test_group import AddTestGroup
from commands.add_test_run import AddTestRun
from commands.remove_group import RemoveGroup
from commands.test_report import TestReport
from commands.view_group import ViewGroup
from commands.view_system import ViewSystem
from core.application_data import ApplicationData


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()
        commands = {
            "addtestgroup": AddTestGroup,
            "addtest": AddTest,
            "addtestrun": AddTestRun,
            "testreport": TestReport,
            "removegroup": RemoveGroup,
            "viewgroup": ViewGroup,
            "viewsystem": ViewSystem
        }

        if cmd.lower() not in commands:
            raise ValueError(f'Invalid command name: {cmd}!')

        return commands[cmd.lower()](params, self._app_data)



