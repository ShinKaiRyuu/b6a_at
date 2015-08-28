from selenium.webdriver.common.by import By
from webium import Find
from .base_page import BasePage


class MainPage(BasePage):

    url_path = '/'

    a_tag_with_text_xpath = "//a[contains(.,'{link_text}')]"
    manage_site_link = Find(by=By.XPATH, value=a_tag_with_text_xpath.format(link_text='Manage Site'))
    manage_users_link = Find(by=By.XPATH, value=a_tag_with_text_xpath.format(link_text='Manage Users'))
