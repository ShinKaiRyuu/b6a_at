from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

PARTNER_COLUMNS_MAP = {
    '1': 'order',
    '2': 'name',
    '3': 'created_by',
    '4': 'updated_by',
    '5': 'status',
    '6': 'links',
    '7': 'data_key'
}


class ManagePartnersPage(BasePage, TableMixin):
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

    success_message = Find(value='#w0')

    def get_partners(self):
        return self.get_table_records(PARTNER_COLUMNS_MAP)

    def delete_partner(self, context):
        self.filter_data('name_filter', context.partner_data['name'])
        delete_link = Find(by=By.XPATH, value="//a[contains(@href,'delete/{}')]".format(context.partner_id),
                           context=self)
        delete_link.click()

    def filter_data(self, filter_name, filter_value):
        filter_element = getattr(self, filter_name)
        filter_element.clear()
        filter_element.send_keys(filter_value)
        filter_element.send_keys(keys.Keys.RETURN)
        self.wait_for_loading()
