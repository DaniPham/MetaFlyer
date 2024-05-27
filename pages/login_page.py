from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from data.locators import LoginPageLocators

class LoginPage(BasePage):
        
        def __init__(self, driver, wait):
            super().__init__(driver, wait)
            self.url = "https://www.metaflyer.io/login"
            self.locator = LoginPageLocators
            
        def go_to_page(self):
            return super().go_to_page(self.url)
            
        def get_title(self):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(LoginPageLocators.TITLE))
            return element.text
        
        def input_id(self, id):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(LoginPageLocators.ID_INPUT))
            element.send_keys(id)
            
        def input_password(self, password):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
            element.send_keys(password)
            
        def click_login(self):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
            element.click()
            
        def click_forgot_id(self):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(LoginPageLocators.FORGOT_ID))
            element.click()
            
        def click_reset_password(self):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(LoginPageLocators.RESET_PASSWORD))
            element.click()
            
        def click_register(self):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(LoginPageLocators.REGISTER_LINK))
            element.click()
        