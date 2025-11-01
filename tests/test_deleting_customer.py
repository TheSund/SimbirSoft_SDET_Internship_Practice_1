import allure
import pytest

from pages.customers_page import CustomersPage
from utils.data_utils import DataUtils


@allure.parent_suite('XYZ Bank Testing')
@allure.suite('Customers List Testing')
@allure.title('Deleting a customer')
@pytest.mark.order(3)
def test_deleting_customer(driver):
    page = CustomersPage(driver)

    page.open_customers_tab()
    names = page.get_column_values('first_name')
    target_name = DataUtils.get_value_closest_to_avg_by_len(names)
    page.delete_customer(target_name)

    remaining_names = page.get_column_values('first_name')
    assert target_name not in remaining_names, f'Клиент {target_name} не был удалён'
