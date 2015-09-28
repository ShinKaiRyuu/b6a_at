from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import Find

from pages.base_page import BasePage
from pages.table_mixin import TableMixin

OPPORTUNITIES_COLUMNS_MAP = {
    '1': 'place',
    '2': 'name',
    '3': 'views',
    '4': 'record_date',
    '5': 'created_by',
    '6': 'updated_By',
    '7': 'links',
    '8': 'data_key'
}


class UpdateItemsPage(BasePage, TableMixin):
    url_path = '/admin/items/update/'

    name = Find(value="input#item-name")
    vpm = Find(value="input#item-vpm")
    content = Find(value="textarea#item-content")
    record_date = Find(value="input#item-record_date")
    # buttons
    update_btn = Find(by=By.XPATH, value='//button[text()="Update"]')
    html = Find(value=".re-html")

    opportunity_form = Find(value='#w0')

    opportunity_tab = Find(value='#itemTabs > li:nth-child(2) > a:nth-child(1)')
    create_opportunity = Find(value="span#create_item")
    opportunity_name = Find(value="input#opportunity-name")
    opportunity_views = Find(value="input#opportunity-views")
    opportunity_vpm = Find(value="input#opportunity-vpm")
    opportunity_html = Find(by=By.XPATH, value='id("redactor-toolbar-1")/li[1]/a')
    opportunity_content = Find(value="textarea#opportunity-content")
    opportunity_date = Find(by=By.XPATH, value='id("opportunity-record_date")')
    next_month = Find(by=By.XPATH, value='//span[contains(text(),"Next")]')
    prev_month = Find(by=By.XPATH, value='//span[contains(text(),"Prev")]')
    opportunity_update = Find(by=By.XPATH, value='(//button)[4]')

    scoreboard_link = Find(by=By.XPATH, value='//ul[contains(@id,"top-menu")]/li/a[contains(text(),"Scoreboard")]')

    def get_data(self):
        return self.get_table_records(OPPORTUNITIES_COLUMNS_MAP)

    def get_item_details(self):
        kwargs = {}
        kwargs.update(name=self.name.get_attribute("value"))
        kwargs.update(content=self.content.get_attribute("value"))
        return kwargs

    def update_item_details(self, **inventory_group):
        self.clear_send_keys('name', inventory_group)
        self.html.click()
        self.clear_send_keys('content', inventory_group)
        self.update_btn.click()
        self.wait_for_loading()

    def fill_opportunity_info(self, **opportunity):
        self.opportunity_tab.click()
        self.create_opportunity.click()
        self.clear_send_keys('opportunity_name', opportunity)
        self.clear_send_keys('opportunity_views', opportunity)
        self._driver.execute_script("$('input').removeAttr('readonly')")
        self.clear_send_keys('opportunity_date', opportunity)
        self.opportunity_update.click()
        self.opportunity_tab.click()

    def view_opportunity(self, opportunity_id):
        update_link = Find(by=By.XPATH, value="//a[contains(@href,'update/{}')]".format(opportunity_id),
                           context=self)
        update_link.click()

    def wait_for_form_closed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(lambda x: (self.opportunity_form.get_attribute("style") == 'display: none;') is True)
