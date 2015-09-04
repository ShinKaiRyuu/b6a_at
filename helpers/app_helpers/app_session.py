import re
import pages

import requests

APP_URL = 'http://b6a.scoreboard-qa.selfip.com'
ADMIN_CREDENTIALS = {'username': 'admin', 'password': '123456'}
ROOT_CREDENTIALS = {'username': 'root', 'password': '123456'}
URL_PREFIXES = {
    'create_product': '/admin/goods/create',
    'delete_product': '/admin/goods/delete/{}',
    'block_user': '/user/admin/block',
    'create_partner': '/admin/partner/create',
    'delete_partner': '/admin/partner/delete/{}',
    'create_page': '/admin/page/create',
    'delete_page': '/admin/page/delete/{}',
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
    assert '/user/logout' in r.text
    return s


def get_csrf_token(response):
    response_content = response.text
    csrf_pattern = re.compile('<meta name="csrf-token" content="(.*?)">')
    return csrf_pattern.findall(response_content)[0]


def get_admin_session():
    global _admin_session
    if not _admin_session:
        _admin_session = _get_logged_session(ADMIN_CREDENTIALS)
    return _admin_session
