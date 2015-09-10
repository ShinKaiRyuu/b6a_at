from behave import *
from nose.tools import assert_equal

from features.steps.add_steps import save_item_id
from helpers.data_helpers import create_inventory_group_data

use_step_matcher("re")


@step("fill form with inventory group data")
def step_impl(context):
    inventorygroup = create_inventory_group_data()
    context.page.create_inventory_group(**inventorygroup)
    context.inventory_group_data = inventorygroup


@step("I want to see new inventory group in list")
def step_impl(context):
    inventorygroup = [inventorygroup for inventorygroup in context.page.get_data() if
                      inventorygroup['name'].lower() == context.inventory_group_data['name'].lower()]
    assert_equal(len(inventorygroup), 1)
    inventorygroup = inventorygroup[0]
    inventorygroup_info = {'id': inventorygroup['id'], 'data_key': inventorygroup['data_key']}
    save_item_id(inventorygroup_info, 'inventory_group', context)
