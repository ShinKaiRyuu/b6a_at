from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

USER_COLUMNS_MAP = {
    '1': 'username',
    '2': 'email',
    '3': 'registrationtime',
    '4': 'confirmation',
    '5': 'block_status',
    '6': 'links',
    '7': 'data_key'
}


class ManageUsersPage(BasePage, TableMixin):
    url_path = '/user/admin/index'
    # sorting
    username_link = Find(by=By.XPATH, value='//a[contains(@data-sort,"username")]')
    email_link = Find(by=By.XPATH, value='//a[contains(@data-sort,"email")]')
    registrationtime_link = Find(by=By.XPATH, value='//a[contains(@data-sort,"created_at")]')
    description_link = Find(by=By.XPATH, value='//a[text()="Description"]')
    price_link = Find(by=By.XPATH, value='//a[text()="Price"]')

    # filters
    username_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[username]"]')
    email_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[email]"]')
    registrationtime_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[created_at]"]')

    # date picker
    active_date_in_date_picker = Find(value='.ui-state-active')

    # links
    create_link = Find(by=By.XPATH, value='//a[contains(text(),"Create")]')
    create_user_link = Find(by=By.XPATH, value='//a[@href="/user/admin/create"]')
    block_user_link = Find(by=By.XPATH, value='//a[text()="Block"]')
    unblock_user_link = Find(by=By.XPATH, value='//a[text()="Unblock"]')
    roles_link = Find(by=By.XPATH, value='//a[@href="/rbac/role/index"]')
    permissions_link = Find(by=By.XPATH, value='//a[@href="/rbac/permission/index"]')

    # TODO change selector
    success_message = Find(value='#w4')

    def get_data(self):
        return self.get_table_records(USER_COLUMNS_MAP)

    def delete_user(self, context):
        self.filter_data('username', context.user_data['username'])
        delete_link = Find(by=By.XPATH, value="//a[contains(@href,'delete/{}')]".format(context.user_id), context=self)
        delete_link.click()

    def block_user(self, context):
        self.filter_data('username', context.user_data['username'])
        block_link = Find(by=By.XPATH, value="//a[contains(@href,'block?id={}')]".format(context.user_id), context=self)
        block_link.click()

    def update_user(self, context):
        self.filter_data('username', context.user_data['username'])
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update/{}')]".format(context.user_id), context=self)
        update_link.click()

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name + '_filter')
        filter_element.clear()
        filter_element.send_keys(filter_value)
        if filter_name == 'registrationtime':
            self.active_date_in_date_picker.click()
        else:
            filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
