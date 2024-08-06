import unittest
from unittest.mock import Mock

from commands.show_category import ShowCategoryCommand
from core.application_data import ApplicationData
from errors.invalid_params import InvalidParams
from models.product import Product
from tests.valid_values import VALID_PRODUCT_NAME, VALID_PRODUCT_BRAND, VALID_PRODUCT_PRICE, VALID_PRODUCT_GENDER, \
    VALID_CATEGORY_NAME


class ShowCategoryCommand_Should(unittest.TestCase):

    def setUp(self):
        self.app_data = ApplicationData()
        self.params = ["item"]

    def test_initAppData_validAppData(self):
        self.show_cat_cmd = ShowCategoryCommand(self.params, self.app_data)

        self.assertEqual(self.app_data, self.show_cat_cmd._app_data)
        self.assertIsInstance(self.show_cat_cmd._app_data, ApplicationData)

    def test_initParams_validParams(self):
        self.show_cat_cmd = ShowCategoryCommand(self.params, self.app_data)

        self.assertEqual(1, len(self.show_cat_cmd._params))
        self.assertIsInstance(self.show_cat_cmd._params, list)

    def test_initParams_invalidNumberParams(self):
        self.params = ["item1", "item2"]

        with self.assertRaises(InvalidParams):
            self.show_cat_cmd = ShowCategoryCommand(self.params, self.app_data)

    def test_executeMethod_withExistingCatName_withNoProducts(self):
        self.app_data.create_category(self.params[0])
        self.show_cat_cmd = ShowCategoryCommand(self.params, self.app_data)

        expected = f'#Category: {self.params[0]}\n #No products in this category'
        self.assertEqual(expected, self.show_cat_cmd.execute())

    def test_executeMethod_withExistingCatName_withProducts(self):
        self.app_data.create_category(self.params[0])
        self.show_cat_cmd = ShowCategoryCommand(self.params, self.app_data)
        product2 = Product(VALID_PRODUCT_NAME, VALID_PRODUCT_BRAND, VALID_PRODUCT_PRICE, VALID_PRODUCT_GENDER)
        self.app_data.categories[0].add_product(product2)

        new_line = "\n"
        product_strings = [p.to_string() for p in self.app_data.categories[0].products]
        expected = f'#Category: {self.app_data.categories[0].name}{new_line}{new_line.join(product_strings)}'

        self.assertEqual(expected, self.show_cat_cmd.execute())

    def test_execute_returnsOutput(self):
        # Arrange
        FAKE_CATEGORY_OUTPUT = 'fake output'
        CMD_NAME = 'cmd_name'
        category = Mock()
        category.to_string = lambda: FAKE_CATEGORY_OUTPUT

        app_data = Mock()
        app_data.find_category_by_name = lambda name: category if name == CMD_NAME else None

        command = ShowCategoryCommand([CMD_NAME], app_data)

        # Act
        actual_output = command.execute()

        # Assert
        self.assertEqual(FAKE_CATEGORY_OUTPUT, actual_output)
