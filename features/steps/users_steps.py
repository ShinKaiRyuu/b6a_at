from behave import *
from nose.tools import assert_true

use_step_matcher("re")


@step("I want to see all users")
def step_impl(context):
    users = context.page.get_users()
    assert_true(len(users) >= 1)
