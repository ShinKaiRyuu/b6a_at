from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import Find

from pages.base_page import BasePage


class CreateProductPage(BasePage):
    # url_path = '/admin/goods/create'
    url_path = 'admin/goods/update/'
    a_tag = "//div/ul/li/a[contains(.,'{link_text}')]"
    # inputs
    title = Find(value="input#goods-title")
    seourl = Find(value="input#goods-slug")
    description = Find(value="#goods-description")
    price = Find(value="input#goods-price")
    enabled = Find(value="input#goods-enabled")
    # buttons
    create = Find(by=By.XPATH, value='//button[text()="Create"]')
    update = Find(by=By.XPATH, value='//button[text()="Update"]')
    html = Find(value=".re-html")
    # links
    manage_products_link = Find(by=By.XPATH, value=a_tag.format(link_text='Manage Portal'))
    # alert
    succes_message = Find(by=By.XPATH, value='//div[@id="w3"]')

    def create_new_product(self, **kwargs):
        self.clear_send_keys('title', kwargs)
        self.html.click()
        self.clear_send_keys('description', kwargs)
        self.clear_send_keys('price', kwargs)
        if kwargs['enabled']:
            self.enabled.click()
        wait = WebDriverWait(self._driver, 25)
        wait.until(lambda x: (self.seourl.get_attribute("value") != '') is True)
        self.create.click()
        wait = WebDriverWait(self._driver, 30)
        wait.until(lambda x: 'Updated successfully.' in self.succes_message.text)
        self.wait_for_loading()

    def get_product_details(self):
        kwargs = {}
        kwargs.update(title=self.title.get_attribute("value"))
        kwargs.update(seourl=self.seourl.get_attribute("value"))
        kwargs.update(description=self.description.get_attribute("value"))
        kwargs.update(price=self.price.get_attribute("value"))
        kwargs.update(enabled=int(self.enabled.get_attribute("value")))
        return kwargs

    def update_product_details(self, **product):
        self.clear_send_keys('title', product)
        self.html.click()
        self.clear_send_keys('description', product)
        self.clear_send_keys('price', product)
        if product['enabled']:
            if self.enabled.get_attribute('value') == 0:
                self.enabled.click()
        elif product['enabled'] == 0:
            if self.enabled.get_attribute('value') == 1:
                self.enabled.click()
        wait = WebDriverWait(self._driver, 25)
        wait.until(lambda x: (self.seourl.get_attribute("value") != '') is True)
        self.update.click()
        wait = WebDriverWait(self._driver, 30)
        wait.until(lambda x: 'Updated successfully.' in self.succes_message.text)
        self.wait_for_loading()
