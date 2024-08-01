from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.user_role import UserRole
from models.user import User


class ShowUsersCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)

        if not self._app_data.logged_in_user.is_admin:
            raise ValueError("You are not an admin!")

        all_users = "--NO USERS--"
        if self._app_data.users:
            all_users = '\n'.join(f"{i + 1}. {str(user)}"
                                  for i, user in enumerate(self._app_data.users))

        return (f"--USERS--\n"
                f"{all_users}")

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0

