from selenium.webdriver.common.by import By
from webium import Finds, Find

from pages.base_page import BasePage

PRODUCT_COLUMNS_MAP = {
    '1': '#',
    '2': 'id',
    '3': 'title',
    '4': 'slug',
    '5': 'description',
    '6': 'price',
    '7': 'links',
    '8': 'data_key'
}


class ManageProductsPage(BasePage):
    url_path = '/admin/goods/index'

    # sorting
    id_link = Find(by=By.XPATH, value='//a[text()="ID"]')
    title_link = Find(by=By.XPATH, value='//a[text()="Title"]')
    slug_link = Find(by=By.XPATH, value='//a[text()="Slug"]')
    description_link = Find(by=By.XPATH, value='//a[text()="Description"]')
    price_link = Find(by=By.XPATH, value='//a[text()="Price"]')

    # buttons
    create_new_product_btn = Find(by=By.XPATH, value='//a[@href="/admin/goods/create"]')

    # table
    product_record_xpath = '//tr[@data-key]'
    product_column_xpath = '//tr[@data-key="{}"]/td[{}]'
    product_column_links_xpath = '//tr[@data-key="{}"]/td/a[@title]'
    product_records = Finds(by=By.XPATH, value=product_record_xpath)

    table = Find(value='.table')
    view_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)')
    update_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(2)')
    delete_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(3)')

    def get_products(self):
        products = [
            {
                column_name: self._get_product_column_value(data_key, column_name)
                for column_name in PRODUCT_COLUMNS_MAP.values()
                }
            for data_key in self._get_data_keys()
            ]
        return products

    def _get_data_keys(self):
        return [u.get_attribute('data-key') for u in self.product_records]

    def _get_product_column_value(self, data_key, column_name):
        column_num = next((c_num for c_num, c_name in PRODUCT_COLUMNS_MAP.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'links':
            column_xpath = self.product_column_links_xpath.format(data_key)
            links = Finds(by=By.XPATH, value=column_xpath, context=self)
            return [
                {
                    link.get_attribute('title').lower(): link.get_attribute('href')
                }
                for link in links
                ]

        else:
            column_xpath = self.product_column_xpath.format(data_key, column_num)
            return Find(by=By.XPATH, value=column_xpath, context=self).text
