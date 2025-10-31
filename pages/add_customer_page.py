import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.locators import (
    ADD_CUSTOMER_TAB,
    ADD_FIRST_NAME,
    ADD_LAST_NAME,
    ADD_POST_CODE,
    ADD_CUSTOMER_SUBMIT
)


class AddCustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=5)

        self.add_customer_tab_button = (By.CSS_SELECTOR, ADD_CUSTOMER_TAB)
        self.first_name = (By.CSS_SELECTOR, ADD_FIRST_NAME)
        self.last_name = (By.CSS_SELECTOR, ADD_LAST_NAME)
        self.post_code = (By.CSS_SELECTOR, ADD_POST_CODE)
        self.submit_btn = (By.CSS_SELECTOR, ADD_CUSTOMER_SUBMIT)

    @allure.step('Открытие вкладки "Add Customer"')
    def open_add_customer_tab(self):
        self.click(*self.add_customer_tab_button)

    @allure.step('Добавление клиента с индексом {post_code}, именем {first_name} и фамилией {last_name}')
    def add_customer(self, first_name:str, last_name: str, post_code: str) -> None:
        self.send_keys(*self.first_name, first_name)
        self.send_keys(*self.last_name,last_name)
        self.send_keys(*self.post_code,post_code)
        self.click(*self.submit_btn)