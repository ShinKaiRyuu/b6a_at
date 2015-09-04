from helpers.app_helpers.app_session import create_source, delete_source


def create_product(product_data):
    product_payload = {
        'Goods[title]': product_data['title'],
        'Goods[slug]': product_data['seourl'],
        'Goods[description]': product_data['description'],
        'Goods[price]': product_data['price'],
        'Goods[enabled]': product_data['enabled'],
    }
    return create_source(source_name='product', source_payload=product_payload)


def delete_product(product_id):
    delete_source(source_name='product', source_id=product_id)
