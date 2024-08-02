import unittest

from models.gender import Gender
from models.product import Product

VALID_PRODUCT_NAME = "test name"
VALID_PRODUCT_BRAND = "test brand"
VALID_PRODUCT_PRICE = 4.5
VALID_PRODUCT_GENDER = Gender.UNISEX


class Product_Should(unittest.TestCase):

    def setUp(self):
        self.product = Product(VALID_PRODUCT_NAME,
                               VALID_PRODUCT_BRAND,
                               VALID_PRODUCT_PRICE,
                               VALID_PRODUCT_GENDER)

    def test_initName_validName(self):
        self.assertEqual(VALID_PRODUCT_NAME, self.product.name)

    def test_initBrand_validBrand(self):
        self.assertEqual(VALID_PRODUCT_BRAND, self.product.brand)

    def test_initPrice_validPrice(self):
        self.assertEqual(VALID_PRODUCT_PRICE, self.product.price)

    def test_initGender_validGender(self):
        self.assertEqual(VALID_PRODUCT_GENDER, self.product.gender)

    def test_initNameRaisesValueError_invalidName(self):
        with self.assertRaises(ValueError):
            Product("a", VALID_PRODUCT_BRAND, VALID_PRODUCT_PRICE, VALID_PRODUCT_GENDER)

    def test_initBrandRaisesValueError_invalidBrand(self):
        with self.assertRaises(ValueError):
            Product(VALID_PRODUCT_NAME, 'a', VALID_PRODUCT_PRICE, VALID_PRODUCT_GENDER)

    def test_initPriceRaisesValueError_invalidPrice(self):
        with self.assertRaises(ValueError):
            Product(VALID_PRODUCT_NAME, VALID_PRODUCT_BRAND, -1, VALID_PRODUCT_GENDER)

    # def test_initGenderRaisesValueError_invalidGender(self):
    #     with self.assertRaises(ValueError):
    #         Product(VALID_PRODUCT_NAME, VALID_PRODUCT_BRAND, VALID_PRODUCT_PRICE, 'asd')

    def test_setterSetsCorrectly_validName(self):
        self.product.name = "new name"
        self.assertEqual("new name", self.product.name)