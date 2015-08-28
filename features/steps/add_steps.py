import random

from behave import *
from faker import Faker

from helpers import app_helpers

use_step_matcher("re")
data_from_table = lambda context: [
    {head: row[head] for head in context.table.headings if row[head]}
    for row in context.table.rows
    ]


def _create_user_data():
    faker = Faker()
    return {
        'username': faker.user_name(),
        'email': faker.email(),
        'password': faker.password(),
        'name': faker.name(),
        'public_email': faker.email(),
        'location': faker.city(),
        'bio': faker.user_name(),
        'partner_id': random.choice(['1', '2'])
    }


@given("created user")
def step_impl(context):
    user_data = _create_user_data()
    user_id = app_helpers.create_user(user_data)

    context.created_items['users'] = context.created_items.get('users', [])
    context.created_items['users'].append(user_id)

    print(context.created_items)

    import time
    time.sleep(5)


def _create_product_data():
    faker = Faker()
    return {
        'title': faker.company(),
        'slug': faker.pystr(max_chars=10),
        'description': faker.pystr(max_chars=20),
        'price': faker.pyint(),
        'enabled': random.getrandbits(1),

    }


@given("created product")
def step_impl(context):
    product_data = _create_product_data()
    product_id = app_helpers.create_product(product_data)

    context.created_items['products'] = context.created_items.get('products', [])
    context.created_items['products'].append(product_id)

    print(context.created_items)

    import time
    time.sleep(5)
