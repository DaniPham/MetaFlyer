import pytest
from pages.register_page import RegisterPage
from pages.individual_register_page import IndividualRegisterPage
from pages.company_register_page import CompanyRegisterPage
from pages.register_success_page import RegisterSuccessPage
from tests.base_test import BaseTest
import time

class TestRegister(BaseTest):
    
    @pytest.fixture()
    def load_pages(self):
        self.page = RegisterPage(self.driver, self.wait)
        self.page.go_to_page()
        
    def individual_register(self, load_pages):
        self.page.select_individual()
        self.page = IndividualRegisterPage(self.driver, self.wait)
        self.page.input_name("John Doe")
        self.page.input_id("a12345")
        self.page.check_email()
        self.page.input_password("Password@123")
        self.page.input_password_verify("Password@123")
        self.page.input_email("johndoe@gmail.com")
        self.page.input_phone("1234567890")
        self.page.check_term_1()
        self.page.check_term_2()
        self.page.check_term_3()
        self.page.check_term_4()
        self.page.click_submit()
        self.page = RegisterSuccessPage(self.driver, self.wait)
        assert self.page.get_title() == "모모 회원가입 완료"
        
    def test_company_register(self, load_pages):
        self.page.select_company()
        self.page = CompanyRegisterPage(self.driver, self.wait)
        self.page.input_name("Jane Doe")
        self.page.input_id("b12345")
        self.page.check_email()
        self.page.input_password("Password@123")
        self.page.input_password_verify("Password@123")
        self.page.input_email("janedoe@gmail.com")
        self.page.input_phone("12345678901")
        self.page.select_company_type("개인사업자")
        self.page.input_company_name("Jane Doe Inc.")   
        self.page.input_ceo("Jane Doe")
        self.page.input_open_date()
        self.page.input_business_registration("1234567890123")
        self.page.check_term_1()
        self.page.check_term_2()
        self.page.check_term_3()
        self.page.check_term_4()
        self.page.click_submit()
        self.page = RegisterSuccessPage(self.driver, self.wait)
        assert self.page.get_title() == "모모 회원가입 완료"
        
        
        
        
        