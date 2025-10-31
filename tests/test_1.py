import allure
from selenium.webdriver.common.alert import Alert
from pages.add_customer_page import AddCustomerPage
from utils.customer_generators import CustomerGenerator

@allure.parent_suite('XYZ Bank Testing')
@allure.suite('Customers List Testing')
@allure.title('Adding a customer')
def test_1(driver):
    page = AddCustomerPage(driver)

    post_code = CustomerGenerator.generate_post_code()
    first_name = CustomerGenerator.generate_first_name(post_code)
    last_name = CustomerGenerator.generate_last_name(first_name)

    page.open_add_customer_tab()
    page.add_customer(first_name, last_name, post_code)

    alert = Alert(driver)
    assert alert.text[0:46] == 'Customer added successfully with customer id :', 'Клиент не был добавлен'
    alert.accept()