from pages.base_page import BasePage
from webium import Find, Finds
from selenium.webdriver.common.by import By


class ManageProductsPage(BasePage):

    url_path = '/admin/goods/index'

    # sorting
    id_link = Find(value='a[data-sort*=id]')
    title_link = Find(value='a[data-sort*=title]')
    slug_link = Find(value='a[data-sort*=slug]')
    description_link = Find(value='a[data-sort*=description]')
    price_link = Find(value='a[data-sort*=price]')

    # buttons
    create_new_product_btn = Find(value='#main-container > div > div.col-xs-10 > div > p > a')

    #table
    table = Find(value='.table')
    view_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)')
    update_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(2)')
    delete_link = Find(value='.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(3)')

