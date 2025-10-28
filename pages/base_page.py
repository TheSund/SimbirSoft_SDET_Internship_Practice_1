from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Initialization
    def __init__(self, driver):
        self.driver = driver

    # Waiting for an element to load
    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, value)))

    # Click an element
    def click(self, by, value):
        self.wait_for_element(by, value).click()

    # Send keys to a text based element
    def send_keys(self, by, value, text):
        self.wait_for_element(by, value).send_keys(text)