from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

ITEMS_COLUMNS_MAP = {
    '1': 'place',
    '2': 'name',
    '3': 'average_Views',
    '4': 'total_opportunities',
    '5': 'vpm',
    '6': 'record_date',
    '7': 'created_by',
    '8': 'updated_By',
    '9': 'links_without_title',
    '10': 'data_key'
}


class UpdateInventorygroupsPage(BasePage, TableMixin):
    url_path = '/admin/groups/update/'

    name = Find(value="input#inventorygroup-name")
    content = Find(value="textarea#inventorygroup-content")
    partner_id = Find(value="select#inventorygroup-partner_id")
    # buttons
    create_btn = Find(by=By.XPATH, value='id("create_group")')

    update_btn = Find(by=By.XPATH, value='//button[text()="Update"]')
    html = Find(value=".re-html")

    item_form = Find(value='#w0')

    item_tab = Find(value='#groupTabs > li:nth-child(2) > a:nth-child(1)')
    create_item = Find(value="span#create_item")
    item_name = Find(value="input#item-name")
    item_vpm = Find(value="input#item-vpm")
    item_html = Find(by=By.XPATH, value='id("redactor-toolbar-1")/li[1]/a')
    item_content = Find(value="textarea#item-content")
    item_date = Find(by=By.XPATH, value='id("item-record_date")')
    next_month = Find(by=By.XPATH, value='//span[contains(text(),"Next")]')
    prev_month = Find(by=By.XPATH, value='//span[contains(text(),"Prev")]')
    item_update = Find(by=By.XPATH, value='(//button)[4]')

    def get_data(self):
        return self.get_table_records(ITEMS_COLUMNS_MAP)

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

    def fill_item_info(self, **item):
        self.item_tab.click()
        self.create_item.click()
        self.clear_send_keys('item_name', item)
        self.clear_send_keys('item_vpm', item)
        self.item_html.click()
        self.clear_send_keys('item_content', item)
        self._driver.execute_script("$('input').removeAttr('readonly')")
        self.clear_send_keys('item_date', item)
        self.item_update.click()
        self.item_tab.click()

    def view_item(self, item_id):
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'items/update/{}')]".format(item_id),
                           context=self)
        update_link.click()

    def wait_for_form_closed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(lambda x: (self.item_form.get_attribute("style") == 'display: none;') is True)
