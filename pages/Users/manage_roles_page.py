from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

ROLE_COLUMNS_MAP = {
    '1': 'name',
    '2': 'description',
    '3': 'rule_name',
    '4': 'data_key'
}


class ManageRolesPage(BasePage, TableMixin):
    url_path = '/rbac/role/index'

    name_filter = Find(by=By.XPATH, value='//input[@name="Search[name]"]')
    description_filter = Find(by=By.XPATH, value='//input[@name="Search[description]"]')
    rulename_filter = Find(by=By.XPATH, value='//input[@name="Search[rule_name]"]')

    def get_data(self):
        return self.get_table_records(ROLE_COLUMNS_MAP)

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name + '_filter')
        filter_element.clear()
        filter_element.send_keys(filter_value)
        filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
