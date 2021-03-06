from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

INVENTORYGROUPS_COLUMNS_MAP = {
    '1': 'place',
    '2': 'name',
    '3': 'partner',
    # '4': 'createdby',
    '4': 'updated',
    '5': 'links_without_title',
    '6': 'data_key'
}


class ManageInventorygroupsPage(BasePage, TableMixin):
    url_path = '/admin/groups/index'
    # sorting
    id_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"id")]')
    name_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"name")]')
    partner_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"partner_id")]')
    createdby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_created_id")]')
    updatedby_sort = Find(by=By.XPATH, value='//a[contains(@data-sort,"user_updated_id")]')

    # inputs
    name = Find(value="input#inventorygroup-name")
    content = Find(value="textarea#inventorygroup-content")
    partner_id = Find(value="select#inventorygroup-partner_id")
    # buttons
    create_btn = Find(by=By.XPATH, value='id("create_group")')
    update_btn = Find(by=By.XPATH, value='//button[text()="Update"]')
    html = Find(value=".re-html")
    success_message = Find(value='#w0')

    scoreboard_link = Find(by=By.XPATH, value='//ul[contains(@id,"top-menu")]/li/a[contains(text(),"Scoreboard")]')

    def get_data(self):
        return self.get_table_records(INVENTORYGROUPS_COLUMNS_MAP)

    def view_inventory_group(self, inventory_group_id):
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update?id={}')]".format(inventory_group_id),
                           context=self)
        update_link.click()

    def create_inventory_group(self, **inventory_group):
        self.clear_send_keys('name', inventory_group)
        self.html.click()
        self.clear_send_keys('content', inventory_group)
        self.update_btn.click()
        self.wait_for_loading()

    def open_inventory_group(self, inventorygroup_info):
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update?id={}')]".format(inventorygroup_info['id']),
                           context=self)
        update_link.click()

    def delete_inventory_group(self, inventorygroup_info):
        delete_link = Find(by=By.XPATH, value="//a[contains(@href,'delete?id={}')]".format(inventorygroup_info['id']),
                           context=self)
        delete_link.click()
