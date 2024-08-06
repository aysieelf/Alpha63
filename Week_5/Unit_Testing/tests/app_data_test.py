import unittest
from unittest.mock import Mock

from core.application_data import ApplicationData
from models.product import Product
from tests.valid_values import VALID_PRODUCT_NAME, VALID_PRODUCT_BRAND, VALID_PRODUCT_PRICE, VALID_PRODUCT_GENDER


class ApplicationData_Should(unittest.TestCase):

    def setUp(self) -> None:
        self.app_data = ApplicationData()
        self.category = Mock()
        self.product = Mock()

    def test_getterProductsReturnsListInTuple(self):
        self.assertEqual(tuple([]), self.app_data.products)

    def test_getterCategoriesReturnsListInTuple(self):
        self.assertEqual(tuple([]), self.app_data.categories)

    def test_createProduct_createsSuccessfully_whenProductIsNew(self):
        self.app_data.create_product(VALID_PRODUCT_NAME,
                                     VALID_PRODUCT_BRAND,
                                     VALID_PRODUCT_PRICE,
                                     VALID_PRODUCT_GENDER)

        self.assertEqual(1, len(self.app_data.products))
        self.assertIsInstance(self.app_data.products[0], Product)

    def test_createProduct_raisesValueError_whenProductExists(self):
        self.app_data.create_product(VALID_PRODUCT_NAME,
                                     VALID_PRODUCT_BRAND,
                                     VALID_PRODUCT_PRICE,
                                     VALID_PRODUCT_GENDER)

        with self.assertRaises(ValueError):
            self.app_data.create_product(VALID_PRODUCT_NAME,
                                         VALID_PRODUCT_BRAND,
                                         VALID_PRODUCT_PRICE,
                                         VALID_PRODUCT_GENDER)

    def test_findProductByName_ReturnsCorrectProduct_whenProductExists(self):
        self.app_data.create_product(VALID_PRODUCT_NAME,
                                     VALID_PRODUCT_BRAND,
                                     VALID_PRODUCT_PRICE,
                                     VALID_PRODUCT_GENDER)
        actual = self.app_data.find_product_by_name(VALID_PRODUCT_NAME)
        self.assertEqual(VALID_PRODUCT_NAME, actual.name)

    def test_findProductByName_RaisesValueError_whenProductDoesNotExists(self):
        with self.assertRaises(ValueError):
            self.app_data.find_product_by_name(VALID_PRODUCT_NAME)

    def test_productExists_whenProductExists(self):
        self.app_data.create_product(VALID_PRODUCT_NAME,
                                     VALID_PRODUCT_BRAND,
                                     VALID_PRODUCT_PRICE,
                                     VALID_PRODUCT_GENDER)

        self.assertEqual(True, self.app_data.product_exists(VALID_PRODUCT_NAME))

    def test_productExists_whenProductDoesNotExist(self):
        self.assertEqual(False, self.app_data.product_exists(VALID_PRODUCT_NAME))