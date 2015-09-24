from ast import literal_eval
import random
from tempmail import TempMail
from faker import Faker
from helpers.app_helpers.app_partner import get_enabled_partners_data_keys

_faker = None


def get_faker():
    global _faker
    if not _faker:
        _faker = Faker()
    return _faker


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
        'name': faker.pystr(max_chars=10),
        'public_email': faker.email(),
        'location': faker.city(),
        'bio': faker.user_name(),
        'partner_id': random.choice(get_enabled_partners_data_keys())
    }


def create_product_data():
    faker = get_faker()
    product_data = {
        'title': faker.pystr(max_chars=10),
        'description': ''.join(['<p>', faker.pystr(max_chars=20), '</p>']),
        'price': ''.join([str(faker.pyint()), '.00']),
        'enabled': 1,

    }
    product_data['seourl'] = _prepare_for_slug(product_data['title'])
    return product_data


def create_partner_data():
    faker = get_faker()
    return {
        'name': faker.user_name(),
        'star_name': faker.user_name(),
        'star_email': faker.email(),
        'status': 1,
    }


def create_page_data():
    faker = get_faker()
    page_data = {
        'name': faker.pystr(max_chars=10),
        'parent_id': '',
        'content': ''.join(['<p>', faker.pystr(max_chars=20), '</p>']),
        'status': 'published',
        'title': faker.pystr(max_chars=10),
        'keywords': faker.pystr(max_chars=10),
        'description': faker.pystr(max_chars=10),
    }
    page_data['slug'] = _prepare_for_slug(page_data['name'])
    return page_data


def create_inventory_group_data():
    faker = get_faker()
    inventory_group_data = {
        'name': faker.pystr(max_chars=10),
        'partner_id': random.choice(get_enabled_partners_data_keys()),
        'content': ''.join(['<p>', faker.pystr(max_chars=20), '</p>']),
    }
    inventory_group_data['slug'] = _prepare_for_slug(inventory_group_data['name'])
    return inventory_group_data


def create_item_data():
    faker = get_faker()
    item__data = {
        'item_name': faker.pystr(max_chars=10),
        'item_vpm': faker.pyint(),
        'item_content': ''.join(['<p>', faker.pystr(max_chars=20), '</p>']),
        'item_date': faker.date(pattern="%m/%d/2015")
    }
    item__data['slug'] = _prepare_for_slug(item__data['item_name'])
    return item__data


def create_opportunity_data():
    faker = get_faker()
    opportunity__data = {
        'opportunity_name': faker.pystr(max_chars=10),
        'opportunity_views': faker.pyint(),
        'opportunity_date': faker.date(pattern="%m/%d/2015")
    }
    opportunity__data['slug'] = _prepare_for_slug(opportunity__data['opportunity_name'])
    return opportunity__data


def _prepare_for_slug(some_text):
    return some_text.lower().replace(' ', '-').replace('.', '').replace(',', '')
