from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By
from webium import Finds, Find

from pages.base_page import BasePage

ROLE_COLUMNS_MAP = {
    '1': 'name',
    '2': 'description',
    '3': 'rule_name',
    '4': 'data_key'
}


class ManageRolesPage(BasePage):
    url_path = '/rbac/role/index'

    name_filter = Find(by=By.XPATH, value='//input[@name="Search[name]"]')
    description_filter = Find(by=By.XPATH, value='//input[@name="Search[description]"]')
    rule_name_filter = Find(by=By.XPATH, value='//input[@name="Search[rule_name]"]')

    role_record_xpath = '//tr[@data-key]'
    role_column_xpath = '//tr[@data-key="{}"]/td[{}]'
    role_column_links_xpath = '//tr[@data-key="{}"]/td/a[@title]'
    role_records = Finds(by=By.XPATH, value=role_record_xpath)

    def get_roles(self):
        roles = [
            {
                column_name: self._get_role_column_value(data_key, column_name)
                for column_name in ROLE_COLUMNS_MAP.values()
                }
            for data_key in self._get_data_keys()
            ]

        return roles

    def _get_data_keys(self):
        return [u.get_attribute('data-key') for u in self.role_records]

    def _get_role_column_value(self, data_key, column_name):
        column_num = next((c_num for c_num, c_name in ROLE_COLUMNS_MAP.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'links':
            column_xpath = self.role_column_links_xpath.format(data_key)
            links = Finds(by=By.XPATH, value=column_xpath, context=self)
            return [
                {
                    link.get_attribute('title').lower(): link.get_attribute('href')
                }
                for link in links
                ]

        else:
            column_xpath = self.role_column_xpath.format(data_key, column_num)
            return Find(by=By.XPATH, value=column_xpath, context=self).text

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name)
        filter_element.clear()
        filter_element.send_keys(filter_value)
        filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
