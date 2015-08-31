from behave import *
from nose.tools import assert_equal, assert_in, assert_true
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

from helpers.data_helpers import make_ordered_dict

use_step_matcher("re")


@when(
    "I create new product with (?P<title>.+), (?P<slug>.+), (?P<description>.+), "
    "(?P<price>.+), (?P<enabled>.+)")
def step_impl(context, title, slug, description, price, enabled):
    keys = ['title', 'slug', 'description', 'price']
    kwargs = make_ordered_dict(keys, locals())
    context.page.create_new_product(enabled, **kwargs)
    context.product = kwargs
    if enabled:
        context.product['enabled'] = '1'
    if not enabled:
        context.product['enabled'] = '0'


@step("I want to see  product details with new data")
def step_impl(context):
    assert_equal(context.page.get_product_details(), context.product)
    context.product[id] = context.page.id.text


@then("I want to see created product in list")
def step_impl(context):
    result = 0
    for product in context.page.get_products():
        if product['title'] == context.product['title']:
            assert_equal(product['title'], context.product['title'])
            assert_equal(product['slug'], context.product['slug'])
            assert_equal(product['description'], context.product['description'])
            assert_equal(product['price'], context.product['price'])
            result = 1
    assert_equal(result, 1)


@step("I want to see all products")
def step_impl(context):
    products = context.page.get_products
    assert_true(len(products) >= 1)


# TODO make choise dismiss\accept
@then("I want to see dialog box")
def step_impl(context):
    WebDriverWait(context.driver, 3).until(ec.alert_is_present())
    time.sleep(2)
    alert = context.driver.switch_to_alert()
    alert.dismiss()
