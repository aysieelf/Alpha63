from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_float

class CreateProductCommand:

    def __init__(self, params, app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        product = self._params[0]
        if self._app_data.product_exists(product):
            raise ValueError(f'{self.__class__.__name__} with name {product} already exists!')
        try_parse_float(self._params[2])
        Gender.from_string(self._params[3])