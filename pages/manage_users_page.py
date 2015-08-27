from selenium.webdriver.common.by import By
from webium import Finds, Find

from .base_page import BasePage

USER_COLUMNS_MAP = {
    '1': 'username',
    '2': 'email',
    '3': 'registration_ip',
    '4': 'registration_time',
    '5': 'confirmation',
    '6': 'block_status',
    '7': 'links',
    '8': 'data_key'
}


class ManageUsersPage(BasePage):
    url_path = '/user/admin/index'

    user_record_xpath = '//tr[@data-key]'
    user_column_xpath = '//tr[@data-key="{}"]/td[{}]'
    user_column_links_xpath = '//tr[@data-key="{}"]/td/a[@title]'
    user_records = Finds(by=By.XPATH, value=user_record_xpath)

    def get_users(self):
        users = [
            {
                column_name: self._get_user_column_value(data_key, column_name)
                for column_name in USER_COLUMNS_MAP.values()
            }
            for data_key in self._get_data_keys()
        ]

        return users

    def _get_data_keys(self):
        return [u.get_attribute('data-key') for u in self.user_records]

    def _get_user_column_value(self, data_key, column_name):
        column_num = next((c_num for c_num, c_name in USER_COLUMNS_MAP.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'links':
            column_xpath = self.user_column_links_xpath.format(data_key)
            links = Finds(by=By.XPATH, value=column_xpath, context=self)
            return [
                {
                    link.get_attribute('title').lower(): link.get_attribute('href')
                }
                for link in links
            ]

        else:
            column_xpath = self.user_column_xpath.format(data_key, column_num)
            return Find(by=By.XPATH, value=column_xpath, context=self).text
