import re
import requests
from pages import LoginPage, CreateUserPage, UpdateUserPage, CreateProductPage

APP_URL = 'http://b6a.scoreboard-qa.selfip.com'
ADMIN_CREDENTIALS = {'username': 'admin', 'password': '123456'}


def get_requests_app_cookies(credentials):
    s = _get_logged_session(credentials)
    return s.cookies


def _get_url(page):
    return ''.join([APP_URL, page.url_path])


def _get_logged_session(credentials):
    url = _get_url(LoginPage)
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
    csrf_pattern = re.compile('<input type="hidden" name="_csrf" value="(.*?)">')
    return csrf_pattern.findall(response_content)[0]


def _get_admin_session():
    return _get_logged_session(ADMIN_CREDENTIALS)


def create_user(user_data):
    s = _get_admin_session()
    user_id = _create_user_record(s, user_data)
    _update_user_record(s, user_id, user_data)
    return user_id


def _create_user_record(session, user_data):
    url = _get_url(CreateUserPage)
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
    url = _get_url(UpdateUserPage)
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
    r = s.get(_get_url(UpdateUserPage), params=params)

    if 'The requested page does not exist' in r.text:
        return 
    
    payload = {'_csrf': _get_csrf_token(r)}
    url = ''.join([APP_URL, '/user/admin/delete/{}'.format(user_id)])
    r = s.post(url, data=payload)
    assert 'User has been deleted' in r.text


def create_product(product_data):
    s = _get_admin_session()
    url = _get_url(CreateProductPage)
    r = s.get(url)

    payload = {
        '_csrf': _get_csrf_token(r),
        'Product[title]': product_data['title'],
        'Product[slug]': product_data['slug'],
        'Product[description]': product_data['description'],
        'Product[price]': product_data['price'],
        'Product[enabled]': product_data['enabled'],
    }
    r = s.post(url, data=payload)
    assert 'Product has been created' in r.text
    product_id = r.url.split('/')[-1]
    return product_id


def delete_product(product_id):
    raise NotImplementedError
