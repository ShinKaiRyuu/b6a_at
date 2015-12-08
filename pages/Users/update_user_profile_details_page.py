from selenium.webdriver.common.by import By
from webium import Find
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class UpdateUserProfileDetailsPage(BasePage):
    url_path = '/user/admin/update'

    # inputs
    name = Find(value="input#profile-name")
    public_email = Find(value="input#profile-public_email")
    location = Find(value="input#profile-location")
    bio = Find(value="textarea#profile-bio")
    partner = Find(value="select#profile-partner_id")

    # links
    account_details_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/update/")]')
    profile_details_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/update-profile?id=")]')
    information_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/info?id=")]')
    assignments_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/assignments?id=")]')
    block_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/block?id=")]')
    delete_link = Find(by=By.XPATH, value='//a[contains(@href,"/user/admin/delete/")]')

    # create button
    update = Find(by=By.XPATH, value="//button[contains(text(),'Update')]")

    def view_user_profile_details(self):
        user_data = {'name': self.name.get_attribute("value"),
                     # 'public_email': self.public_email.get_attribute("value"),
                     'location': self.location.get_attribute("value"), 'bio': self.bio.get_attribute("value"),
                     'partner_id': self.partner.get_attribute("value")}
        return user_data

    def update_user_profile_details(self, **user):
        self.clear_send_keys('name', user)
        # self.clear_send_keys('public_email', user)
        self.clear_send_keys('location', user)
        self.clear_send_keys('bio', user)
        partner = Select(self.partner)
        partner.select_by_value(user['partner_id'])
        self.update.click()
        self.wait_for_loading()
