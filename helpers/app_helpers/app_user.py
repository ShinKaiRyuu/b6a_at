from nose.tools import assert_in, assert_equal
from helpers.app_helpers.app_session import get_admin_session, get_url, get_csrf_token, APP_URL, URL_PREFIXES
import pages


def create_user(user_data):
    s = get_admin_session()
    user_info = _create_user_record(s, user_data)
    _update_user_record(s, user_info.get('id'), user_data)
    return user_info


def _create_user_record(session, user_data):
    url = get_url(pages.CreateUserPage.url_path)
    r = session.get(url)

    payload = {
        '_csrf': get_csrf_token(r),
        'User[username]': user_data['username'],
        'User[email]': user_data['email'],
        'User[password]': user_data['password'],
    }
    r = session.post(url, data=payload)
    assert_equal(r.status_code, 200)
    assert_in('User has been created', r.text)
    user_id = r.url.split('?id=')[-1]
    return {'id': user_id, 'data_key': user_id}


def _update_user_record(session, user_id, user_data):
    params = {'id': user_id}
    url = get_url(pages.UpdateUserProfileDetailsPage.url_path)
    r = session.get(url, params=params)

    payload = {
        '_csrf': get_csrf_token(r),
        'Profile[name]': user_data['name'],
        'Profile[public_email]': user_data['public_email'],
        'Profile[location]': user_data['location'],
        'Profile[bio]': user_data['bio'],
        'Profile[partner_id]': user_data['partner_id'],
    }
    r = session.post(url, params=params, data=payload)
    assert_equal(r.status_code, 200)
 #   assert_in('Profile details have been updated', r.text)


def delete_user(user_id):
    s = get_admin_session()
    params = {'id': user_id}
    r = s.get(get_url(pages.UpdateUserProfileDetailsPage.url_path), params=params)

    if 'The requested page does not exist' in r.text:
        assert_equal(r.status_code, 404)
        return

    if 'Access denied' in r.text:
        assert_equal(r.status_code, 403)
        return

    payload = {'_csrf': get_csrf_token(r)}
    url = ''.join([APP_URL, '/user/admin/delete?id={}'.format(user_id)])
    r = s.post(url, data=payload)
    assert_equal(r.status_code, 200)
    assert_in('User has been deleted', r.text)


def create_blocked_user(user_data):
    s = get_admin_session()
    user_info = _create_user_record(s, user_data)
    _update_user_record(s, user_info.get('id'), user_data)
    _block_user(s, user_info.get('id'))
    return user_info


def _block_user(session, user_id):
    params = {'id': user_id}
    url = get_url(pages.UpdateUserProfileDetailsPage.url_path)
    r = session.get(url, params=params)

    payload = {'_csrf': get_csrf_token(r)}
    url = get_url(URL_PREFIXES['block_user'])
    r = session.post(url, params=params, data=payload)
    assert_equal(r.status_code, 200)
    assert_in('User has been blocked', r.text)
