from decimal import Decimal

from selenium.webdriver.common.by import By
from webium import BasePage as WebiumBasePage, Finds, Find


class InventoryMixin(WebiumBasePage):
    record_xpath2 = '//div[@id="inventoryContent"]/div/table/tbody/tr[@data-key]'
    column_xpath2 = '//div[@id="inventoryContent"]/div/table/tbody/tr[@data-key="{}"]/td[{}]'
   # column_links_xpath = '//div[@data-key="{}"]/div/div[@title]'
    records2 = Finds(by=By.XPATH, value=record_xpath2)

    def _get_data_keys2(self):
        return [u.get_attribute('data-key') for u in self.records2 if int(u.get_attribute('data-key')) > 0]

    def _get_record_column_value2(self, data_key, column_name, columns_map):
        column_num = next((c_num for c_num, c_name in columns_map.items() if c_name == column_name), None)

        if column_name == 'data_key':
            return data_key

        elif column_name == 'impressions_total':
            column_xpath = self.column_xpath2.format(data_key, column_num)
            if Find(by=By.XPATH, value=column_xpath, context=self).text == '(not set)':
                return ''
            else:
                return int(Find(by=By.XPATH, value=column_xpath, context=self).text.replace(',', ''))
        elif column_name == 'value_total':
            column_xpath = self.column_xpath2.format(data_key, column_num)
            if Find(by=By.XPATH, value=column_xpath, context=self).text == '(not set)':
                return ''
            else:
                return Decimal(
                    Find(by=By.XPATH, value=column_xpath, context=self).text.replace('$', '').replace(',', ''))
        elif column_name == 'inventory_title':
            column_xpath = self.column_xpath2.format(data_key, column_num)
            if Find(by=By.XPATH, value=column_xpath, context=self).text == '(not set)':
                return ''
            else:
                return Find(by=By.XPATH, value=column_xpath, context=self).text.lower()
        elif column_name == 'opportunity_activation':
            column_xpath = self.column_xpath2.format(data_key, column_num)
            if Find(by=By.XPATH, value=column_xpath, context=self).text == '(not set)':
                return ''
            else:
                return int(Find(by=By.XPATH, value=column_xpath, context=self).text)
        elif column_name == 'vpm_total':
            column_xpath = self.column_xpath2.format(data_key, column_num)
            if Find(by=By.XPATH, value=column_xpath, context=self).text == '(not set)':
                return ''
            else:
                return Decimal(
                    Find(by=By.XPATH, value=column_xpath, context=self).text.replace('$', '').replace(',', ''))
        elif column_name == 'inventory_item_views':
            column_xpath = self.column_xpath2.format(data_key, column_num)
            if Find(by=By.XPATH, value=column_xpath, context=self).text == '(not set)':
                return ''
            else:
                return float(Find(by=By.XPATH, value=column_xpath, context=self).text.replace(',', ''))
        else:
            column_xpath = self.column_xpath2.format(data_key, column_num)
            if Find(by=By.XPATH, value=column_xpath, context=self).text == '(not set)':
                return ''
            else:
                return Find(by=By.XPATH, value=column_xpath, context=self).text

    def get_table_records_for_item(self, columns_map):
        records = [
            {
                column_name: self._get_record_column_value2(data_key, column_name, columns_map)
                for column_name in columns_map.values()
                }
            for data_key in self._get_data_keys2()
            ]

        return records
