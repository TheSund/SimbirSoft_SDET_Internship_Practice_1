from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver, timeout=5):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    def click(self, by, value):
        self.find_element(by, value).click()

    def send_keys(self, by, value, text: str):
        self.find_element(by, value).send_keys(text)