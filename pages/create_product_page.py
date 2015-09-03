from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage


class CreateProductPage(BasePage):
    # url_path = '/admin/goods/create'
    url_path = 'admin/goods/update/'

    # inputs
    title = Find(value="input#goods-title")
    # slug = Find(value="input#goods-slug")
    description = Find(value="#goods-description")
    price = Find(value="input#goods-price")
    enabled = Find(value="input#goods-enabled")
    # buttons
    update = Find(by=By.XPATH, value='//button[text()="Update"]')
    html = Find(value=".re-html")

    def create_new_product(self, **kwargs):
        self.clear_send_keys('title', kwargs)
        # self.clear_send_keys('slug', kwargs)
        self.html.click()
        self.clear_send_keys('description', kwargs)
        self.clear_send_keys('price', kwargs)
        if kwargs['enabled']:
            self.enabled.click()
        self.update.click()
        self.wait_for_loading()


def get_product_details(self):
    title = self.title.get_attribute("value")
    slug = self.slug.get_attribute("value")
    description = self.description.get_attribute("value")
    price = self.price.get_attribute("value")
    enabled = self.enabled.get_attribute("value")
    keys = ['title', 'slug', 'description', 'price', 'enabled']
    # kwargs = make_ordered_dict(keys, locals())
    kwargs = {k: locals().get(k) for k in keys}
    return kwargs
