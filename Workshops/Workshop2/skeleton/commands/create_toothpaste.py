from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count
from commands.create_product import CreateProductCommand


class CreateToothpasteCommand(CreateProductCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        self._app_data.create_toothpaste(*self._params)

        return f'Toothpaste with name {self._params[0]} was created!'
