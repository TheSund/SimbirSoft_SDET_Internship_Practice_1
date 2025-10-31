import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.locators import (
    CUSTOMERS_TAB,
    CUSTOMERS_TABLE_ROWS,
    COL_FIRST_NAME,
    COL_LAST_NAME,
    COL_POST_CODE,
    COL_ACCOUNT_NUMBER,
    COL_DELETE_CUSTOMER
)


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=5)

        self.customers_tab_button = (By.CSS_SELECTOR, CUSTOMERS_TAB)
        self.table_rows = (By.CSS_SELECTOR, CUSTOMERS_TABLE_ROWS)
        self.column_headers = {
            "first_name": (By.XPATH, COL_FIRST_NAME),
            "last_name": (By.XPATH, COL_LAST_NAME),
            "post_code": (By.XPATH, COL_POST_CODE),
            "account_number": (By.XPATH, COL_ACCOUNT_NUMBER),
            "delete_customer": (By.XPATH, COL_DELETE_CUSTOMER),
        }

    @allure.step('Открытие вкладки "Customers"')
    def open_customers_tab(self):
        self.click(*self.customers_tab_button)

    @allure.step('Сортировка таблицы по столбцу {column}')
    def sort_by_column(self, column: str):
        if column not in self.column_headers:
            raise ValueError(f'Unknown column: {column}')
        self.click(*self.column_headers[column])

    @allure.step('Получение данных из столбца {column}')
    def get_column_values(self, column: str) -> list[str]:
        column_index = list(self.column_headers.keys()).index(column) + 1
        return [row.find_element(By.XPATH, f'./td[{column_index}]').text for row in self.find_elements(*self.table_rows)]

    @allure.step('Удаление из таблицы клиента {customer}')
    def delete_customer(self, customer: str) -> str:
        rows = self.find_elements(*self.table_rows)

        for row in rows:
            name = row.find_element(By.XPATH, './td[1]').text
            if name == customer:
                delete_button = row.find_element(By.XPATH, ".//button[contains(text(), 'Delete')]")
                delete_button.click()
                return customer
        raise AssertionError(f'Клиент {customer} не найден в таблице')