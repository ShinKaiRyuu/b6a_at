import random
import time

from behave import *
from nose.tools import assert_equal, assert_true
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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


# TODO DESCRIPTION FIX
@step("I want to see  product details")
def step_impl(context):
    assert_equal(context.page.get_product_details(), context.product)
    if 'Update Products:' not in context.driver.title:
        context.product['id'] = context.page.id.text


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
    products = context.page.get_products()
    assert_true(len(products) >= 1)


# TODO make choise dismiss\accept
@then("I want to see dialog box and click (?P<dialogbox_answer>.+)")
def step_impl(context, dialogbox_answer):
    WebDriverWait(context.driver, 3).until(ec.alert_is_present())
    alert = context.driver.switch_to_alert()
    if dialogbox_answer == "No":
        alert.dismiss()
    elif dialogbox_answer == "Yes":
        alert.accept()


@when("I view random product")
def step_impl(context):
    product_number = random.randint(1, len(context.page.get_products()))
    context.product = context.page.view_product(context, product_number)


@when("I update random product")
def step_impl(context):
    product_number = random.randint(1, len(context.page.get_products()))
    context.product = context.page.update_product(context, product_number)
