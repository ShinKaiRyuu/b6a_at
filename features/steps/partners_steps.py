from behave import *
from nose.tools import assert_true, assert_equal
from helpers.data_helpers import create_partner_data

use_step_matcher("re")


@step("I want to see all partners")
def step_impl(context):
    partners = context.page.get_partners()
    assert_true(len(partners) >= 1)


@step("I want to see created partner in list")
def step_impl(context):
    context.page.filter_data('name_filter', context.partner_data['name'])
    partner = [partner for partner in context.page.get_partners() if partner['name'] == context.partner_data['name']]
    assert_equal(len(partner), 1)
    partner = partner[0]
    assert_equal(partner['partner_status'], context.partner_data['partner_status'])


@when("I create new partner")
def step_impl(context):
    partner = create_partner_data()
    context.page.create_new_partner(**partner)
    context.partner_data = partner
