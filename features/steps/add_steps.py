from behave import *

from helpers import app_helpers
from helpers.data_helpers import create_user_data, create_product_data, create_partner_data, create_page_data

use_step_matcher("re")


def data_from_table(context):
    return [
        {head: row[head] for head in context.table.headings if row[head]}
        for row in context.table.rows
        ]


@given("created blocked user")
@given("created user")
def step_impl(context):
    if 'blocked' not in context.step_name:
        create_user = app_helpers.create_user
    else:
        create_user = app_helpers.create_blocked_user

    context.user_data = create_user_data()
    context.user_id = create_user(context.user_data)
    save_item_id(context.user_id, 'users', context)


@given("created disabled product")
@given("created product")
def step_impl(context):
    context.product_data = create_product_data()
    if 'disabled' in context.step_name:
        context.product_data['enabled'] = 0

    context.product_id = app_helpers.create_product(context.product_data)
    save_item_id(context.product_id, 'products', context)


@given("created disabled partner")
@given("created partner")
def step_impl(context):
    context.partner_data = create_partner_data()
    if 'disabled' in context.step_name:
        context.product_data['status'] = 0

    context.partner_id = app_helpers.create_partner(context.partner_data)
    save_item_id(context.partner_id, 'partners', context)


@given('created parent page with draft additional page')
@given('created parent page with additional page')
@given('created draft parent page')
@given('created parent page')
def step_impl(context):
    context.parent_page_data = create_page_data()

    if 'draft parent' in context.step_name:
        context.page_data['status'] = 'draft'

    context.parent_page_id = app_helpers.create_page(context.parent_page_data)
    save_item_id(context.parent_page_id, 'pages', context)

    if 'additional page' in context.step_name:
        context.additional_page_data = create_page_data()
        context.additional_page_data['parent_id'] = context.parent_page_id
        if 'draft additional' in context.step_name:
            context.additional_page_data['status'] = 'draft'
        context.additional_page_id = app_helpers.create_page(context.additional_page_data)
        save_item_id(context.additional_page_id, 'pages', context)


def save_item_id(item_id, entity_name, context):
    items = context.created_items.get(entity_name, [])
    items.insert(0, item_id)
    context.created_items[entity_name] = items
