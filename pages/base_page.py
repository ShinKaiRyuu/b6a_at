from selenium.webdriver.support.wait import WebDriverWait
from webium import BasePage as WebiumBasePage, Find


class BasePage(WebiumBasePage):

    url_path = None

    login_link = Find(value='a[href*=login]')
    logout_css = 'a[href*=logout]'
    logout_link = Find(value=logout_css)

    def clear_send_keys(self, element_name, kwargs):
        value = kwargs.get(element_name)
        element = getattr(self, element_name)
        element.clear()
        element.send_keys(value)

    def get_login_status(self):
        return 'logged in' if self._driver.execute_script(
            "return $('{}').length".format(self.logout_css)) == 1 else 'logged out'

    def wait_for_loading(self, seconds=180):
        wait = WebDriverWait(self._driver, seconds)
        wait.until(lambda x: self._driver.execute_script('return jQuery.active == 0') is True)
