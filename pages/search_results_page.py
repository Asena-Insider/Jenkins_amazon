from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.SEARCH_BOX = (By.ID, "twotabsearchtextbox")
        self.SEARCH_RESULTS_TEXT = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
        self.NEXT_PAGE_BUTTON = (By.XPATH, "//a[text()='2']")
        self.CURRENT_PAGE_NUMBER = (By.CSS_SELECTOR, "span.s-pagination-item.s-pagination-selected")
        self.THIRD_PRODUCT = (By.XPATH, "(//h2[contains(@class,'a-size-base-plus')])[2]")

    def search_for(self, item):
        self.wait_for_element(self.SEARCH_BOX).send_keys(item)
        self.wait_for_element(self.SEARCH_BOX).send_keys(Keys.RETURN)

    def verify_search_results(self, text):
        result = self.wait_for_element(self.SEARCH_RESULTS_TEXT).text.lower()
        assert text in result

    def go_to_next_page(self):
        self.wait_and_click(self.NEXT_PAGE_BUTTON)

    def verify_on_page(self, page_number):
        current_page = self.wait_for_element(self.CURRENT_PAGE_NUMBER).text
        assert current_page == str(page_number)

    def click_third_product(self):
        self.wait_and_click(self.THIRD_PRODUCT)
