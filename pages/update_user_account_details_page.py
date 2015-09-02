from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage


class UpdateUserAccountDetailsPage(BasePage):
    url_path = '/user/admin/update'

    # inputs
    username = Find(value="input#user-username")
    email = Find(value="input#user-email")
    password = Find(value="input#user-password")

    # links
    account_details_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/update/")]')
    profile_details_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/update-profile?id=")]')
    information_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/info?id=")]')
    assignments_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/assignments?id=")]')
    block_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/block?id=")]')
    delete_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/delete/")]')

    # create button
    update = Find(by=By.XPATH, value="//button[contains(text(),'Update')]")

    def view_user_account_details(self, user_data=None):
        user_data['username'] = self.username.get_attribute("value")
        user_data['email'] = self.email.get_attribute("value")
        return user_data

    def update_user_account_details(self, **user):
        self.clear_send_keys('username', user)
        self.clear_send_keys('email', user)
        self.clear_send_keys('password', user)
        self.update.click()
        self.wait_for_loading()
