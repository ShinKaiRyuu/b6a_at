from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webium import Finds, Find

from pages.base_page import BasePage

PERMISSION_COLUMNS_MAP = {
    '1': 'name',
    '2': 'description',
    '3': 'rule_name',
    '4': 'data_key'
}


class ManagePermissionPage(BasePage):
    url_path = '/rbac/permission/index'

    name_filter = Find(by=By.XPATH, value='//input[@name="Search[name]"]')
    description_filter = Find(by=By.XPATH, value='//input[@name="Search[description]"]')
    rule_name_filter = Find(by=By.XPATH, value='//input[@name="Search[rule_name]"]')

    permission_record_xpath = '//tr[@data-key]'
    permission_column_xpath = '//tr[@data-key="{}"]/td[{}]'
    permission_column_links_xpath = '//tr[@data-key="{}"]/td/a[@title]'
    permission_records = Finds(by=By.XPATH, value=permission_record_xpath)

    def get_permissions(self):
        permissions = [
            {
                column_name: self._get_permission_column_value(data_key, column_name)
                for column_name in PERMISSION_COLUMNS_MAP.values()
                }
            for data_key in self._get_data_keys()
            ]

        return permissions

    def _get_data_keys(self):
        return [u.get_attribute('data-key') for u in self.permission_records]

    def _get_permission_column_value(self, data_key, column_name):
        column_num = next((c_num for c_num, c_name in PERMISSION_COLUMNS_MAP.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'links':
            column_xpath = self.permission_column_links_xpath.format(data_key)
            links = Finds(by=By.XPATH, value=column_xpath, context=self)
            return [
                {
                    link.get_attribute('title').lower(): link.get_attribute('href')
                }
                for link in links
                ]

        else:
            column_xpath = self.permission_column_xpath.format(data_key, column_num)
            return Find(by=By.XPATH, value=column_xpath, context=self).text

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name)
        filter_element.clear()
        filter_element.send_keys(filter_value)
        filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
