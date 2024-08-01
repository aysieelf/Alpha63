from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData


class CreateCategoryCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = validate_params_count(params, self.__class__.__name__, 1)
        self._app_data = app_data

    def execute(self):
        category_name = self._params[0]
        if self._app_data.category_exists(category_name):
            raise ValueError(f'Category {category_name} already exists.')

        self._app_data.create_category(category_name)

        return f'Category with name {category_name} was created!'
