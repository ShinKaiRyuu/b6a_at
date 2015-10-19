from behave import *
from nose.tools import assert_equal, assert_true
from selenium.webdriver.support.wait import WebDriverWait

from features.steps.add_steps import save_item_id
from helpers.data_helpers import create_inventory_group_data, create_item_data, create_opportunity_data

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
    inventorygroup_id = inventorygroup['links_without_title'][0]['update'].split('/')[-1]
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
    item_data = create_item_data()
    context.page.fill_item_info(**item_data)
    context.item_data = item_data
    context.page.wait_for_form_closed()


@then("I want to see item in list") #TODO fix
def step_impl(context):
    context.driver.refresh()
    context.page.wait_for_loading(240)
    wait = WebDriverWait(context.driver, 10)
    wait.until(lambda x: (len(context.page.get_data()) == 1) is True)
    item = [item for item in context.page.get_data() if
            item['name'].lower() == context.item_data['item_name'].lower()]
    assert_equal(len(item), 1)
    item = item[0]
    item_id = item['links_without_title'][0]['update'].split('/')[-1]
    item_info = {'data_key': item['data_key'], 'id': item_id}
    context.item_info = item_info


@when("I view item")
def step_impl(context):
    context.page.view_item(context.item_info['id'])


@then("I add a new opportunity")
def step_impl(context):
    opportunity_data = create_opportunity_data()
    context.page.fill_opportunity_info(**opportunity_data)
    context.opportunity_data = opportunity_data
    context.page.wait_for_form_closed()


@then("I want to see opportunity in list")
def step_impl(context):
    context.driver.refresh()
    context.page.wait_for_loading(240)
    wait = WebDriverWait(context.driver, 30)
    wait.until(lambda x: (len(context.page.get_data()) == 1) is True)
    opportunity = [opportunity for opportunity in context.page.get_data() if
                   opportunity['name'].lower() == context.opportunity_data['opportunity_name'].lower()]
    assert_equal(len(opportunity), 1)
    opportunity = opportunity[0]
    opportunity_id = opportunity['links_without_title'][0]['update'].split('/')[-1]
    opportunity_info = {'data_key': opportunity['data_key'], 'id': opportunity_id}
    context.opportunity_info = opportunity_info


@then("I open items page")
def step_impl(context):
    context.page.open_items_page(context.inventorygroup_data)


@then("I want to see items details")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(lambda x: (len(context.page.get_data()) != 0) is True)
    temp = context.page.get_data()
    inventorygroup = [inventorygroup for inventorygroup in context.page.get_data() if
            inventorygroup['inventory_title'].lower() == context.inventorygroup_data['name'].lower()]
    assert_equal(len(inventorygroup), 1)
    inventorygroup = inventorygroup[0]
    assert_equal(inventorygroup['impressions_total'], context.opportunity_data['opportunity_views'])
    assert_equal(inventorygroup['vpm_total'], float(context.item_data['item_vpm']))


@when("I open item by clicking on name in tabel")
def step_impl(context):
    context.page.open_name_link(context.inventorygroup_data['name'])


@when("I open item by clicking on view in tabel")
def step_impl(context):
    context.page.open_view_link(context.inventorygroup_data['slug'])


@then("I want to see items opportunity details")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(lambda x: (len(context.page.get_item_data()) != 0) is True)
    temp2 = context.page.get_item_data()
    item = [item for item in context.page.get_item_data() if
            item['activation_element_title'].lower() == context.item_data['item_name'].lower()]
    assert_equal(len(item), 1)
    item = item[0]
    assert_equal(item['impressions_total'], context.opportunity_data['opportunity_views'])
    context.page.close_modal_window()


@then("I want to see items opportunity information")
def step_impl(context):
    assert_true(context.inventorygroup_data['content'] in context.driver.page_source)
