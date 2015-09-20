from behave import *
from nose.tools import assert_equal

from features.steps.add_steps import save_item_id
from helpers.data_helpers import create_inventory_group_data,create_item_data

use_step_matcher("re")


@step("fill form with inventory group data")
def step_impl(context):
    inventorygroup = create_inventory_group_data()
    context.page.create_inventory_group(**inventorygroup)
    context.inventory_group_data = inventorygroup


@step("I want to see new inventory group in list")
def step_impl(context):
    context.page.wait_for_loading()
    inventorygroup = [inventorygroup for inventorygroup in context.page.get_data() if
                      inventorygroup['name'].lower() == context.inventory_group_data['name'].lower()]
    assert_equal(len(inventorygroup), 1)
    inventorygroup = inventorygroup[0]
    inventorygroup_list = inventorygroup['links'][0]['update'].split('/')
    inventorygroup_id = inventorygroup_list[-1]
    inventorygroup_info = {'id': inventorygroup_id, 'data_key': inventorygroup['data_key']}
    save_item_id(inventorygroup_info, 'inventory_group', context)


@when("I view inventory group")
def step_impl(context):
    context.page.open_inventory_group(context.inventorygroup_info)


@step("I want to see inventory group details")
def step_impl(context):
    inventory_group_details = context.page.get_inventory_group_details()
    assert_equal(context.inventorygroup_data['name'], inventory_group_details['name'])
    assert_equal(context.inventorygroup_data['content'], inventory_group_details['content'])


@then("I want to change name content")
def step_impl(context):
    inventory_group = create_inventory_group_data()
    context.page.update_inventory_group_details(**inventory_group)
    context.old_inventorygroup_data = context.inventorygroup_data
    context.inventorygroup_data = inventory_group


@then("I want to see updated inventory group in list")
def step_impl(context):
    context.page.wait_for_loading()
    inventorygroup = [inventorygroup for inventorygroup in context.page.get_data() if
                      inventorygroup['name'].lower() == context.inventorygroup_data['name'].lower()]
    assert_equal(len(inventorygroup), 1)


@when("I delete created inventory group")
def step_impl(context):
    context.page.delete_inventory_group(context.inventorygroup_info)


@step("I want to see inventory group in list")
def step_impl(context):
    inventorygroup = [inventorygroup for inventorygroup in context.page.get_data() if
                      inventorygroup['name'].lower() == context.inventorygroup_data['name'].lower()]
    assert_equal(len(inventorygroup), 1)


@then("I want to see inventory group is deleted")
def step_impl(context):
    inventorygroup = [inventorygroup for inventorygroup in context.page.get_data() if
                      inventorygroup['name'].lower() == context.inventorygroup_data['name'].lower()]
    assert_equal(len(inventorygroup), 0)


@then("I add a new item")
def step_impl(context):
    item_info = create_item_data()
    context.page.fill_item_info(**item_info)
