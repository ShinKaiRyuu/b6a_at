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
    product_data = {
        'title': faker.name(),
        'description': ''.join(['<p>', faker.pystr(max_chars=20), '</p>']),
        'price': ''.join([str(faker.pyint()), '.00']),
        'enabled': 1,

    }
    product_data['slug'] = product_data['title'].lower().replace(' ', '-').replace('.', '').replace(',', '')
    return product_data


def create_partner_data():
    faker = get_faker()
    partner_data = {
        'title': faker.name(),
        'description': ''.join(['<p>', faker.pystr(max_chars=20), '</p>']),
        'price': ''.join([str(faker.pyint()), '.00']),
        'enabled': random.getrandbits(1),

    }
    partner_data['slug'] = partner_data['title'].lower().replace(' ', '-').replace('.', '').replace(',', '')
    return partner_data
