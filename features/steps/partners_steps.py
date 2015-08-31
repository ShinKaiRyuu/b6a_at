from behave import *
from nose.tools import assert_true

use_step_matcher("re")


@step("I want to see all partners")
def step_impl(context):
    partners = context.page.get_partners()
    assert_true(len(partners) >= 1)
