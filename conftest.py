import pytest
from selenium import webdriver

from data.constants import BASE_URL


@pytest.fixture()
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument('--enable-javascript')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    _driver = webdriver.Edge(options=options)
    _driver.get(BASE_URL)
    yield _driver
    _driver.quit()
