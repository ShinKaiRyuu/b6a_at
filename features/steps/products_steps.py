import random

from behave import *
from nose.tools import assert_equal, assert_true, assert_in
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from helpers.data_helpers import create_product_data

use_step_matcher("re")


@when(
    "I create new product")
def step_impl(context):
    product = create_product_data()
    context.page.create_new_product(**product)
    context.product_data = product


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


@when("I delete created product")
def step_impl(context):
    context.page.delete_product(context)


@then("I want to see product in list is (?P<status>.+)")
def step_impl(context, status):
    product = [product for product in context.page.get_products() if product['title'] == context.product_data['title']]
    assert_equal(len(product), 1)
    if status == 'not deleted':
        assert_equal(product[0]['price'], context.product_data['price'])


@then("I want to see product is (?P<status>.+)")
def step_impl(context, status):
    context.page.filter_data('title_filter', context.product_data['title'])
    product = [product for product in context.page.get_products() if product['title'] == context.product_data['title']]
    context.page.replace_bad_elements('.close')
    success_message = context.page.success_message.text
    if status == 'deleted':
        assert_equal(len(product), 0)
        assert_in('Deleted successfully.', success_message)
