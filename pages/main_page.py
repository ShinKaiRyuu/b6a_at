from selenium.webdriver.common.by import By
from webium import Find
from .base_page import BasePage


class MainPage(BasePage):

    url_path = '/'

    a_tag = "//a[contains(.,'{link_text}')]"
    manage_site_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Site'))
    manage_users_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Users'))
    manage_partners_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Partners'))
    manage_pages_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Pages'))
    manage_products_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Products'))
