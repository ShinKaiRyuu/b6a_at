from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

PRODUCT_COLUMNS_MAP = {
    '1': 'order',
    '2': 'title',
    '3': 'price',
    '4': 'createdby',
    '5': 'updatedby',
    '6': 'enabled',
    '7': 'links',
    '8': 'data_key'
}


class ManageProductsPage(BasePage, TableMixin):
    url_path = '/admin/goods/index'

    # region page elements
    # region sorting
    order_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"sort_order")]')
    title_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"title")]')
    price_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"price")]')
    createdby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_created_id")]')
    updatedby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_updated_id")]')
    enabled_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"enabled")]')
    # endregion

    # region filters
    order_filter = Find(by=By.XPATH, value='//input[@name="GoodsSearch[sort_order]"]')
    title_filter = Find(by=By.XPATH, value='//input[@name="GoodsSearch[title]"]')
    price_filter = Find(by=By.XPATH, value='//input[@name="GoodsSearch[price]"]')
    createdby_filter = Find(by=By.XPATH, value='//input[@name="GoodsSearch[user_created_id]"]')
    updatedby_filter = Find(by=By.XPATH, value='//input[@name="GoodsSearch[user_updated_id]"]')
    enabled_filter = Find(by=By.XPATH, value='//select[@name="GoodsSearch[enabled]"]')
    # endregion

    # region buttons
    create_new_product_btn = Find(by=By.XPATH, value='//a[@href="/admin/goods/create"]')
    # endregion

    # region work with table
    table = Find(value='.table')
    view_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)')
    update_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(2)')
    delete_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(3)')
    # endregion

    # region success message
    success_message = Find(value='#w0')
    # endregion
    # endregion

    def get_data(self):
        return self.get_table_records(PRODUCT_COLUMNS_MAP)

    def delete_product(self, product_title, product_info):
        self.filter_data('title', product_title)
        delete_link = Find(by=By.XPATH, value="//a[contains(@href,'delete/{}')]".format(product_info['id']),
                           context=self)
        delete_link.click()

    def view_product(self, product_title, product_info):
        self.filter_data('title', product_title)
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update/{}')]".format(product_info['id']),
                           context=self)
        update_link.click()

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name + '_filter')
        if filter_name == 'enabled':
            self.enabled_filter.click()
            value = Find(by=By.XPATH, value='//option[text()="{}"]'.format(filter_value), context=self)
            value.click()
            self.enabled_filter.send_keys(keys.Keys.RETURN)
        else:
            filter_element.clear()
            filter_element.send_keys(filter_value)
            filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
