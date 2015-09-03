from behave import *
from nose.tools import assert_true, assert_equal, assert_in

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
    assert_equal(int(partner['status'].replace('Enabled', '1').replace('Disabled', '0')),
                 context.partner_data['status'])


@when("I create new partner")
def step_impl(context):
    partner = create_partner_data()
    context.page.create_new_partner(context, **partner)
    context.partner_data = partner


@when("I delete created partner")
def step_impl(context):
    context.page.delete_partner(context)


@then("I want to see partner in list is (?P<status>.+)")
def step_impl(context, status):
    partner = [partner for partner in context.page.get_partners() if partner['name'] == context.partner_data['name']]
    assert_equal(len(partner), 1)
    partner = partner[0]
    if status == 'not deleted':
        assert_equal(int(partner['status'].replace('Enabled', '1').replace('Disabled', '0')),
                     context.partner_data['status'])


@then("I want to see partner is (?P<status>.+)")
def step_impl(context, status):
    context.page.filter_data('name_filter', context.partner_data['name'])
    partner = [partner for partner in context.page.get_partners() if partner['title'] == context.product_data['title']]
    context.page.replace_bad_elements('.close')
    success_message = context.page.success_message.text
    if status == 'deleted':
        assert_equal(len(partner), 0)
        assert_in('Deleted successfully.', success_message)
