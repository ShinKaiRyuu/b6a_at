from behave import *
from nose.tools import assert_in
from webium.driver import get_driver

from pages import (
    MainPage, LoginPage, ManageProductsPage, CreateProductPage, ViewProductPage, ManageUsersPage)

use_step_matcher("re")

PAGES_MAP = {
    'Main': MainPage,
    'Login': LoginPage,
    'Manage Products': ManageProductsPage,
    'Create Product': CreateProductPage,
    'View Product': ViewProductPage,
    'Manage Users': ManageUsersPage,
}


@when("I open (?P<page_name>.+) page")
@step("I am on (?P<page_name>.+) page")
def step_impl(context, page_name):
    context.page_name = page_name
    page = PAGES_MAP[page_name]
    context.page = page(url=''.join([context.app_url, page.url_path]))
    context.page.open()


@then("I want to see (?P<page_name>.+) page")
def step_impl(context, page_name):
    page = PAGES_MAP[page_name]
    assert_in(page.url_path, get_driver().current_url)
    context.page = page()
