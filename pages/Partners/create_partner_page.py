import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webium import Find

from pages.base_page import BasePage


class CreatePartnerPage(BasePage):
    url_path = '/admin/partner/update/'

    a_tag = "//div/ul/li/a[contains(.,'{link_text}')]"
    # inputs
    name = Find(value="input#partner-name")
    star_name = Find(value="input#partner-star_name")
    star_email = Find(value="#partner-star_email")
    logo_file = Find(value="input#partner-logofile")
    partner_status = Find(value="select#partner-status")
    # buttons
    update = Find(by=By.XPATH, value='//button[text()="Update"]')
    # links
    manage_partners_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Partners'))
    # alert
    succes_message = Find(by=By.XPATH, value='//div[@id="w2"]')

    def create_new_partner(self, **kwargs):
        self.clear_send_keys('name', kwargs)
        self.clear_send_keys('star_name', kwargs)
        self.clear_send_keys('star_email', kwargs)
        #        self.logo_file.send_keys(get_full_path(kwargs['partner_logo']))
        partner_status_select = Select(self.partner_status)
        partner_status_select.select_by_index(kwargs['status'])
        self.update.click()
        wait = WebDriverWait(self._driver, 30)
        wait.until(lambda x: 'Updated successfully.' in self.succes_message.text)
        self.wait_for_loading()

    def get_partner_details(self):
        kwargs = {}
        kwargs.update(name=self.name.get_attribute("value"))
        kwargs.update(star_name=self.star_name.get_attribute("value"))
        kwargs.update(star_email=self.star_email.get_attribute("value"))
        kwargs.update(status=int(self.partner_status.get_attribute("value")))
        return kwargs

    def update_partner_details(self, **partner):
        self.clear_send_keys('name', partner)
        self.clear_send_keys('star_name', partner)
        self.clear_send_keys('star_email', partner)
        if partner['status']:
            if self.partner_status.get_attribute('value') == 0:
                self.partner_status.click()
        elif partner['status'] == 0:
            if self.partner_status.get_attribute('value') == 1:
                self.partner_status.click()
        self.update.click()
        wait = WebDriverWait(self._driver, 30)
        wait.until(lambda x: 'Updated successfully.' in self.succes_message.text)
        self.wait_for_loading()
