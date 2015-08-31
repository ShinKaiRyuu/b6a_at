import time

from webium import Find

from pages.base_page import BasePage


class CreateProductPage(BasePage):
    # url_path = '/admin/goods/create'
    url_path = 'admin/goods/update/5'

    # inputs
    title = Find(value="input#goods-title")
    slug = Find(value="input#goods-slug")
    description = Find(value="#goods-description")
    price = Find(value="input#goods-price")
    enabled = Find(value="input#goods-enabled")
    # buttons
    create = Find(value="button.btn-primary")
    html = Find(value=".re-html")

    def create_new_product(self, enabled, **kwargs):
        self.clear_send_keys('title', kwargs)
        self.clear_send_keys('slug', kwargs)
        self.html.click()
        self.clear_send_keys('description', kwargs)
        self.clear_send_keys('price', kwargs)
        if not enabled:
            self.enabled.click()
        self.create.click()
        time.sleep(5)
