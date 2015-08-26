from webium.driver import get_driver


def get_updated_driver():
    driver = get_driver()
    driver.set_page_load_timeout(60)
    driver.maximize_window()
    return driver
