from behave import *
from nose.tools import assert_true

use_step_matcher("re")


@step("I want to see all pages")
def step_impl(context):
    pages = context.page.get_pages()
    assert_true(len(pages) >= 1)
