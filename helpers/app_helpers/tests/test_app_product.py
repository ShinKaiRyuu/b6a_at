import unittest
import logging
from nose.tools import assert_true
from helpers.app_helpers import create_product, delete_product
from helpers import data_helpers as data


class ProductTest(unittest.TestCase):
    def _get_product_data(self):
        product_data = data.create_product_data()
        product_data['title'] = 'DELETE_ME.{}'.format(product_data['title'])
        return product_data

    def _create_product(self, disabled=False):
        product_data = self._get_product_data()
        if disabled:
            product_data['enabled'] = 0
        self.logger.info('product_data: {}'.format(product_data))
        product_info = create_product(product_data)
        self.logger.info('product_info: {}'.format(product_info))
        assert_true(product_info)
        self.products_ids.append(product_info.get('id'))
        return product_info

    def setUp(self):
        self.products_ids = []
        self.logger = logging.getLogger(self._testMethodName)

    def test_create_product(self):
        self._create_product()

    def test_create_blocked_product(self):
        self._create_product(disabled=True)

    def test_delete_product(self):
        product_info = self._create_product()
        delete_product(product_info.get('id'))

    def tearDown(self):
        if self.products_ids:
            for _id in self.products_ids:
                delete_product(_id)
