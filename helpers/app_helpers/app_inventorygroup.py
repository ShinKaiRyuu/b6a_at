from helpers.app_helpers.app_session import create_source, delete_source


def create_inventorygroup(inventorygroup_data):
    inventorygroup_payload = {
        'Inventorygroup[name]': inventorygroup_data['name'],
        'Inventorygroup[partner_id]': inventorygroup_data['partner_id'],
        'Inventorygroup[content]': inventorygroup_data['content'],
    }
    return create_source(source_name='product', source_payload=inventorygroup_payload)


def delete_inventorygroup(inventorygroup_id):
    delete_source(source_name='product', source_id=inventorygroup_id)
