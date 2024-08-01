from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData


class ShowCategoryCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        # Todo validate params
        self._params = validate_params_count(params, self.__class__.__name__, 1)
        self._app_data = app_data

    def execute(self):
        category_name = self._params[0]
        category = self._app_data.find_category_by_name(category_name)

        return category.to_string()
