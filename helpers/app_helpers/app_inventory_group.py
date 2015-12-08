from nose.tools import assert_equal, assert_in
from bs4 import BeautifulSoup
from helpers.app_helpers.app_session import (
    get_admin_session, get_url, URL_PREFIXES, SOURCE_NAMES_MAP, get_csrf_token, delete_source,
)
import pages


def create_inventory_group(inventory_group_data):
    payload = {
        'InventoryGroup[name]': inventory_group_data['name'],
        'InventoryGroup[slug]': inventory_group_data['slug'],
        'InventoryGroup[partner_id]': inventory_group_data['partner_id'],
        'InventoryGroup[content]': inventory_group_data['content'],
    }
    s = get_admin_session()
    url = get_url(pages.ManageInventorygroupsPage.url_path + '?sort=-id')
    s.get(url)
    url = get_url(URL_PREFIXES['create_source'].format(name=SOURCE_NAMES_MAP['inventory_group']))
    r = s.get(url)
    data_key = _get_group_data_key(r)
    assert_equal(r.status_code, 200)
    payload['_csrf'] = get_csrf_token(r, on_form=True)
    payload['InventoryGroup[id]'] = data_key
    r = s.post(url, data=payload)
    assert_equal(r.status_code, 200)
    url = get_url(pages.ManageInventorygroupsPage.url_path + '?sort=-id')
    r = s.get(url)
    assert_in(inventory_group_data['name'], r.text)
    _id = _get_group_id(r, data_key)
    return {'id': _id, 'data_key': data_key}


def delete_inventory_group(inventory_group_id):
    delete_source(source_name='inventory_group', source_id=inventory_group_id)


def _get_group_data_key(response):
    soup = BeautifulSoup(response.text)
    data_key = soup.find('input', id='inventorygroup-id')['value']
    return data_key


def _get_group_id(response, data_key):
    soup = BeautifulSoup(response.text)
    _id = soup.find('tr', attrs={'data-key': data_key}).a['href'].split('?id=')[-1]
    return _id
