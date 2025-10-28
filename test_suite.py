import allure
import pytest
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

from conftest import driver
from pages.main_page import MainPage

# POSITIVE TESTS
@allure.parent_suite("Form Fields Testing")
@allure.suite("Positive tests")
@allure.title("Test 1 - Successful submission")
@allure.description("Correct operation of the form with valid values.")
def test_1(driver):
    driver.execute_script("document.body.style.zoom='50%'")
    form_page = MainPage(driver)
    form_page.fill_form(
        name="Sol Badguy",
        password="GG3RdREV2",
        email="sol@badguy.com",
        message=form_page.get_longest_tools_list(),
        drink=["Milk", "Coffee"],
        color="Yellow",
        automation="No"
    )
    form_page.submit_form()
    try:
        alert = Alert(driver)
        assert alert.text == "Message received!"
        alert.accept()
    except NoAlertPresentException:
        print("Submission failed - No message was received.")
        pytest.fail()
    driver.refresh()