from behave import *
from nose.tools import assert_equal, assert_in, assert_true
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


@step("I want to see  product details with (?P<title>.+), (?P<slug>.+), (?P<description>.+), "
      "(?P<price>.+), (?P<enabled>.+)")
def step_impl(context, title, slug, description, price, enabled):
    keys = ['title', 'slug', 'description', 'price', 'enabled']
    kwargs = make_ordered_dict(keys, locals())
    # TODO change asserting (format text)
    assert_equal(context.page.get_product_details(), kwargs)


@then("I want to see product with (?P<title>.+) in list")
def step_impl(context, title):
    title = title
    table_text = context.page.table.text
    assert_in(title, table_text)


@step("I want to see all products")
def step_impl(context):
    products = context.page.get_products()
    assert_true(len(products) >= 1)


@then("I want to see dialog box")
def step_impl(context):
    WebDriverWait(context.driver , 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
    time.sleep(2)
    alert = context.driver.switch_to_alert()
    alert.dismiss()
