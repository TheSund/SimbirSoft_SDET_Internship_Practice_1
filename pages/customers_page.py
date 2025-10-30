import allure
from selenium.webdriver.common.by import By
from helpers.base_page import BasePage
from conftest import driver


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=5)

        self.customers_tab_button = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')
        self.table_rows = (By.CSS_SELECTOR, "table tbody tr")
        self.column_headers = {
            "first_name": (By.XPATH, '//td/a[contains(text(),"First Name")]'),
            "last_name": (By.XPATH, '//td/a[contains(text(),"Last Name"")]'),
            "post_code": (By.XPATH, '//td/a[contains(text(),"Post Code")]'),
            "account_number": (By.XPATH, '//td[contains(text(),"Account Number")]'),
            "delete_customer": (By.XPATH, '//td[contains(text(),"Delete Customer")]'),
        }

    @allure.step('Открытие вкладки "Customers"')
    def open_customers_tab(self):
        self.find_element(*self.customers_tab_button).click()

    @allure.step('Сортировка таблицы по столбцу {column}')
    def sort_by_column(self, column: str):
        if column not in self.column_headers:
            raise ValueError(f'Unknown column: {column}')
        self.find_element(*self.column_headers[column]).click()

    @allure.step('Получение данных из столбца {column}')
    def get_column_values(self, column: str) -> list[str]:
        column_index = list(self.column_headers.keys()).index(column) + 1
        return [row.find_element(By.XPATH, f'./td[{column_index}]').text for row in self.find_elements(*self.table_rows)]

    @allure.step('Удаление из таблицы клиента {customer}')
    def delete_customer(self, customer: str) -> str:
        rows = self.find_elements(*self.table_rows)

        for row in rows:
            name = row.find_element(By.XPATH, "./td[1]").text
            if name == customer:
                delete_button = row.find_element(By.XPATH, ".//button[contains(text(), 'Delete')]")
                delete_button.click()
                return customer
        raise AssertionError(f"Клиент {customer} не найден в таблице")