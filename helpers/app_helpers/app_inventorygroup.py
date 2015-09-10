from helpers.app_helpers.app_session import (
    delete_source, get_admin_session, get_url, URL_PREFIXES, SOURCE_NAMES_MAP, get_csrf_token
)
import pages


def create_inventorygroup(inventorygroup_data):
    payload = {
        'Inventorygroup[name]': inventorygroup_data['name'],
        'Inventorygroup[slug]': inventorygroup_data['slug'],
        'Inventorygroup[partner_id]': inventorygroup_data['partner_id'],
        'Inventorygroup[content]': inventorygroup_data['content'],
    }
    # TODO FIX
    s = get_admin_session()
    url = get_url(pages.ManageInventorygroupsPage.url_path)
    r = s.get(url)

    url = get_url(URL_PREFIXES['create_source'].format(name=SOURCE_NAMES_MAP['inventorygroup']))
    r = s.get(url)
    payload['_csrf'] = get_csrf_token(r, on_form=True)
    return None


def delete_inventorygroup(inventorygroup_id):
    delete_source(source_name='inventorygroup', source_id=inventorygroup_id)
