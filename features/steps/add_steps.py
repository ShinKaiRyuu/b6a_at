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
