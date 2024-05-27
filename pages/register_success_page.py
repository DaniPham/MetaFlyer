from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from data.locators import RegisterPageLocators

class RegisterSuccesssPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.locator = RegisterPageLocators
        
    def get_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.TITLE))
        return element.text
        
        