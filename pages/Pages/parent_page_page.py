from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin


class ParentPagePage(BasePage, TableMixin):
    url_path = '/page/'

    def open_additional_page(self, text):
        link = Find(by=By.XPATH, value='//a[contains(text(),"{}")]'.format(text), context=self)
        link.click()
