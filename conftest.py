import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope="module")
def driver():
    options = Options()
    driver = webdriver.Edge()
    driver.get("https://practice-automation.com/form-fields/")
    yield driver
    driver.quit()
