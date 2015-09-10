import unittest
import logging
from nose.tools import assert_true, assert_in, assert_not_in
from helpers.app_helpers import get_enabled_partners_data_keys, create_partner, delete_partner
from helpers import data_helpers as data


class PartnerTest(unittest.TestCase):
    def _get_partner_data(self, enabled=True):
        partner_data = data.create_partner_data()
        partner_data['name'] = 'DELETE_ME.{}'.format(partner_data['name'])
        if not enabled:
            partner_data['status'] = 0
        return partner_data

    def _create_partner(self, enabled=True):
        partner_data = self._get_partner_data(enabled=enabled)
        self.logger.info('partner_data: {}'.format(partner_data))
        partner_info = create_partner(partner_data)
        self.logger.info('partner_info: {}'.format(partner_info))
        assert_true(partner_info)
        self.partners_ids.append(partner_info.get('id'))
        return partner_info

    def setUp(self):
        self.partners_ids = []
        self.logger = logging.getLogger(self._testMethodName)

    def test_get_enabled_partners(self):
        partners_data_keys = get_enabled_partners_data_keys()
        assert_true(partners_data_keys)

    def test_create_enabled_partner(self):
        partner_info = self._create_partner()
        partners_data_keys = get_enabled_partners_data_keys()
        assert_in(partner_info.get('data_key'), partners_data_keys)

    def test_create_disabled_partner(self):
        partner_info = self._create_partner(enabled=False)
        partners_data_keys = get_enabled_partners_data_keys()
        assert_not_in(partner_info.get('data_key'), partners_data_keys)

    def test_delete_partner(self):
        partner_info = self._create_partner()
        delete_partner(partner_info.get('id'))
        partners_data_keys = get_enabled_partners_data_keys()
        assert_not_in(partner_info.get('data_key'), partners_data_keys)

    def tearDown(self):
        if self.partners_ids:
            for _id in self.partners_ids:
                delete_partner(_id)
