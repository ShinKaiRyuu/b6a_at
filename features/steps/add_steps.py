from behave import *

from helpers import app_helpers
from helpers.data_helpers import create_user_data, create_product_data, create_partner_data

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


@given("created product")
def step_impl(context):
    context.product_data = create_product_data()
    context.product_id = app_helpers.create_product(context.product_data)
    save_item_id(context.product_id, 'products', context)


@given("created partner")
def step_impl(context):
    context.user_data = create_partner_data()
    context.user_id = app_helpers.create_user(context.user_data)
    save_item_id(context.user_id, 'users', context)


def save_item_id(item_id, entity_name, context):
    items = context.created_items.get(entity_name, [])
    items.append(item_id)
    context.created_items[entity_name] = items
