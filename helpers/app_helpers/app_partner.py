from bs4 import BeautifulSoup
from helpers.app_helpers.app_session import get_admin_session, get_url
import pages


def get_enabled_partners_ids():
    s = get_admin_session()
    url = get_url(pages.ManagePartnersPage.url_path)
    r = s.get(url)
    soup = BeautifulSoup(r.text)
    partners = soup.findAll(lambda tag: 'data-key' in tag.attrs and 'Enabled' in tag.text)
    partners_ids = [p['data-key'] for p in partners]
    return partners_ids
