from behave import *
from nose.tools import assert_equal, assert_in, assert_true

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


@given("I add one random product")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass