import time

from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage


class UserInformationPage(BasePage):
    url_path = '/user/admin/info'

    # text_fields
    registration_time = Find(by=By.XPATH, value='//tr[1]/td[2]')
    registration_ip = Find(by=By.XPATH, value='//tr[2]/td[2]')
    confirmation_status = Find(by=By.XPATH, value='//tr[3]/td[2]')
    block_status = Find(by=By.XPATH, value='//tr[4]/td[2]')

    def view_user_information(self):
        user_data = {'registrationtime': time.strftime('%Y-%m-%dT%H:%M:%SZ',
                                                       time.strptime(self.registration_time.text, '%B %d, %Y %H:%M')),
                     'registration_ip': self.registration_ip.text,
                     'confirmation': self.confirmation_status.text, 'blockstatus': self.block_status.text, }
        return user_data
