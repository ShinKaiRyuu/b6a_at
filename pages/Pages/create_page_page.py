from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webium import Find

from pages.base_page import BasePage


class CreatePagePage(BasePage):
    url_path = '/admin/page/update/'

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
        self.seourl.click()
        self.html.click()
        self.clear_send_keys('content', kwargs)
        status_select = Select(self.status)
        status_select.select_by_value(kwargs['status'])
        self.seo.click()
        self.clear_send_keys('title', kwargs)
        self.clear_send_keys('keywords', kwargs)
        self.clear_send_keys('description', kwargs)
        self.main.click()
        self.update.click()
        wait = WebDriverWait(self._driver, 10)
        wait.until(lambda x: (self._driver.title == 'Pages') is True)
        self.wait_for_loading()
