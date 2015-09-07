from behave import *
from nose.tools import assert_true, assert_equal, assert_in

from helpers.data_helpers import create_partner_data

use_step_matcher("re")


@step("I want to see all partners")
def step_impl(context):
    partners = context.page.get_data()
    assert_true(len(partners) >= 1)


@step("I want to see created partner in list")
@step("I want to see updated partner in list")
def step_impl(context):
    context.page.filter_data('name', context.partner_data['name'])
    partner = [partner for partner in context.page.get_data() if partner['name'] == context.partner_data['name']]
    assert_equal(len(partner), 1)
    partner = partner[0]
    assert_equal(int(partner['status'].replace('Enabled', '1').replace('Disabled', '0')),
                 context.partner_data['status'])


@when("I create new partner")
def step_impl(context):
    partner = create_partner_data()
    context.page.create_new_partner(**partner)
    context.partner_data = partner


@when("I delete created partner")
def step_impl(context):
    context.page.delete_partner(context.partner_data['name'], context.partner_id)


@then("I want to see partner in list is (?P<status>.+)")
def step_impl(context, status):
    partner = [partner for partner in context.page.get_data() if partner['name'] == context.partner_data['name']]
    assert_equal(len(partner), 1)
    partner = partner[0]
    if status == 'not deleted':
        assert_equal(int(partner['status'].replace('Enabled', '1').replace('Disabled', '0')),
                     context.partner_data['status'])


@then("I want to see partner is (?P<status>.+)")
def step_impl(context, status):
    context.page.filter_data('name', context.partner_data['name'])
    partner = [partner for partner in context.page.get_data() if partner['title'] == context.product_data['title']]
    context.page.replace_bad_elements('.close')
    success_message = context.page.success_message.text
    if status == 'deleted':
        assert_equal(len(partner), 0)
        assert_in('Deleted successfully.', success_message)


@when("I view partner")
@when("I update partner")
def step_impl(context):
    context.page.view_partner(context.partner_data, context.partner_id)


@step("I want to see partner details")
def step_impl(context):
    actual_partner_data = context.page.get_partner_details()
    assert_equal(actual_partner_data, context.partner_data)


@then("I want to change name starname staremail status")
def step_impl(context):
    partner = create_partner_data()
    context.page.update_partner_details(**partner)
    context.old_partner_data = context.partner_data
    context.partner_data = partner


