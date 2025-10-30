import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')
    _driver = webdriver.Edge(options=options)
    _driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager")
    yield _driver
    _driver.quit()
