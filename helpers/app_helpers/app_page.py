from bs4 import BeautifulSoup
from helpers.app_helpers.app_session import get_admin_session, get_url, create_source, delete_source
import pages


def create_page(page_data):
    page_payload = {
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
    return create_source(source_name='page', source_payload=page_payload)


def delete_page(page_id):
    delete_source(source_name='page', source_id=page_id)


def get_published_parent_pages_ids():
    s = get_admin_session()
    url = get_url(pages.ManagePagesPage.url_path)
    r = s.get(url)
    soup = BeautifulSoup(r.text)
    pages_published = soup.findAll(lambda tag: 'data-key' in tag.attrs and 'Published' in tag.text)
    pages_parent = list(filter(lambda x: 'glyphicon-paperclip' not in str(x), pages_published))
    pages_parent_ids = [p['data-key'] for p in pages_parent]
    return pages_parent_ids
