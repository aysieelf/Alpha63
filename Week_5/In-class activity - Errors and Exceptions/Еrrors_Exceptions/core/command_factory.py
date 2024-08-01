from commands.add_to_category import AddToCategoryCommand

from commands.create_category import CreateCategoryCommand
from commands.create_product import CreateProductCommand

from commands.show_category import ShowCategoryCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        cmd, *params = input_line.split()

        if cmd.lower() == "createcategory":
            return CreateCategoryCommand(params, self._app_data)
        if cmd.lower() == "createproduct":
            return CreateProductCommand(params, self._app_data)
        if cmd.lower() == "showcategory":
            return ShowCategoryCommand(params, self._app_data)
        if cmd.lower() == "addproducttocategory":
            return AddToCategoryCommand(params, self._app_data)

        # Todo: validate command
