from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webium import Finds, Find

from helpers.data_helpers import make_ordered_dict
from pages.base_page import BasePage

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

    # filters
    username_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[username]"]')
    email_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[email]"]')
    registration_ip_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[registration_ip]"]')
    registration_at_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[created_at]"]')

    # date picker
    active_date_in_date_picker = Find(value='.ui-state-active')

    # links
    create_link = Find(by=By.XPATH, value='//a[contains(text(),"Create")]')
    create_user_link = Find(by=By.XPATH, value='//a[@href="/user/admin/create"]')

    user_record_xpath = '//tr[@data-key]'
    user_column_xpath = '//tr[@data-key="{}"]/td[{}]'
    user_column_links_xpath = '//tr[@data-key="{}"]/td/a[@title]'
    user_records = Finds(by=By.XPATH, value=user_record_xpath)
    # TODO change selector
    success_message = Find(value='#w4')

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

    def delete_user(self, context):
        for user in self.get_users():
            if user['data_key'] == str(context.user_id):
                username = user['username']
                email = user['email']
                registration_ip = user['registration_ip']
                registration_time = user['registration_time']
                confirmation = user['confirmation']
                # enabled = product['enabled']
                link = next(b['delete'] for b in user['links'] if 'delete' in b)
        link = link.replace(context.app_url, '')
        delete_link = Find(by=By.XPATH, value="//a[contains(@href,'{}')]".format(link), context=self)
        delete_link.click()
        keys = ['username', 'email', 'registration_ip', 'registration_time', 'confirmation']
        kwargs = make_ordered_dict(keys, locals())
        context.user = kwargs

    def filter_user(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name)
        filter_element.clear()
        filter_element.send_keys(filter_value)
        if filter_name == 'registration_at_filter':
            self.active_date_in_date_picker.click()
        self.wait_for_loading()
