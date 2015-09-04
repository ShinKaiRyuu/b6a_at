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

@step("I want to see product details")
def step_impl(context):
    assert_equal(context.page.get_product_details(), context.product_data)


@then("I want to see created product in list")
@then("I want to see updated product in list")
def step_impl(context):
    context.page.filter_data('title_filter', context.product_data['title'])
    product = [product for product in context.page.get_products() if product['title'] == context.product_data['title']]
    assert_equal(len(product), 1)
    product = product[0]
    assert_equal(product['price'], context.product_data['price'])
    assert_equal(int(product['enabled'].replace('Enabled', '1').replace('Disabled', '2')),
                 context.product_data['enabled'])
    context.product_data['created_by'] = product['created_by']
    context.product_data['updated_by'] = product['updated_by']


@step("I want to see all products")
def step_impl(context):
    products = context.page.get_products()
    assert_true(len(products) >= 1)

@then("I want to see dialog box and click (?P<dialogbox_answer>.+)")
def step_impl(context, dialogbox_answer):
    WebDriverWait(context.driver, 3).until(ec.alert_is_present())
    alert = context.driver.switch_to_alert()
    if dialogbox_answer == "No":
        alert.dismiss()
    elif dialogbox_answer == "Yes":
        alert.accept()


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


@when("I view product")
@when("I update product")
def step_impl(context):
    context.page.view_product(context)


@then("I want to change title description price enabled")
def step_impl(context):
    product = create_product_data()
    context.page.update_product_details(**product)
    context.old_product_data = context.product_data
    context.product_data = product


@then("I want to see filtered products")
def step_impl(context):
    filter_name = context.filter_name.replace('_filter', '').replace('_at', '_time')
    products = context.page.get_products()
    for product in products:
        assert_in(context.filter_text.lower(), product[filter_name].lower())
