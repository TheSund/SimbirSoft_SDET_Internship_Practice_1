import allure
from selenium.webdriver.common.by import By
from helpers.base_page import BasePage
from conftest import driver


class AddCustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=5)

        self.add_customer_tab_button = (By.CSS_SELECTOR, 'button[ng-class="btnClass1"]')
        self.first_name = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
        self.last_name = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
        self.post_code = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
        self.submit_btn = (By.CSS_SELECTOR, 'button[type="submit"]')

    @allure.step('Открытие вкладки "Add Customer"')
    def open_add_customer_tab(self):
        self.find_element(*self.add_customer_tab_button).click()

    @allure.step('Добавление клиента с индексом {post_code}, именем {first_name} и фамилией {last_name}')
    def add_customer(self, first_name:str, last_name: str, post_code: str) -> None:
        self.find_element(*self.first_name).send_keys(first_name)
        self.find_element(*self.last_name).send_keys(last_name)
        self.find_element(*self.post_code).send_keys(post_code)
        self.find_element(*self.submit_btn).click()