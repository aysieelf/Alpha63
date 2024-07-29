from commands.add_comment import AddCommentCommand
from commands.add_vehicle import AddVehicleCommand
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.register_user import RegisterUserCommand
from commands.remove_comment import RemoveCommentCommand
from commands.remove_vehicle import RemoveVehicleCommand
from commands.show_users import ShowUsersCommand
from commands.show_vehicles import ShowVehiclesCommand


class CommandFactory:
    COMMANDS = {
            "LOGIN": LoginCommand,
            "LOGOUT": LogoutCommand,
            "SHOWUSERS": ShowUsersCommand,
            "ADDCOMMENT": AddCommentCommand,
            "ADDVEHICLE": AddVehicleCommand,
            "REGISTERUSER": RegisterUserCommand,
            "SHOWVEHICLES": ShowVehiclesCommand,
            "REMOVECOMMENT": RemoveCommentCommand,
            "REMOVEVEHICLE": RemoveVehicleCommand
    }

    def __init__(self, data):
        self._app_data = data

    def create(self, cmd_name):
        if cmd_name.upper() not in CommandFactory.COMMANDS:
            raise ValueError('Invalid command name')

        return CommandFactory.COMMANDS[cmd_name.upper()](self._app_data)


