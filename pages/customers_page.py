from selenium.webdriver.common.by import By
from helpers.base_page import BasePage
from conftest import driver


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=5)

        self.customers_tab_button = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')
        self.table_rows = (By.CSS_SELECTOR, "table tbody tr")
        self.column_headers = {
            "first_name": (By.XPATH, "//td/a[contains(text(),'First Name')]"),
            "last_name": (By.XPATH, "//td/a[contains(text(),'Last Name')]"),
            "post_code": (By.XPATH, "//td/a[contains(text(),'Post Code')]"),
            "account_number": (By.XPATH, "//td[contains(text(),'Account Number')]"),
            "delete_customer": (By.XPATH, "//td[contains(text(),'Delete Customer')]"),
        }

    def open_customers_tab(self):
        self.find_element(*self.customers_tab_button).click()

    def sort_by_column(self, column: str):
        if column not in self.column_headers:
            raise ValueError(f"Unknown column: {column}")
        self.find_element(*self.column_headers[column]).click()

    def get_column_values(self, column: str) -> list[str]:
        column_index = list(self.column_headers.keys()).index(column) + 1
        values = []
        for row in self.find_elements(*self.table_rows):
            value = row.find_element(By.XPATH, f"./td[{column_index}]").text
            values.append(value)
        return values

    def delete_customer_closest_to_avg(self):
        rows = self.find_elements(*self.table_rows)
        names = self.get_column_values('first_name')

        lengths = [len(name) for name in names]
        avg_length = sum(lengths)/len(lengths)
        target_name = min(names, key=lambda n: abs(len(n) - avg_length))

        for row in rows:
            name = row.find_element(By.XPATH, "./td[1]").text
            if name == target_name:
                delete_button = row.find_element(By.XPATH, ".//button[contains(text(), 'Delete')]")
                delete_button.click()
                return target_name

        raise AssertionError(f"Клиент {target_name} не найден в таблице")