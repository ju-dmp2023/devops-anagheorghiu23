from playwright.sync_api import Page
from web.pages.page_base import PageBase

class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#user-name",
            "logout": "#logout-button",
            "key_0":  "#key-0",
            "key_1":  "#key-1",
            "key_2":  "#key-2",
            "key_3":  "#key-3",
            "key_4":  "#key-4",
            "key_5":  "#key-5",
            "key_6":  "#key-6",
            "key_7":  "#key-7",
            "key_8":  "#key-8",
            "key_9":  "#key-9",
            "key_decimal":  "#key-decimal",
            "add":  "#key-add",
            "subtract":  "#key-subtract",
            "multiply":  "#key-multiply",
            "divide":  "#key-divide",
            "equal":  "#key-equals",
            "results":  "#calculator-screen",
            "clear":"#key-clear",
            "toggle_button": "#toggle-button",
            "history":"#history"
        })
    
    def logout(self):
        self.element("logout").click()

    def add (self):
        self.element("clear").click()
        self.element("key_1").click()
        self.element("add").click()
        self.element("key_2").click()
        self.element("equal").click()
  

    def subtract(self):
        self.element("clear").click()
        self.element("key_2").click()
        self.element("subtract").click()
        self.element("key_1").click()
        self.element("equal").click()
 
    
    def multiply(self):
        self.element("clear").click()
        self.element("key_2").click()
        self.element("multiply").click()
        self.element("key_3").click()
        self.element("equal").click()

    
    def divide(self):
        self.element("clear").click()
        self.element("key_4").click()
        self.element("divide").click()
        self.element("key_2").click()
        self.element("equal").click()

    def get_history(self):
        self.element("toggle_button").click()






