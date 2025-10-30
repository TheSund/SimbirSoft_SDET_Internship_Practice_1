import allure
from selenium.webdriver.common.alert import Alert
from pages.add_customer_page import AddCustomerPage
from pages.customers_page import CustomersPage
from utils.customer_generators import CustomerGenerator
from utils.data_utils import DataUtils


@allure.parent_suite('XYZ Bank Testing')
@allure.suite('Customers List Testing')
class TestRun:

    @allure.title('Adding a customer')
    def test_1(self, driver):
        page = AddCustomerPage(driver)

        post_code = CustomerGenerator.generate_post_code()
        first_name = CustomerGenerator.generate_first_name(post_code)
        last_name = CustomerGenerator.generate_last_name(first_name)

        page.open_add_customer_tab()
        page.add_customer(first_name, last_name, post_code)

        alert = Alert(driver)
        assert alert.text[0:46] == 'Customer added successfully with customer id :', 'Клиент не был добавлен'
        alert.accept()

    @allure.title('Sorting customers list by First Name')
    def test_2(self, driver):
        page = CustomersPage(driver)

        page.open_customers_tab()
        for _ in range(2):
            page.sort_by_column('first_name')
            first_names = page.get_column_values('first_name')
            if first_names == sorted(first_names):
                break
        assert first_names == sorted(first_names), 'Список First Name не отсортирован по возрастанию'

    @allure.title('Deleting a customer')
    def test_3(self, driver):
        page = CustomersPage(driver)

        page.open_customers_tab()
        names = page.get_column_values('first_name')
        target_name = DataUtils.get_value_closest_to_avg_by_len(names)
        page.delete_customer(target_name)

        remaining_names = page.get_column_values('first_name')
        assert target_name not in remaining_names, f'Клиент {target_name} не был удалён'