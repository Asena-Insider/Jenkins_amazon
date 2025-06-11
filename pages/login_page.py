import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD_FIELD = (By.ID, "ap_password")

    def login(self, email, password):
        self.wait_for_element(self.EMAIL_FIELD).send_keys(email)
        self.wait_for_element(self.CONTINUE_BUTTON).click()
        time.sleep(5)
        self.wait_for_element(self.PASSWORD_FIELD).send_keys(password)
        self.wait_for_element(self.PASSWORD_FIELD).send_keys(Keys.RETURN)
