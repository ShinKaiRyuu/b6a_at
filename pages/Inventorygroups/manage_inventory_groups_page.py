from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import Find


from pages.base_page import BasePage
from pages.table_mixin import TableMixin

INVENTORYGROUPS_COLUMNS_MAP = {
    '1': 'place',
    '2': 'id',
    '3': 'name',
    '4': 'partner',
    '5': 'createdby',
    '6': 'updatedby',
    '7': 'links',
    '8': 'data_key'
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
    create_inventorygroup_btn = Find(by=By.XPATH, value='id("create_group")')
    html = Find(value=".re-html")
    success_message = Find(value='#w0')

    def get_data(self):
        return self.get_table_records(INVENTORYGROUPS_COLUMNS_MAP)

    def delete_inventory_group(self, inventorygroup_id):
        delete_link = Find(by=By.XPATH, value="//a[contains(@href,'delete/{}')]".format(inventorygroup_id),
                           context=self)
        delete_link.click()

    def view_inventory_group(self,  inventorygroup_id):
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update/{}')]".format(inventorygroup_id),
                           context=self)
        update_link.click()

    def create_inventory_group(self, **inventory_group):
        self.create_inventorygroup_btn.click()
        self.name.clear_send_keys('name', inventory_group)
        partner = Select(self.partner_id)
        partner.select_by_value(inventory_group['partner_id'])
        self.html.click()
        self.content.clear_send_keys('content', inventory_group)



