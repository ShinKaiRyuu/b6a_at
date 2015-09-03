from bs4 import BeautifulSoup
from helpers.app_helpers.app_session import get_admin_session, get_url, URL_PREFIXES, get_csrf_token
import pages


def get_enabled_partners_ids():
    s = get_admin_session()
    url = get_url(pages.ManagePartnersPage.url_path)
    r = s.get(url)
    soup = BeautifulSoup(r.text)
    partners = soup.findAll(lambda tag: 'data-key' in tag.attrs and 'Enabled' in tag.text)
    partners_ids = [p['data-key'] for p in partners]
    return partners_ids


def create_partner(partner_data):
    s = get_admin_session()
    url = get_url(URL_PREFIXES['create_partner'])
    r = s.get(url)
    partner_id = r.url.split('/')[-1]
    url = r.url

    payload = {
        '_csrf': get_csrf_token(r),
        'Partner[name]': partner_data['name'],
        'Partner[star_name]': partner_data['star_name'],
        'Partner[star_email]': partner_data['star_email'],
        'Partner[status]': partner_data['status'],
    }
    r = s.post(url, data=payload)
    assert 'successfully.' in r.text
    return partner_id


def delete_partner(partner_id):
    s = get_admin_session()
    url = get_url(pages.ManagePartnersPage.url_path)
    r = s.get(url)

    payload = {'_csrf': get_csrf_token(r)}
    url = get_url(URL_PREFIXES['delete_partner']).format(partner_id)
    r = s.post(url, data=payload)

    if 'The requested page does not exist' in r.text:
        return

    assert 'Deleted successfully.' in r.text
