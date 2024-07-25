from core.application_data import ApplicationData
from commands.validation_helpers import try_parse_int, validate_params_count
from commands.create_product import CreateProductCommand


class CreateShampooCommand(CreateProductCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 6)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        try_parse_int(self._params[4])
        self._app_data.create_shampoo(*self._params)

        return f'Shampoo with name {self._params[0]} was created!'