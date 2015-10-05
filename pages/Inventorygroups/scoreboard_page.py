from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import Find

from pages.base_page import BasePage
from pages.scoreboard_mixin import ScoreboardMixin

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


class ScoreboardPage(BasePage, ScoreboardMixin):
    url_path = '/scoreboard'

    parthner_select = Find(value='#scoreboard-partner')

    def open_items_page(self, inventorygroup_data):
        status_select = Select(self.parthner_select)
        status_select.select_by_value(inventorygroup_data['partner_id'])

    def get_data(self):
        return self.get_table_records(ITEMS_COLUMNS_MAP)
