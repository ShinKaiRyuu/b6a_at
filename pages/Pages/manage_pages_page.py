from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webium import Find, Finds

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

PAGES_COLUMNS_MAP = {
    '1': 'order',
    '2': 'name',
    # '3': 'createdby',
    '3': 'updated',
    '4': 'status',
    '5': 'links',
    '6': 'data_key'
}


class ManagePagesPage(BasePage, TableMixin):
    url_path = '/admin/page/index'
    # sorting
    order_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"sort_order")]')
    name_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"name")]')
    createdby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_created_id")]')
    updatedby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_updated_id")]')

    # filters
    order_filter = Find(by=By.XPATH, value='//input[@name="SearchPage[sort_order]"]')
    name_filter = Find(by=By.XPATH, value='//input[@name="SearchPage[name]"]')
    createdby_filter = Find(by=By.XPATH, value='//input[@name="SearchPage[user_created_id]"]')
    updatedby_filter = Find(by=By.XPATH, value='//input[@name="SearchPage[user_updated_id]"]')
    status_filter = Find(by=By.XPATH, value='//select[@name="SearchPage[status]"]')

    # buttons
    create_page_btn = Find(by=By.XPATH, value='//a[@href="/admin/page/create"]')

    # links
    public_pages_link = Find(by=By.XPATH, value='id("top-menu-manager")/a')
    link_list = Find(value="#w2")
    links = Finds(by=By.XPATH, value='//ul[@id="w2"]/li/a')
    links2 = Finds(by=By.XPATH, value='//ul[@id="w3"]/li/a')
    link_to_page = Find(by=By.XPATH, value='//a[contains(@href,"/site/page?slug=")]')

    def get_data(self):
        return self.get_table_records(PAGES_COLUMNS_MAP)

    def get_links(self):
        return self.links

    def get_links2(self):
        return self.links2

    def get_link(self, link_text):
        link = Find(by=By.XPATH, value='//ul[@id="w2"]/li/a[contains(text(),"{}")]'.format(link_text), context=self)
        return link

    def get_link2(self, link_text):
        link = Find(by=By.XPATH, value='//ul[@id="w1"]/li/a[contains(text(),"{}")]'.format(link_text), context=self)
        return link

    def view_page(self, page_data, page_info):
        self.filter_data('name', page_data['name'])
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update?id={}')]".format(page_info['id']),
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

    def dragndrop_page(self, page_data):
        self.filter_data('name', page_data['name'])
        page = self.get_data()
        page = page[0]
        self.filter_data('name', ' ')
        source_element = Find(by=By.XPATH, value='//tr[@data-key="{}"]'.format(page['data_key']), context=self)
        dest_element = Find(by=By.XPATH, value='id("pages-grid")/table/tbody/tr[1]', context=self)
        ActionChains(self._driver).drag_and_drop(source_element, dest_element).perform()
        self.wait_for_loading()

    def open_page(self, text):
        self._driver.execute_script("$('a[target=_blank]').removeAttr('target')")
        link = Find(by=By.XPATH, value='//td/a[@href="/page/0/{}"]'.format(text), context=self)
        link.click()
