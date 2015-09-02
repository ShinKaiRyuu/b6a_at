from selenium.webdriver.common.by import By
from webium import Find

from pages.base_page import BasePage


class CreatePermissionPage(BasePage):
    url_path = '/rbac/permission/create'

    access_denied = Find(by=By.XPATH, value="")
