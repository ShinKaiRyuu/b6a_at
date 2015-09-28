from pages.base_page import BasePage
from pages.scoreboard_mixin import ScoreboardMixin

ITEMS_COLUMNS_MAP = {
    '1': 'inventory_title',
    '2': 'inventory_item_views',
    '3': 'opportunity_activation',
    '4': 'impressions_total',
    '5': 'vpm_total',
    '6': 'value_total',
    '7': 'data_key'
}


class ScoreboardItemsPage(BasePage, ScoreboardMixin):
    url_path = '/items'

    def get_data(self):
        return self.get_table_records(ITEMS_COLUMNS_MAP)
