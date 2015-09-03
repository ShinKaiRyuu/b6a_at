from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By
from webium import Finds, Find

from pages.base_page import BasePage

PARTNER_COLUMNS_MAP = {
    '1': 'order',
    '2': 'name',
    '3': 'created_by',
    '4': 'updated_by',
    '5': 'partner_status',
    '6': 'links',
    '7': 'data_key'
}


class ManagePartnersPage(BasePage):
    url_path = '/admin/partner/index'

    # sorting
    order_link = Find(by=By.XPATH, value='//a[text()="Order"]')
    id_link = Find(by=By.XPATH, value='//a[text()="ID"]')
    name_link = Find(by=By.XPATH, value='//a[text()="Name"]')
    star_name_link = Find(by=By.XPATH, value='//a[text()="Star Name"]')

    # filters
    order_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[sort_order]"]')
    name_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[name]"]')
    created_by_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[user_created_id]"]')
    updated_by_filter = Find(by=By.XPATH, value='SearchPartner[user_updated_id]')
    status_name_filter = Find(by=By.XPATH, value='//select[@name="SearchPartner[status]"]')

    # buttons
    create_partner_btn = Find(by=By.XPATH, value='//a[@href="/admin/partner/create"]')

    # table
    partner_record_xpath = '//tr[@data-key]'
    partner_column_xpath = '//tr[@data-key="{}"]/td[{}]'
    partner_column_links_xpath = '//tr[@data-key="{}"]/td/a[@title]'
    partner_records = Finds(by=By.XPATH, value=partner_record_xpath)

    def get_partners(self):
        partners = [
            {
                column_name: self._get_partner_column_value(data_key, column_name)
                for column_name in PARTNER_COLUMNS_MAP.values()
            }
            for data_key in self._get_data_keys()
        ]

        return partners

    def _get_data_keys(self):
        return [u.get_attribute('data-key') for u in self.partner_records]

    def _get_partner_column_value(self, data_key, column_name):
        column_num = next((c_num for c_num, c_name in PARTNER_COLUMNS_MAP.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'links':
            column_xpath = self.partner_column_links_xpath.format(data_key)
            links = Finds(by=By.XPATH, value=column_xpath, context=self)
            return [
                {
                    link.get_attribute('title').lower(): link.get_attribute('href')
                }
                for link in links
            ]

        else:
            column_xpath = self.partner_column_xpath.format(data_key, column_num)
            return Find(by=By.XPATH, value=column_xpath, context=self).text

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name)
        filter_element.clear()
        filter_element.send_keys(filter_value)
        filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
