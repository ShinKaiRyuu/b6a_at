import re
from bs4 import BeautifulSoup
from nose.tools import assert_equal, assert_in
import pages

import requests

APP_URL = 'http://b6a.scoreboard-qa.selfip.com'
ADMIN_CREDENTIALS = {'username': 'admin', 'password': '123456'}
ROOT_CREDENTIALS = {'username': 'root', 'password': '123456'}
URL_PREFIXES = {
    'create_source': '/admin/{name}/create',
    'delete_source': '/admin/{name}/delete/{id}',
    'block_user': '/user/admin/block',
}
SOURCE_NAMES_MAP = {
    'product': 'goods',
    'partner': 'partner',
    'page': 'page',
    'inventorygroup': 'groups'
}
SOURCE_URLS_MAP = {
    'product': pages.ManageProductsPage.url_path,
    'partner': pages.ManagePartnersPage.url_path,
    'page': pages.ManagePagesPage.url_path,
    'inventorygroup': pages.ManageInventorygroupsPage.url_path,
}

_admin_session = None


def get_requests_app_cookies(credentials):
    s = _get_logged_session(credentials)
    return s.cookies


def get_url(url_path):
    return ''.join([APP_URL, url_path])


def _get_logged_session(credentials):
    url = get_url(pages.LoginPage.url_path)
    s = requests.Session()
    r = s.get(url)

    payload = {
        '_csrf': get_csrf_token(r),
        'login-form[rememberMe]': '0',
        'login-form[login]': credentials['username'],
        'login-form[password]': credentials['password']
    }
    r = s.post(url, data=payload)
    assert_equal(r.status_code, 200)
    assert_in('/user/logout', r.text)
    return s


def get_csrf_token(response, on_form=False):
    response_content = response.text
    csrf_pattern = re.compile('<meta name="csrf-token" content="(.*?)">')
    if on_form:
        csrf_pattern = re.compile('<input type="hidden" name="_csrf" value="(.*?)">')
    return csrf_pattern.findall(response_content)[0]


def get_admin_session():
    global _admin_session
    if not _admin_session:
        _admin_session = _get_logged_session(ADMIN_CREDENTIALS)
    return _admin_session


def create_source(source_name, source_payload):
    s = get_admin_session()
    url = get_url(URL_PREFIXES['create_source'].format(name=SOURCE_NAMES_MAP[source_name]))
    r = s.get(url)
    source_payload['_csrf'] = get_csrf_token(r)
    source_id = r.url.split('/')[-1]
    url = r.url
    r = s.post(url, data=source_payload)
    data_key = _get_data_key(source_payload, r)
    assert_equal(r.status_code, 200)
    assert_in('successfully.', r.text)
    return {'id': source_id, 'data_key': data_key}


def delete_source(source_name, source_id):
    s = get_admin_session()
    url = get_url(SOURCE_URLS_MAP[source_name])
    r = s.get(url)

    payload = {'_csrf': get_csrf_token(r)}
    url = get_url(URL_PREFIXES['delete_source']).format(name=SOURCE_NAMES_MAP[source_name], id=source_id)
    r = s.post(url, data=payload)

    if r.status_code == 200:
        assert_in('Deleted successfully.', r.text)
    else:
        assert_equal(r.status_code, 404)


def _get_data_key(payload, response):
    name = payload[[k for k in payload.keys() if '[name]' in k or '[title]' in k][0]]
    soup = BeautifulSoup(response.text)
    trs = soup.findAll(lambda tag: tag.name == 'tr' and 'data-key' in tag.attrs)
    tr = [tr for tr in trs if name in str(tr)][0]
    return tr['data-key']
