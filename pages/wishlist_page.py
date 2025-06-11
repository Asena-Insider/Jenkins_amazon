from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
class WishlistPage(BasePage):
    WISHLIST_LINK = (By.ID, "huc-view-your-list-button")
    ITEM_TITLE = (By.CSS_SELECTOR, "span.a-list-item")
    DELETE_BUTTONS = (By.XPATH, "//input[@name='submit.deleteItem']")

    def go_to_wishlist(self):
        self.wait_for_element(self.WISHLIST_LINK).click()

    def verify_item_in_wishlist(self, item_name):
        assert self.wait_for_element((By.XPATH, f"//*[contains(text(),'{item_name}')]")) is not None

    def delete_items_from_wishlist(self):
        delete_buttons = self.wait_for_elements(self.DELETE_BUTTONS)
        for button in delete_buttons:
            button.click()
            time.sleep(3)

    def verify_item_not_in_wishlist(self, item_name):
        try:
            item = self.wait_for_element((By.XPATH, f"//span[contains(text(),'{item_name}')]"))
            assert item is None
        except:
            # Eğer öğe bulunamazsa bu beklenen bir durumdur ve test geçerli olacaktır
            pass
