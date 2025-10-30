from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''

    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    def get_current_url(self) -> str:
        return self.driver.current_url