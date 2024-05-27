from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from data.locators import IndividualRegisterPageLocators

class IndividualRegisterPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.locator = IndividualRegisterPageLocators
        
    def get_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.TITLE))
        return element.text
    
    def input_name(self, name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.NAME_INPUT))
        element.send_keys(name)
        
    def input_id(self, id):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.ID_INPUT))
        element.send_keys(id)
        
    def check_email(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.CHECK_EMAIL_BUTTON))
        element.click()
        
    def input_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.PASSWORD_INPUT))
        element.send_keys(password)
        
    def input_password_verify(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.PASSWORD_VERIFY_INPUT))
        element.send_keys(password)
        
    def input_email(self, email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.EMAIL_INPUT))
        element.send_keys(email)
        
    def input_phone(self, phone):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.PHONE_INPUT))
        element.send_keys(phone)
        
    def check_term_1(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.TERM_1_LABEL))
        element.click()
        
    def check_term_2(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.TERM_2_LABEL))
        element.click()
        
    def check_term_3(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.TERM_3_LABEL))
        element.click()
        
    def check_term_4(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.TERM_4_LABEL))
        element.click()
        
    def click_back(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.BACK_BUTTON))
        element.click()
    
    def click_submit(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(IndividualRegisterPageLocators.SUBMIT_BUTTON))
        element.click()
        
        
        
