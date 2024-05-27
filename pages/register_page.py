from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from data.locators import RegisterPageLocators

class RegisterPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.url = "https://www.metaflyer.io/register"
        self.locator = RegisterPageLocators
        
    def go_to_page(self):
        return super().go_to_page(self.url)
        
    def get_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.driver.find_element(*RegisterPageLocators.TITLE)))
        return element.text
    
    def select_individual(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.INDIVIDUAL))
        element.click()
    
    def select_company(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.COMPANY))
        element.click()
