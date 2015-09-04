from bs4 import BeautifulSoup
from helpers.app_helpers.app_session import get_admin_session, get_url, create_source, delete_source
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
    partner_payload = {
        'Partner[name]': partner_data['name'],
        'Partner[star_name]': partner_data['star_name'],
        'Partner[star_email]': partner_data['star_email'],
        'Partner[status]': partner_data['status'],
    }
    return create_source(source_name='partner', source_payload=partner_payload)


def delete_partner(partner_id):
    delete_source(source_name='partner', source_id=partner_id)
