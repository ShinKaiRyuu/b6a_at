from selenium.webdriver.common.by import By
from webium import Finds, Find

from pages.base_page import BasePage

PARTNER_COLUMNS_MAP = {
    '1': 'order',
    '2': 'id',
    '3': 'name',
    '4': 'star Name',
    '5': 'status Name',
    '6': 'links',
    '7': 'data_key'
}


class ManagePartnersPage(BasePage):
    url_path = 'admin/partner/index'

    # sorting
    order_link = Find(value='//a[text()="Order"]')
    id_link = Find(value='//a[text()="ID"]')
    name_link = Find(value='//a[text()="Name"]')
    star_name_link = Find(value='//a[text()="Star Name"]')

    # filters
    order_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[sort_order]"]')
    id_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[id]"]')
    name_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[name]"]')
    star_name_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[star_name]"]')
    status_filter = Find(by=By.XPATH, value='//select[@name="SearchPartner[status]"]')

    # buttons
    create_new_partner_btn = Find(by=By.XPATH, value='//a[@href="/admin/partner/create"]')

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
