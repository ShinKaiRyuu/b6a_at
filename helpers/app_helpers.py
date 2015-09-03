import re

import requests
import pages

APP_URL = 'http://b6a.scoreboard-qa.selfip.com'
ADMIN_CREDENTIALS = {'username': 'admin', 'password': '123456'}
ROOT_CREDENTIALS = {'username': 'root', 'password': '123456'}
URL_PREFIXES = {
    'create_product': '/admin/goods/create',
    'delete_product': '/admin/goods/delete/{}',
}


def get_requests_app_cookies(credentials):
    s = _get_logged_session(credentials)
    return s.cookies


def _get_url(url_path):
    return ''.join([APP_URL, url_path])


def _get_logged_session(credentials):
    url = _get_url(pages.LoginPage.url_path)
    s = requests.Session()
    r = s.get(url)

    payload = {
        '_csrf': _get_csrf_token(r),
        'login-form[rememberMe]': '0',
        'login-form[login]': credentials['username'],
        'login-form[password]': credentials['password']
    }
    r = s.post(url, data=payload)
    assert '/user/logout' in r.text
    return s


def _get_csrf_token(response):
    response_content = response.text
    csrf_pattern = re.compile('<meta name="csrf-token" content="(.*?)">')
    return csrf_pattern.findall(response_content)[0]


def _get_admin_session():
    return _get_logged_session(ADMIN_CREDENTIALS)


def create_user(user_data):
    s = _get_admin_session()
    user_id = _create_user_record(s, user_data)
    _update_user_record(s, user_id, user_data)
    return user_id


def _create_user_record(session, user_data):
    url = _get_url(pages.CreateUserPage.url_path)
    r = session.get(url)

    payload = {
        '_csrf': _get_csrf_token(r),
        'User[username]': user_data['username'],
        'User[email]': user_data['email'],
        'User[password]': user_data['password'],
    }
    r = session.post(url, data=payload)
    assert 'User has been created' in r.text
    user_id = r.url.split('/')[-1]
    return user_id


def _update_user_record(session, user_id, user_data):
    params = {'id': user_id}
    url = _get_url(pages.UpdateUserProfileDetailsPage.url_path)
    r = session.get(url, params=params)

    payload = {
        '_csrf': _get_csrf_token(r),
        'Profile[name]': user_data['name'],
        'Profile[public_email]': user_data['public_email'],
        'Profile[location]': user_data['location'],
        'Profile[bio]': user_data['bio'],
        'Profile[partner_id]': user_data['partner_id'],
    }
    r = session.post(url, params=params, data=payload)
    assert 'Profile details have been updated' in r.text


def delete_user(user_id):
    s = _get_admin_session()
    params = {'id': user_id}
    r = s.get(_get_url(pages.UpdateUserProfileDetailsPage.url_path), params=params)

    if 'The requested page does not exist' in r.text:
        return

    payload = {'_csrf': _get_csrf_token(r)}
    url = ''.join([APP_URL, '/user/admin/delete/{}'.format(user_id)])
    r = s.post(url, data=payload)
    assert 'User has been deleted' in r.text


def create_product(product_data):
    s = _get_admin_session()
    url = _get_url(URL_PREFIXES['create_product'])
    r = s.get(url)
    product_id = r.url.split('/')[-1]
    url = r.url

    payload = {
        '_csrf': _get_csrf_token(r),
        'Goods[title]': product_data['title'],
        'Goods[slug]': product_data['slug'],
        'Goods[description]': product_data['description'],
        'Goods[price]': product_data['price'],
        'Goods[enabled]': product_data['enabled'],
    }
    r = s.post(url, data=payload)
    assert 'successfully.' in r.text
    return product_id


def delete_product(product_id):
    s = _get_admin_session()
    url = _get_url(pages.ManageProductsPage.url_path)
    r = s.get(url)

    payload = {
        '_csrf': _get_csrf_token(r),
    }

    url = _get_url(URL_PREFIXES['delete_product']).format(product_id)
    r = s.post(url, data=payload)

    if 'The requested page does not exist' in r.text:
        return

    assert 'Deleted successfully.' in r.text
