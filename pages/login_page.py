from webium import Find, Finds
from .base_page import BasePage


class LoginPage(BasePage):

    url_path = '/user/login'

    username = Find(value='#login-form-login')
    password = Find(value='#login-form-password')
    login_btn = Find(value='button[type=submit]')

    errors_css = '.help-block'

    def login_with(self, credentials):
        self.clear_send_keys('username', credentials)
        self.clear_send_keys('password', credentials)
        self.login_btn.click()
        self.wait_for_loading()

    def get_error_messages(self):
        errors = Finds(value=self.errors_css, context=self)
        return [e.text for e in errors if e.text]
