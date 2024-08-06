import unittest
from unittest.mock import Mock
from models.category import Category
from models.product import Product
from tests.valid_values import VALID_PRODUCT_NAME, VALID_PRODUCT_BRAND, VALID_PRODUCT_PRICE, VALID_PRODUCT_GENDER, \
    VALID_CATEGORY_NAME


class Category_Should(unittest.TestCase):

    @staticmethod
    def create_mock_product(name):
        product = Mock()
        product.name = name
        product.to_string = lambda: VALID_PRODUCT_NAME

        return product

    def setUp(self):
        self.category = Category(VALID_CATEGORY_NAME)

    def test_initName_validName(self):
        self.assertEqual(VALID_CATEGORY_NAME, self.category.name)

    def test_initRaisesValueError_invalidName(self):
        with self.assertRaises(ValueError):
            Category("a")

    def test_GetterReceivesTuple(self):
        self.assertIsInstance(self.category.products, tuple)

    def test_setterSetsCorrectlyName_validName(self):
        self.category.name = "dog name"
        self.assertEqual("dog name", self.category.name)

    def test_setterRaisesValueError_invalidName(self):
        with self.assertRaises(ValueError):
            self.category.name = "a"

    def test_addProductAddSuccessfully_newProduct(self):
        self.category.add_product(self.create_mock_product(VALID_PRODUCT_NAME))
        self.assertEqual(tuple([self.create_mock_product(VALID_PRODUCT_NAME)]), self.category.products)

    def test_addProductRaisesValueError_existingProduct(self):
        self.category.add_product(self.create_mock_product(VALID_PRODUCT_NAME))

        with self.assertRaises(ValueError):
            self.category.add_product(self.create_mock_product(VALID_PRODUCT_NAME))

    def test_removeProductRemovesSuccessfully_existingProduct(self):
        self.category.add_product(self.create_mock_product(VALID_PRODUCT_NAME))
        self.category.remove_product(self.create_mock_product(VALID_PRODUCT_NAME))
        self.assertEqual(tuple([]), self.category.products)

    def test_removeProductRaisesValueError_nonExistingProduct(self):
        with self.assertRaises(ValueError):
            self.category.remove_product(self.create_mock_product(VALID_PRODUCT_NAME))

    def test_toStringReturnsValidOutput_noProducts(self):
        expected = f'#Category: {self.category.name}\n #No products in this category'

        self.assertEqual(expected, self.category.to_string())

    def test_toStringReturnsValidOutput_hasProducts(self):

        new_line = "\n"
        self.category.add_product(self.create_mock_product('prod 1'))
        self.category.add_product(self.create_mock_product('prod 2'))

        product_strings = [p.to_string() for p in self.category.products]
        expected = f'#Category: {self.category.name}{new_line}{new_line.join(product_strings)}'

        self.assertEqual(expected, self.category.to_string())
