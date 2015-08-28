from behave import *
from nose.tools import assert_equal, assert_in, assert_true

from helpers.data_helpers import make_ordered_dict

use_step_matcher("re")


@step("I want to see all partners")
def step_impl(context):
    partners = context.page.get_partners()
    assert_true(len(partners) >= 1)
