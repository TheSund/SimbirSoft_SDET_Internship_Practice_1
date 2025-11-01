import allure
import pytest

from pages.customers_page import CustomersPage

@allure.parent_suite('XYZ Bank Testing')
@allure.suite('Customers List Testing')
@allure.title('Sorting customers list by First Name')
@pytest.mark.order(2)
def test_sorting_by_first_name(driver):
    page = CustomersPage(driver)

    page.open_customers_tab()
    page.sort_by_column('first_name')
    sort_result = page.get_column_values('first_name')
    # Если сортировка по возрастанию - проверить сортировку по убыванию
    if sort_result == sorted(sort_result):
        page.sort_by_column('first_name')
        sort_result = page.get_column_values('first_name')
        assert sort_result == sorted(sort_result, reverse=True), 'Сортировка не сработала (возрастание -> убывание)'
    # Если сортировка по убыванию - проверить сортировку по возрастанию, либо сортировка не работает
    else:
        page.sort_by_column('first_name')
        sort_result = page.get_column_values('first_name')
        assert sort_result == sorted(sort_result), 'Сортировка не сработала (убывание -> возрастание)'
