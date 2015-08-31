from ast import literal_eval
from collections import OrderedDict
import random
from tempmail import TempMail
from faker import Faker

_faker = None


def get_faker():
    global _faker
    if not _faker:
        _faker = Faker()
    return _faker


def make_ordered_dict(keys, _locals):
    kwargs = OrderedDict()
    for key in keys:
        value = _locals.get(key)
        kwargs[key] = modify_value(value)
    return kwargs


def modify_value(value):
    if '[' in value:
        return literal_eval(value.replace('empty', ' '))
    elif 'empty' in value:
        return ''
    elif 'spaces' in value:
        return ' ' * int(value.split(':')[-1][:-1])
    elif 'unique_email' in value:
        return TempMail().get_email_address()
    elif 'faker' in value:
        faker = get_faker()
        faker_attr = value.split('.')[-1]
        return getattr(faker, faker_attr)().split('\n')[0]
    else:
        return value


def create_user_data():
    faker = get_faker()
    return {
        'username': faker.user_name(),
        'email': faker.email(),
        'password': faker.password(),
        'name': faker.name(),
        'public_email': faker.email(),
        'location': faker.city(),
        'bio': faker.user_name(),
        'partner_id': random.choice(['1', '2'])  # TODO get partners ids
    }


def create_product_data():
    faker = get_faker()
    return {
        'title': faker.company(),
        'slug': faker.pystr(max_chars=10),
        'description': faker.pystr(max_chars=20),
        'price': faker.pyint(),
        'enabled': random.getrandbits(1),

    }
