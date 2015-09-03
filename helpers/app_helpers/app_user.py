from helpers.app_helpers.app_session import get_admin_session, get_url, get_csrf_token, APP_URL, URL_PREFIXES
import pages


def create_user(user_data):
    s = get_admin_session()
    user_id = _create_user_record(s, user_data)
    _update_user_record(s, user_id, user_data)
    return user_id


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
    assert 'User has been created' in r.text
    user_id = r.url.split('/')[-1]
    return user_id


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
    assert 'Profile details have been updated' in r.text


def delete_user(user_id):
    s = get_admin_session()
    params = {'id': user_id}
    r = s.get(get_url(pages.UpdateUserProfileDetailsPage.url_path), params=params)

    if 'The requested page does not exist' in r.text:
        return

    payload = {'_csrf': get_csrf_token(r)}
    url = ''.join([APP_URL, '/user/admin/delete/{}'.format(user_id)])
    r = s.post(url, data=payload)
    assert 'User has been deleted' in r.text

def create_blocked_user(user_data):
    s = get_admin_session()
    user_id = _create_user_record(s, user_data)
    _update_user_record(s, user_id, user_data)
    _block_user(s, user_id)
    return user_id

def _block_user(session, user_id):
    params = {'id': user_id}
    url = get_url(pages.UpdateUserProfileDetailsPage.url_path)
    r = session.get(url, params=params)

    payload = {'_csrf': get_csrf_token(r)}
    url = get_url(URL_PREFIXES['block_user'])
    r = session.post(url, params=params, data=payload)
    assert 'User has been blocked' in r.text
