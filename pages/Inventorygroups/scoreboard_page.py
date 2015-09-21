from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin


class ScoreboardPage(BasePage, TableMixin):
    url_path = '/score-board'

    def open_items_page(self, inventorygroup_data):
        xpath = '//a[@href="/group/{}/items"]'.format(inventorygroup_data['slug'])
        link = Find(by=By.XPATH, value=xpath, context=self)
        link.click()
