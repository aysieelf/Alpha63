import unittest

from models.gender import Gender
from models.product import Product
from tests.valid_values import VALID_PRODUCT_NAME, VALID_PRODUCT_BRAND, VALID_PRODUCT_PRICE, VALID_PRODUCT_GENDER


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

    def test_setterSetsCorrectlyName_validName(self):
        self.product.name = "new name"
        self.assertEqual("new name", self.product.name)

    def test_setterSetsCorrectlyBrand_validBrand(self):
        self.product.brand = "new brand"
        self.assertEqual("new brand", self.product.brand)

    def test_setterSetsCorrectlyPrice_validPrice(self):
        self.product.price = 3.4
        self.assertEqual(3.4, self.product.price)

    def test_setterRaisesValueError_invalidName(self):
        with self.assertRaises(ValueError):
            self.product.name = "new name new name"

    def test_setterRaisesValueError_invalidBrand(self):
        with self.assertRaises(ValueError):
            self.product.brand = "new brand new brand"

    def test_setterRaisesValueError_invalidPrice(self):
        with self.assertRaises(ValueError):
            self.product.price = -9

    def test_toStringReturnsValidOutput(self):
        expected = '\n'.join([
            f' #{self.product.name} {self.product.brand}',
            f' #Price: ${self.product.price:.2f}',
            f' #Gender: {self.product.gender.value}',
            ' ==='
        ])

        self.assertEqual(expected, self.product.to_string())