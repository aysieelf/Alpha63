from core.application_data import ApplicationData


class AddToCategoryCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        # Todo validate params
        self._params = params
        self._app_data = app_data

    def execute(self):
        category_name, product_name = self._params
        category = self._app_data.find_category_by_name(category_name)
        product = self._app_data.find_product_by_name(product_name)

        category.add_product(product)

        return f'Product {product_name} added to category {category_name}!'
