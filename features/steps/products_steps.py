from behave import *
from nose.tools import assert_equal, assert_true, assert_in
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from features.steps.add_steps import save_item_id
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
    context.page.filter_data('title', context.product_data['title'])
    product = [product for product in context.page.get_data() if product['title'] == context.product_data['title']]
    assert_equal(len(product), 1)
    product = product[0]
    assert_equal(product['price'], float(context.product_data['price']))
    assert_equal(int(product['enabled'].replace('Enabled', '1').replace('Disabled', '2')),
                 context.product_data['enabled'])
    product_info = {}
    product_data_key = product['data_key']
    product_list = product['links'][0]['update product'].split('?id=')
    product_id = product_list[-1]
    product_info['id'] = product_id
    product_info['data_key'] = product_data_key
    save_item_id(product_info, 'products', context)
    #  context.product_data['createdby'] = product['createdby']
    context.product_data['updated'] = product['updated']


@step("I want to see all products")
def step_impl(context):
    products = context.page.get_data()
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
    context.page.delete_product(context.product_data['title'], context.product_info)


@then("I want to see product in list is (?P<status>.+)")
def step_impl(context, status):
    product = [product for product in context.page.get_data() if product['title'] == context.product_data['title']]
    assert_equal(len(product), 1)
    if status == 'not deleted':
        assert_equal(product[0]['price'], float(context.product_data['price']))


@then("I want to see product is (?P<status>.+)")
def step_impl(context, status):
    success_message = context.page.success_message.text
    if status == 'deleted':
        assert_in('Deleted successfully.', success_message)
    context.page.filter_data('title', context.product_data['title'])
    product = [product for product in context.page.get_data() if product['title'] == context.product_data['title']]
    context.page.replace_bad_elements('.close')
    if status == 'deleted':
        assert_equal(len(product), 0)


@when("I view product")
@when("I update product")
def step_impl(context):
    context.page.view_product(context.product_data['title'], context.product_info)


@then("I want to change title description price enabled")
def step_impl(context):
    product = create_product_data()
    context.page.update_product_details(**product)
    context.old_product_data = context.product_data
    context.product_data = product


@when("I open product")
def step_impl(context):
    context.page.open_product(context.product_data['title'])


@step("I want to see product elements")
def step_impl(context):
    assert_true(context.product_data['description'] in context.driver.page_source)
