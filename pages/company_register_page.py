from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from data.locators import CompanyRegisterPageLocators
from selenium.webdriver.common.by import By

class CompanyRegisterPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.locator = CompanyRegisterPageLocators
        
    def get_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.TITLE))
        return element.text
    
    def input_name(self, name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.NAME_INPUT))
        element.send_keys(name)
        
    def input_id(self, id):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.ID_INPUT))
        element.send_keys(id)
        
    def check_email(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.CHECK_EMAIL_BUTTON))
        element.click()
        
    def input_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.PASSWORD_INPUT))
        element.send_keys(password)
        
    def input_password_verify(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.PASSWORD_VERIFY_INPUT))
        element.send_keys(password)
        
    def input_email(self, email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.EMAIL_INPUT))
        element.send_keys(email)
        
    def input_phone(self, phone):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.PHONE_INPUT))
        element.send_keys(phone)
        
    def select_company_type(self, company_type):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.COMPANY_TYPE_SELECT))
        element.click()
        for option in self.driver.find_elements(*CompanyRegisterPageLocators.COMPANY_TYPE_OPTION):
            if option.text == company_type:
                option.click()
                break
            
    def input_company_name(self, company_name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.COMPANY_NAME_INPUT))
        element.send_keys(company_name)
        
    def input_ceo(self, ceo):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.COMPANY_CEO_INPUT))
        element.send_keys(ceo)
        
    def input_open_date(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.COMPANY_OPEN_DATE_INPUT))
        element.click()
        element_2 = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/div/form/div[10]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div")))
        element_2.click()
        
    def input_business_registration(self, business_registration):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.BUSINESS_REGISTRATION_INPUT))
        element.send_keys(business_registration)
        
    def check_term_1(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.TERM_1_LABEL))
        element.click()
    
    def check_term_2(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.TERM_2_LABEL))
        element.click()
        
    def check_term_3(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.TERM_3_LABEL))
        element.click()
        
    def check_term_4(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.TERM_4_LABEL))
        element.click()
        
    def click_back(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.BACK_BUTTON))
        element.click()
        
    def click_submit(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(CompanyRegisterPageLocators.SUBMIT_BUTTON))
        element.click()
            
        