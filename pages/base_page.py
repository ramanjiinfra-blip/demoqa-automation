# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("""
            let ad = document.getElementById("google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0");
            if (ad) ad.remove();
        """)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
