from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

PARTNER_COLUMNS_MAP = {
    '1': 'order',
    '2': 'name',
    '3': 'createdby',
    '4': 'updatedby',
    '5': 'status',
    '6': 'links',
    '7': 'data_key'
}


class ManagePartnersPage(BasePage, TableMixin):
    url_path = '/admin/partner/index'
    # sorting
    order_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"sort_order")]')
    name_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"name")]')
    createdby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_created_id")]')
    updatedby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_updated_id")]')

    # filters
    order_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[sort_order]"]')
    name_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[name]"]')
    createdby_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[user_created_id]"]')
    updatedby_filter = Find(by=By.XPATH, value='//input[@name="SearchPartner[user_updated_id]"]')
    status_filter = Find(by=By.XPATH, value='//select[@name="SearchPartner[status]"]')

    # buttons
    create_partner_btn = Find(by=By.XPATH, value='//a[@href="/admin/partner/create"]')

    success_message = Find(value='#w0')

    def get_data(self):
        return self.get_table_records(PARTNER_COLUMNS_MAP)

    def delete_partner(self, name, id):
        self.filter_data('name', name)
        delete_link = Find(by=By.XPATH, value="//a[contains(@href,'delete/{}')]".format(id),
                           context=self)
        delete_link.click()

    def view_partner(self, product_data, product_id):
        self.filter_data('name', product_data['name'])
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update/{}')]".format(product_id),
                           context=self)
        update_link.click()

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name + '_filter')
        if filter_name == 'status':
            self.status_filter.click()
            value = Find(by=By.XPATH, value='//option[text()="{}"]'.format(filter_value), context=self)
            value.click()
            self.status_filter.send_keys(keys.Keys.RETURN)
        else:
            filter_element.clear()
            filter_element.send_keys(filter_value)
            filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
