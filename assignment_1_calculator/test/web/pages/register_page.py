from playwright.sync_api import Page
from web.pages.page_base import PageBase

class RegisterPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#username",
            "password": "#password1",
            "password_again": "#password2",
            "register": "#register"
        })

    def registerinpage(self,username, password, password_again):
        self.element("username").fill(username)
        self.element("password").fill(password)
        self.element("password_again").fill(password_again)
        self.element("register").click()

