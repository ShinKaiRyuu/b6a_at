import datetime

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

    item_tab = Find(value='#groupTabs > li:nth-child(2) > a:nth-child(1)')
    create_item = Find(value="span#create_item")
    item_name = Find(value="input#item-name")
    item_vpm = Find(value="input#item-vpm")
    item_html = Find(by=By.XPATH, value='id("redactor-toolbar-1")/li[1]/a')
    item_content = Find(value="textarea#item-content")
    item_date = Find(by=By.XPATH, value='id("item-record_date")')
    next_month = Find(by=By.XPATH, value='//span[contains(text(),"Next")]')
    prev_month = Find(by=By.XPATH, value='//span[contains(text(),"Prev")]')

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
        date = item['item_date'].split('-')
        self.set_item_time(date[1], date[0])

    def set_item_time(self, day, month):
        self.item_date.click()
        self.item_date.click()
        self.item_date.click()
        self.item_date.click()
        now = datetime.datetime.now()
        difference = now.month - month
        if difference < 0:
            for x in range(0, difference):
                self.next_month.click()
        elif difference > 0:
            for x in range(0, difference):
                self.prev_month.click()
        item_day = Find(by=By.XPATH, value='//td/a[@href="/page/{}"]'.format(text), context=self)
