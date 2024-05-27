import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest

class TestLogin(BaseTest):
    
    @pytest.fixture()
    def load_pages(self):
        self.page = LoginPage(self.driver, self.wait)
        self.page.go_to_page()
        
    def test_login(self, load_pages):
        self.page.input_id("a1234")
        self.page.input_password("Password@123")
        self.page.click_login()
        #assert login success
        
    def test_login_incorrect_id(self, load_pages):
        self.page.input_id("a12345")
        self.page.input_password("Password@123")
        self.page.click_login()
        #assert login failed
        
    def test_login_incorrect_password(self, load_pages):
        self.page.input_id("a1234")
        self.page.input_password("Password@1234")
        self.page.click_login()
        #assert login failed
        
        