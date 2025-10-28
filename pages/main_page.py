from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    NAME_FIELD = (By.ID, "name-input") # Text field "Name" (required)
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']") # Text field "Password"
    EMAIL_FIELD = (By.ID, "email") # Text field "Email"
    MESSAGE_AREA = (By.ID, "message") # Text area "Message"
    SUBMIT_BUTTON = (By.ID, "submit-btn") # "Submit" button
    # Checkbox inputs "What is your favorite drink?"
    FAV_DRINK_CHECKBOXES = {
        "Water": (By.ID, "drink1"),
        "Milk": (By.ID, "drink2"),
        "Coffee": (By.ID, "drink3"),
        "Wine": (By.ID, "drink4"),
        "Ctrl-Alt-Delight": (By.ID, "drink5")
    }
    # Radio inputs "What is your favorite color?"
    FAV_COLOR_RADIO_BUTTONS = {
        "Red": (By.ID, "color1"),
        "Blue": (By.ID, "color2"),
        "Yellow": (By.ID, "color3"),
        "Green": (By.ID, "color4"),
        "#FFC0CB": (By.ID, "color5")
    }
    AUTOMATION_SELECT = (By.XPATH, "//select[@name='automation']") # Select dropdown "Do you like automation?"
    TOOLS_LIST = (By.XPATH,"//ul[li[text()='Selenium'] and li[text()='Playwright']]")
    # Filling the form with data
    def fill_form(self, name, password, email, message, drink, color, automation):
        self.send_keys(*self.NAME_FIELD, name)
        self.send_keys(*self.PASSWORD_FIELD, password)
        self.select_fav_drinks(drink)
        self.select_fav_color(color)
        self.select_automation(automation)
        self.send_keys(*self.EMAIL_FIELD, email)
        self.send_keys(*self.MESSAGE_AREA, message)

    # Selecting "What is your favorite drink?" checkboxes
    def select_fav_drinks(self, drinks):
        if len(drinks) > 0:
            if isinstance(drinks, str):
                drinks = [drinks]
            for drink in drinks:
                if drink in self.FAV_DRINK_CHECKBOXES:
                    self.click(*self.FAV_DRINK_CHECKBOXES[drink])

    # Selecting "What is your favorite color?" radio options
    def select_fav_color(self, color):
        if len(color) > 0:
            self.click(*self.FAV_COLOR_RADIO_BUTTONS[color])

    # Selecting "Do you like automation?" dropdown options
    def select_automation(self, value):
        select_element = self.wait_for_element(*self.AUTOMATION_SELECT)
        dropdown = Select(select_element)
        dropdown.select_by_visible_text(value)

    # Clicking "Submit" button to submit the form
    def submit_form(self):
        self.click(*self.SUBMIT_BUTTON)
    # Getting the count of tools in "Automation tools" and the longest tool
    def get_longest_tools_list(self):
        ul_element = self.wait_for_element(*self.TOOLS_LIST)
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        count = len(li_elements)
        max_item = max(li_elements, key=lambda el: len(el.text))
        result = (f"Количество инструментов в списке Automation tools: {count}\n"
                f"Инструмент с наибольшим количеством символов: {max_item.text.strip()}")
        return result