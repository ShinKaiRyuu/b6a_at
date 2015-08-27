from pages.base_page import BasePage
from webium import Find, Finds
from selenium.webdriver.common.by import By
from collections import OrderedDict
from helpers.data_helpers import make_ordered_dict, modify_value


class ViewProductPage(BasePage):
    # url_path = '/admin/goods/create'
    url_path = 'admin/goods/view/5'

    #links
    manage_products_menu_link = Find(value=".nav-pills > li:nth-child(4) > a:nth-child(1)")

    #table data
    title = Find(value=".table > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
    slug = Find(value=".table > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)")
    description = Find(value=".table > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)")
    price = Find(value=".table > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)")
    enabled = Find(value=".table > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2)")

    def get_product_details(self, title, slug, description, price, enabled):
        product_details = OrderedDict()
        keys = ['title', 'slug', 'description', 'price', 'enabled']
        kwargs = make_ordered_dict(keys, locals())
        return kwargs
