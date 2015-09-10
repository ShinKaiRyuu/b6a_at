import unittest
import logging
from nose.tools import assert_true
from helpers.app_helpers import create_page, delete_page
from helpers import data_helpers as data


class PageTest(unittest.TestCase):
    def _get_page_data(self):
        page_data = data.create_page_data()
        page_data['name'] = 'DELETE_ME.{}'.format(page_data['name'])
        return page_data

    def _create_page(self, draft=False):
        page_data = self._get_page_data()
        if draft:
            page_data['status'] = 'draft'
        self.logger.info('parent page_data: {}'.format(page_data))
        page_info = create_page(page_data)
        self.logger.info('parent page_info: {}'.format(page_info))
        assert_true(page_info)
        self.pages_ids.append(page_info.get('id'))
        return page_info

    def _create_additional_page(self, draft=False):
        parent_page_info = self._create_page()
        addit_page_data = self._get_page_data()
        addit_page_data['parent_id'] = parent_page_info.get('data_key')
        if draft:
            addit_page_data['status'] = 'draft'
        self.logger.info('additional page_data: {}'.format(addit_page_data))
        addit_page_info = create_page(addit_page_data)
        assert_true(addit_page_info)
        self.logger.info('additional page_info: {}'.format(addit_page_info))
        self.pages_ids.insert(0, addit_page_info.get('id'))
        return addit_page_info

    def setUp(self):
        self.pages_ids = []
        self.logger = logging.getLogger(self._testMethodName)

    def test_create_parent_page(self):
        self._create_page()

    def test_create_draft_parent_page(self):
        self._create_page(draft=True)

    def test_create_additional_page(self):
        self._create_additional_page()

    def test_create_draft_additional_page(self):
        self._create_additional_page(draft=True)

    def test_delete_parent_page(self):
        page_info = self._create_page()
        delete_page(page_info.get('id'))

    def test_delete_additional_page(self):
        addit_page_info = self._create_additional_page()
        delete_page(addit_page_info.get('id'))

    def tearDown(self):
        if self.pages_ids:
            for _id in self.pages_ids:
                delete_page(_id)
