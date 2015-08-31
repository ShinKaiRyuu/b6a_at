from behave import *

from helpers import app_helpers
from helpers.data_helpers import create_user_data, create_product_data

use_step_matcher("re")
data_from_table = lambda context: [
    {head: row[head] for head in context.table.headings if row[head]}
    for row in context.table.rows
    ]


@given("created user")
def step_impl(context):
    user_data = create_user_data()
    user_id = app_helpers.create_user(user_data)
    save_item_id(user_id, 'users', context)


@given("created product")
def step_impl(context):
    product_data = create_product_data()
    product_id = app_helpers.create_product(product_data)
    save_item_id(product_id, 'products', context)


def save_item_id(item_id, entity_name, context):
    items = context.created_items.get(entity_name, [])
    items.append(item_id)
