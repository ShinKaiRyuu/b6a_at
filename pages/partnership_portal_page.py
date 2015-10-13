from selenium.webdriver.common.by import By
from webium import Find, Finds

from .base_page import BasePage


class PartnershipPortalPage(BasePage):
    url_path = '/portal'

    a_tag = "//a[contains(.,'{link_text}')]"
    manage_site_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Site'))
    manage_users_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Users'))
    manage_partners_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Partners'))
    manage_pages_link = Find(by=By.XPATH, value=a_tag.format(link_text='Pages'))
    manage_products_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Portal'))
    manage_scoreboard_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Scoreboard'))
    header_links = Finds(by=By.XPATH, value='//ul[@id="top-menu"]/li/a')

    def open_product(self, product_title):
        self._driver.execute_script("$('a[target=_blank]').removeAttr('target')")
        product_link = Find(by=By.XPATH, value='//a[text()="{}"]'.format(product_title), context=self)
        product_link.click()

