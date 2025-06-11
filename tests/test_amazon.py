import unittest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        # Service nesnesini doğrudan kullanıyoruz
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_amazon_happy_path(self):
        driver = self.driver
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        search_results_page = SearchResultsPage(driver)
        product_page = ProductPage(driver)
        wishlist_page = WishlistPage(driver)

        # Amazon ana sayfasına gidin ana sayfada olduğunuzu doğrulayın. Assert ile
        home_page.open()

        def wait_for_page_title(driver, title):
            WebDriverWait(driver, 10).until(EC.title_contains(title)) #Bekleme süresi ekledim elementi bulamıyor.

        self.assertIn("Amazon", driver.title)



if __name__ == "__main__":
    unittest.main()

