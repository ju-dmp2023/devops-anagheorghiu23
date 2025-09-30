from web.test_base import WebBase
from web.pages.login_page import LoginPage
from web.pages.calculator_page import CalculatorPage
from web.pages.register_page import RegisterPage
from playwright.sync_api import expect
import pytest
import random
import string

class TestWeb(WebBase):
    def test_login(self):
        LoginPage(self.page).login(username="admin",password="test1234")
        expect(CalculatorPage(self.page).element("username")).to_have_text("admin")

    def test_register(self):
        random_username = "user_" + ''.join(random.choices(string.ascii_lowercase, k=6))
        CalculatorPage(self.page).logout()
        LoginPage(self.page).register()
        # RegisterPage(self.page).registerinpage(username="user12", password="1234", password_again="1234")
        # expect(CalculatorPage(self.page).element("username")).to_have_text("user12")
        RegisterPage(self.page).registerinpage(username=random_username, password="1234", password_again="1234")
        expect(CalculatorPage(self.page).element("username")).to_have_text(random_username)
        # CalculatorPage(self.page).logout()

    def test_add(self):
        CalculatorPage(self.page).add()
        expect(CalculatorPage(self.page).element("results")).to_have_value("3")


    def test_add(self):
        CalculatorPage(self.page).subtract()
        expect(CalculatorPage(self.page).element("results")).to_have_value("1")
    
    def test_multiply(self):
        CalculatorPage(self.page).multiply()
        expect(CalculatorPage(self.page).element("results")).to_have_value("6")

    def test_divide(self):
        CalculatorPage(self.page).divide()
        expect(CalculatorPage(self.page).element("results")).to_have_value("2")

    def test_history(self):
        CalculatorPage(self.page).logout()
        LoginPage(self.page).login(username="admin",password="test1234")
        CalculatorPage(self.page).add()
        CalculatorPage(self.page).get_history()
        expect(CalculatorPage(self.page).element("history")).to_have_value("1+2=3\n")
        CalculatorPage(self.page).logout()
        