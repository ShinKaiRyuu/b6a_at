from selenium.webdriver.common.by import By
from webium import Find, Finds

from pages.base_page import BasePage


class UserAssignmentsPage(BasePage):
    url_path = '/user/admin/assignments'

    # select
    assignments_seartch_field = Find(value='.select2-search__field')

    # added assignmnets
    assignments = \
        Finds(by=By.XPATH,
              value='//ul[@class="select2-selection__rendered"]/li[@class="select2-selection__choice"]')

    # update
    update = Find(value='.btn-success')

    # links
    create = Find(by=By.XPATH, value='//a[contains(text(),"Create")]')
    new_user = Find(by=By.XPATH, value='//a[contains(text(),"New user")]')
    new_role = Find(by=By.XPATH, value='//a[contains(text(),"New role")]')
    new_permission = Find(by=By.XPATH, value='//a[contains(text(),"New permission")]')

    def view_assignments(self):
        self.wait_for_loading()
        assignments_text = []
        assignments = \
            Finds(by=By.XPATH,
                  value='//ul[@class="select2-selection__rendered"]/li[@class="select2-selection__choice"]',
                  context=self)
        for assignment in assignments:
            text = assignment.text
            assignments_text.append(text)
        return assignments_text

    def add_assignment(self, assignment_value):
        self.assignments_seartch_field.send_keys(assignment_value)
        assignment = Find(value='.select2-results__option--highlighted', context=self)
        assignment.click()
        self.update.click()
        self._driver.refresh()

    def remove_assignment(self, assignment_value):
        remove_assignment_button = Find(by=By.XPATH, value='//li[contains(text(),"{}")]/span'.format(assignment_value),
                                        context=self)
        remove_assignment_button.click()
        self.update.click()
        self._driver.refresh()
