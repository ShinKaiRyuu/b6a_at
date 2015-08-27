from behave import *
from nose.tools import assert_true
from webium.driver import get_driver

from pages import (
    MainPage, LoginPage, ManageProductsPage, CreateProductPage,ViewProductPage)

use_step_matcher("re")

PAGES_MAP = {
    'Main': MainPage,
    'Login': LoginPage,
    'Manage Products': ManageProductsPage,
    'Create Product': CreateProductPage,
    'View Product': ViewProductPage
}


@when("I open (?P<page_name>.+) page")
@step("I am on (?P<page_name>.+) page")
def step_impl(context, page_name):
    context.page_name = page_name
    page = PAGES_MAP[page_name]
    context.page = page(url=''.join([context.app_url, page.url_path]))
    context.page.open()

    # success = None
    # while not success:
    #     try:
    #         context.page.open()
    #         success = True
    #     except TimeoutException:
    #         print('caught TimeoutException')
    #         close_driver()
    #         context.driver = get_updated_driver()


@then("I want to see (?P<page_name>.+) page")
def step_impl(context, page_name):
    page = PAGES_MAP[page_name]
    assert_true(get_driver().current_url.endswith(page.url_path),
                '{} not ends with {}'.format(get_driver().current_url, page.url_path))
    context.page = page()
