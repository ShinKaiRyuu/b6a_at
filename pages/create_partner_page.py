from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webium import Find

from pages.base_page import BasePage
from helpers.files import get_full_path


class CreatePartnerPage(BasePage):
    url_path = '/admin/partner/update/'

    # inputs
    name = Find(value="input#partner-name")
    star_name = Find(value="input#partner-star_name")
    star_email = Find(value="#partner-star_email")
    logo_file = Find(value="input#partner-logofile")
    partner_status = Find(value="select#partner-status")
    # buttons
    update = Find(by=By.XPATH, value='//button[text()="Update"]')

    def create_new_partner(self, **kwargs):
        self.clear_send_keys('name', kwargs)
        self.clear_send_keys('star_name', kwargs)
        self.clear_send_keys('star_email', kwargs)
        self.logo_file.send_keys(get_full_path(kwargs['partner_logo']))
        partner_status_select = Select(self.partner_status)
        partner_status_select.select_by_visible_text(kwargs['partner_status'])
        self.update.click()
        self.wait_for_loading()
