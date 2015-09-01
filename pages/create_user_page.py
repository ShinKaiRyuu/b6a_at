from webium import Find

from pages.base_page import BasePage


class CreateUserPage(BasePage):
    url_path = '/user/admin/create'

    # inputs
    username = Find(value="input#user-username")
    email = Find(value="input#user-email")
    password = Find(value="input#user-password")

    # create button
    save = Find(value=".btn")

    def create_new_user(self, **kwargs):
        self.clear_send_keys('username', kwargs)
        self.clear_send_keys('email', kwargs)
        self.clear_send_keys('password', kwargs)
        self.save.click()
        self.wait_for_loading()
