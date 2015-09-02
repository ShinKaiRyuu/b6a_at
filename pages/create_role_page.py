from pages.base_page import BasePage


class CreateRolePage(BasePage):
    url_path = '/rbac/role/create'

    access_denied = Find ('')