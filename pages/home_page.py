from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://www.amazon.com.tr"
        self.LOGIN_BUTTON = (By.ID, "nav-link-accountList")

    def open(self):
        self.driver.get(self.url)

    def go_to_login_page(self):
        self.wait_and_click(self.LOGIN_BUTTON)




