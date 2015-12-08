from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webium import Find

from pages.base_page import BasePage


class CreatePagePage(BasePage):
    url_path = '/admin/page/update'

    # inputs
    name = Find(value="input#page-name")
    seourl = Find(value='input#page-slug')
    parentid = Find(value='select#page-parent_id')
    content = Find(value='textarea#page-content')
    status = Find(value='select#page-status')

    title = Find(value="input#page-title")
    keywords = Find(value="input#page-keywords")
    description = Find(value="textarea#page-description")
    # tabs
    main = Find(by=By.XPATH, value='//a[contains(@href,"#pageTabs-tab0")]')
    seo = Find(by=By.XPATH, value='//a[contains(@href,"#pageTabs-tab1")]')
    info = Find(by=By.XPATH, value='//a[contains(@href,"#pageTabs-tab2")]')
    # buttons
    update = Find(by=By.XPATH, value='//button[text()="Update Page"]')
    html = Find(value='a.re-html')

    def create_new_page(self, **kwargs):
        self.clear_send_keys('name', kwargs)
        self.html.click()
        self.clear_send_keys('content', kwargs)
        status_select = Select(self.status)
        status_select.select_by_value(kwargs['status'])
        wait = WebDriverWait(self._driver, 25)
        wait.until(lambda x: (self.seourl.get_attribute("value") != '') is True)
        self.seo.click()
        self.clear_send_keys('title', kwargs)
        self.clear_send_keys('keywords', kwargs)
        self.clear_send_keys('description', kwargs)
        self.main.click()
        self.update.click()

    def get_page_details(self):
        kwargs = {}
        kwargs.update(name=self.name.get_attribute("value"))
        kwargs.update(slug=self.seourl.get_attribute("value"))
        kwargs.update(parent_id=self.parentid.get_attribute("value"))
        kwargs.update(status=self.status.get_attribute("value"))
        kwargs.update(content=self.content.get_attribute("value"))
        self.seo.click()
        kwargs.update(title=self.title.get_attribute("value"))
        kwargs.update(keywords=self.keywords.get_attribute("value"))
        kwargs.update(description=self.description.get_attribute("value"))
        self.main.click()
        return kwargs

    def update_page_details(self, **page):
        self.clear_send_keys('name', page)
        self.html.click()
        self.clear_send_keys('content', page)
        status_select = Select(self.status)
        status_select.select_by_value(page['status'])
        wait = WebDriverWait(self._driver, 25)
        wait.until(lambda x: (self.seourl.get_attribute("value") != '') is True)
        self.seo.click()
        self.clear_send_keys('title', page)
        self.clear_send_keys('keywords', page)
        self.clear_send_keys('description', page)
        self.main.click()
        self.update.click()
