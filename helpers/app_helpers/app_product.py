from helpers.app_helpers.app_session import get_admin_session, URL_PREFIXES, get_url, get_csrf_token
import pages


def create_product(product_data):
    s = get_admin_session()
    url = get_url(URL_PREFIXES['create_product'])
    r = s.get(url)
    product_id = r.url.split('/')[-1]
    url = r.url

    payload = {
        '_csrf': get_csrf_token(r),
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
    s = get_admin_session()
    url = get_url(pages.ManageProductsPage.url_path)
    r = s.get(url)

    payload = {
        '_csrf': get_csrf_token(r),
    }

    url = get_url(URL_PREFIXES['delete_product']).format(product_id)
    r = s.post(url, data=payload)

    if 'The requested page does not exist' in r.text:
        return

    assert 'Deleted successfully.' in r.text
