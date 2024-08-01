from core.application_data import ApplicationData


class CreateCategoryCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        # Todo validate params
        self._params = params
        self._app_data = app_data

    def execute(self):
        category_name = self._params[0]
        if self._app_data.category_exists(category_name):
            raise ValueError(f'Category {category_name} already exists.')

        self._app_data.create_category(category_name)

        return f'Category with name {category_name} was created!'
