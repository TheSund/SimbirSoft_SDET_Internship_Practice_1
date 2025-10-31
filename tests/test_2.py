import allure

from pages.customers_page import CustomersPage

@allure.parent_suite('XYZ Bank Testing')
@allure.suite('Customers List Testing')
@allure.title('Sorting customers list by First Name')
def test_2(driver):
    page = CustomersPage(driver)

    page.open_customers_tab()
    for _ in range(2):
        page.sort_by_column('first_name')
        first_names = page.get_column_values('first_name')
        if first_names == sorted(first_names):
            break
    assert first_names == sorted(first_names), 'Список First Name не отсортирован по возрастанию'
