from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage


class CreateUserPage(BasePage):
    url_path = '/user/admin/create'

    # inputs
    username = Find(value="input#user-username")
    email = Find(value="input#user-email")
    password = Find(value="input#user-password")

    # create button
    save = Find(by=By.XPATH, value="//button[contains(text(),'Save')]")

    def create_new_user(self, **user):
        self.clear_send_keys('username', user)
        self.clear_send_keys('email', user)
        self.clear_send_keys('password', user)
        self.save.click()
        self.wait_for_loading()
