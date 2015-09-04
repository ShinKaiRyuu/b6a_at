from pages.base_page import BasePage
from pages.table_mixin import TableMixin

PAGES_COLUMNS_MAP = {
    '1': 'order',
    '2': 'name',
    '3': 'created_by',
    '4': 'updated_by',
    '5': 'status',
    '6': 'links',
    '7': 'data_key'
}


class ManagePagesPage(BasePage, TableMixin):
    url_path = '/admin/page/index'

    def get_pages(self):
        return self.get_table_records(PAGES_COLUMNS_MAP)
