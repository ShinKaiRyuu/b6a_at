from bs4 import BeautifulSoup
from helpers.app_helpers.app_session import get_admin_session, get_url, get_csrf_token, URL_PREFIXES
import pages


def create_page(page_data):
    s = get_admin_session()
    url = get_url(URL_PREFIXES['create_page'])
    r = s.get(url)
    page_id = r.url.split('/')[-1]
    url = r.url

    payload = {
        '_csrf': get_csrf_token(r),
        'Page[name]': page_data['name'],
        'Page[slug]': page_data['slug'],
        'Page[parent_id]': page_data['parent_id'],
        'Page[content]': page_data['content'],
        'Page[status]': page_data['status'],
        'Page[title]': page_data['title'],
        'Page[keywords]': page_data['keywords'],
        'Page[description]': page_data['description'],
        'user_created_id': 1,
    }

    r = s.post(url, data=payload)
    assert 'successfully.' in r.text
    return page_id


def delete_page(page_id):
    s = get_admin_session()
    url = get_url(pages.ManagePagesPage.url_path)
    r = s.get(url)

    payload = {'_csrf': get_csrf_token(r)}
    url = get_url(URL_PREFIXES['delete_page']).format(page_id)
    r = s.post(url, data=payload)

    if 'The requested page does not exist' in r.text:
        return

    assert 'Deleted successfully.' in r.text


def get_published_parent_pages_ids():
    s = get_admin_session()
    url = get_url(pages.ManagePagesPage.url_path)
    r = s.get(url)
    soup = BeautifulSoup(r.text)
    pages_published = soup.findAll(lambda tag: 'data-key' in tag.attrs and 'Published' in tag.text)
    pages_parent = list(filter(lambda x: 'glyphicon-paperclip' not in str(x), pages_published))
    pages_parent_ids = [p['data-key'] for p in pages_parent]
    return pages_parent_ids
