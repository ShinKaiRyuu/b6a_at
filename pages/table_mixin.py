from selenium.webdriver.common.by import By
from webium import BasePage as WebiumBasePage, Finds, Find


class TableMixin(WebiumBasePage):
    record_xpath = '//tr[@data-key]'
    column_xpath = '//tr[@data-key="{}"]/td[{}]'
    column_links_xpath = '//tr[@data-key="{}"]/td/a[@title]'
    records = Finds(by=By.XPATH, value=record_xpath)

    def _get_data_keys(self):
        return [u.get_attribute('data-key') for u in self.records]

    def _get_record_column_value(self, data_key, column_name, columns_map):
        column_num = next((c_num for c_num, c_name in columns_map.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'links':
            column_xpath = self.column_links_xpath.format(data_key)
            links = Finds(by=By.XPATH, value=column_xpath, context=self)
            return [
                {
                    link.get_attribute('title').lower(): link.get_attribute('href')
                }
                for link in links
                ]
        if column_name == 'order':
            column_xpath = self.column_xpath.format(data_key, column_num)
            return int(Find(by=By.XPATH, value=column_xpath, context=self).text)
        else:
            column_xpath = self.column_xpath.format(data_key, column_num)
            return Find(by=By.XPATH, value=column_xpath, context=self).text

    def get_table_records(self, columns_map):
        records = [
            {
                column_name: self._get_record_column_value(data_key, column_name, columns_map)
                for column_name in columns_map.values()
                }
            for data_key in self._get_data_keys()
            ]

        return records
