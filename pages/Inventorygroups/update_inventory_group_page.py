from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage


class UpdateInventorygroupsPage(BasePage, ):
    url_path = '/admin/groups/update/'

    name = Find(value="input#inventorygroup-name")
    content = Find(value="textarea#inventorygroup-content")
    partner_id = Find(value="select#inventorygroup-partner_id")
    # buttons
    create_btn = Find(by=By.XPATH, value='id("create_group")')
    update_btn = Find(by=By.XPATH, value='//button[text()="Update"]')
    html = Find(value=".re-html")

    def get_inventory_group_details(self):
        kwargs = {}
        kwargs.update(name=self.name.get_attribute("value"))
        kwargs.update(content=self.content.get_attribute("value"))
        return kwargs

    def update_inventory_group_details(self, **inventory_group):
        self.clear_send_keys('name', inventory_group)
        self.html.click()
        self.clear_send_keys('content', inventory_group)
        self.update_btn.click()
        self.wait_for_loading()

