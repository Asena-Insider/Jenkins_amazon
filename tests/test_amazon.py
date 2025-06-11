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

        # Amazon ana sayfasına gidin
        home_page.open()

        def wait_for_page_title(driver, title):
            WebDriverWait(driver, 10).until(EC.title_contains(title)) #Bekleme süresi ekledim elementi bulamıyor.

        self.assertIn("Amazon", driver.title)

        # Login ekranını açın ve giriş yapın
        home_page.go_to_login_page()
        login_page.login('smettommer@gmail.com', '(smoss1905A)')

        # 'Samsung' araması yapın
        search_results_page.search_for('samsung')

        # Arama sonucunu doğrulayın
        search_results_page.verify_search_results('samsung')

        # 2. sayfaya geçin ve doğrulayın
        search_results_page.go_to_next_page()
        search_results_page.verify_on_page(2)

        # Üçüncü ürüne tıklayın
        search_results_page.click_third_product()

        # Ürünü istek listesine ekleyin
        product_page.add_to_list()

        # İstek listesine gidin ve ürünü doğrulayın
        wishlist_page.go_to_wishlist()
        driver.save_screenshot("wishlist_debug.png")  # Sayfa ekran görüntüsünü al çünkü yüklendiğinden emin değiliz locater bulamıyor teyit amaçlı ekledim.
        print("Sayfa başlığı:", driver.title)
        wishlist_page.verify_item_in_wishlist('Samsung') # Belki tam login olmamışsızdır ve Amazon tekrar ana sayfaya atıyordur. Bunu doğrulamak için eklendi.

        # Ürünü istek listesinden silin ve doğrulayın
        wishlist_page.delete_items_from_wishlist()
        wishlist_page.verify_item_not_in_wishlist('Samsung')
        print("Test başarıyla tamamlandı!")

if __name__ == "__main__":
    unittest.main()
