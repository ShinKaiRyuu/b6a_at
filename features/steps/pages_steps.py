from behave import *
from nose.tools import assert_true, assert_equal

use_step_matcher("re")


@step("I want to see table with all pages")
def step_impl(context):
    pages = context.page.get_data()
    assert_true(len(pages) >= 1)

