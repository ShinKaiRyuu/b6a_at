from selenium.webdriver.common.by import By
from webium import Find
from pages.base_page import BasePage
from pages.table_mixin import TableMixin

PAGES_COLUMNS_MAP = {
    '1': 'order',
    '2': 'name',
    '3': 'createdby',
    '4': 'updatedby',
    '5': 'status',
    '6': 'links',
    '7': 'data_key'
}


class ManagePagesPage(BasePage, TableMixin):
    url_path = '/admin/page/index'
    # sorting
    order_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"sort_order")]')
    name_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"name")]')
    createdby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_created_id")]')
    updatedby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_updated_id")]')

    # filters
    username_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[username]"]')
    email_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[email]"]')
    registration_ip_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[registration_ip]"]')
    registration_at_filter = Find(by=By.XPATH, value='//input[@name="UserSearch[created_at]"]')

    def get_pages(self):
        return self.get_table_records(PAGES_COLUMNS_MAP)
