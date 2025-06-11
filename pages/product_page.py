from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ADD_TO_LIST_BUTTON = (By.ID, "wishListMainButton")

    def add_to_list(self):
        self.wait_and_click(self.ADD_TO_LIST_BUTTON)
