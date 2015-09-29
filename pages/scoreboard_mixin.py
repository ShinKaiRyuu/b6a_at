from decimal import Decimal

from selenium.webdriver.common.by import By
from webium import BasePage as WebiumBasePage, Finds, Find


class ScoreboardMixin(WebiumBasePage):
    record_xpath = '//div[@data-key]'
    column_xpath = '//div[@data-key="{}"]/div/div[{}]'
    column_links_xpath = '//div[@data-key="{}"]/div/div[@title]'
    records = Finds(by=By.XPATH, value=record_xpath)

    def _get_data_keys(self):
        return [u.get_attribute('data-key') for u in self.records if int(u.get_attribute('data-key')) > 0]

    def _get_record_column_value(self, data_key, column_name, columns_map):
        column_num = next((c_num for c_num, c_name in columns_map.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'impressions_total':
            column_xpath = self.column_xpath.format(data_key, column_num)
            return int(Find(by=By.XPATH, value=column_xpath, context=self).text)
        elif column_name == 'value_total':
            column_xpath = self.column_xpath.format(data_key, column_num)
            return Decimal(Find(by=By.XPATH, value=column_xpath, context=self).text.replace('$', '').replace(',', ''))
        elif column_name == 'inventory_title':
            column_xpath = self.column_xpath.format(data_key, column_num)
            return Find(by=By.XPATH, value=column_xpath, context=self).text.lower()
        elif column_name == 'opportunity_activation':
            column_xpath = self.column_xpath.format(data_key, column_num)
            return int(Find(by=By.XPATH, value=column_xpath, context=self).text)
        elif column_name == 'vpm_total':
            column_xpath = self.column_xpath.format(data_key, column_num)
            return Decimal(Find(by=By.XPATH, value=column_xpath, context=self).text.replace('$', '').replace(',', ''))
        elif column_name == 'inventory_item_views':
            column_xpath = self.column_xpath.format(data_key, column_num)
            return float(Find(by=By.XPATH, value=column_xpath, context=self).text.replace(',', ''))
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
