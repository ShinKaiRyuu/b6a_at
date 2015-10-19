from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import Find

from pages.base_page import BasePage
from pages.scoreboard_mixin import ScoreboardMixin
from pages.inventory_mixin import InventoryMixin

ITEMS_COLUMNS_MAP = {
    '1': 'inventory_title',
    '2': 'inventory_item_views',
    '3': 'opportunity_activation',
    '4': 'impressions_total',
    '5': 'vpm_total',
    '6': 'value_total',
    '7': 'view_item',
    '8': 'data_key'
}

ITEMS_DETAILS_MAP = {
    '1': 'activation_element_title',
    '2': 'inventory_item_views',
    '3': 'opportunity_activation',
    '4': 'impressions_total',
}


class ScoreboardPage(BasePage, ScoreboardMixin, InventoryMixin):
    url_path = '/scoreboard'

    parthner_select = Find(value='#scoreboard-partner')

    def open_items_page(self, inventorygroup_data):
        status_select = Select(self.parthner_select)
        status_select.select_by_value(inventorygroup_data['partner_id'])

    def get_data(self):
        return self.get_table_records(ITEMS_COLUMNS_MAP)

    def open_name_link(self, name):
        link = Find(by=By.XPATH, value='//a[contains(text(),"{}")]'.format(name), context=self)
        link.click()

    def open_view_link(self, slug):
        link = Find(by=By.XPATH, value='//a[@href="/group/{}"]'.format(slug), context=self)
        link.click()

    def close_modal_window(self):
        link = Find(by=By.XPATH, value='//button[@class="close"]', context=self)
        link.click()

    def get_item_data(self):
        return self.get_table_records_for_item(ITEMS_DETAILS_MAP)

