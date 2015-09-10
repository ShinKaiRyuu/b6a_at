import unittest
import logging
from nose.tools import assert_true
from helpers.app_helpers import create_inventory_group, delete_inventory_group
from helpers import data_helpers as data


class InventoryGroupTest(unittest.TestCase):
    def _get_inventory_group_data(self):
        inventory_group_data = data.create_inventory_group_data()
        inventory_group_data['name'] = 'DELETE_ME.{}'.format(inventory_group_data['name'])
        return inventory_group_data

    def _create_inventory_group(self):
        inventory_group_data = self._get_inventory_group_data()
        self.logger.info('inventory_group_data: {}'.format(inventory_group_data))
        inventory_group_info = create_inventory_group(inventory_group_data)
        self.logger.info('inventory_group_info: {}'.format(inventory_group_info))
        assert_true(inventory_group_info)
        self.inventory_groups_ids.append(inventory_group_info.get('id'))
        return inventory_group_info

    def setUp(self):
        self.inventory_groups_ids = []
        self.logger = logging.getLogger(self._testMethodName)

    def test_create_inventory_group(self):
        self._create_inventory_group()

    def test_delete_inventory_group(self):
        inventory_group_info = self._create_inventory_group()
        delete_inventory_group(inventory_group_info.get('id'))

    def tearDown(self):
        if self.inventory_groups_ids:
            for _id in self.inventory_groups_ids:
                delete_inventory_group(_id)
