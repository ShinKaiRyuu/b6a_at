from behave import *
from nose.tools import assert_equal, assert_in

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
    assert_equal(context.page.get_product_details
                 (context.page.title.text,
                  context.page.slug.text,
                  context.page.description.text,
                  context.page.price.text,
                  context.page.enabled.text)
                 ,
                 kwargs
                 )


@then("I want to see product with (?P<title>.+) in list")
def step_impl(context, title):
    title = title
    table_text = context.page.table.text
    assert_in(title, table_text)
