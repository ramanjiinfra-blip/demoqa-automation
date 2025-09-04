from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DynamicPropsPage(BasePage):
    URL = "https://demoqa.com/dynamic-properties"
    ENABLE_AFTER = (By.ID, "enableAfter")
    COLOR_CHANGE = (By.ID, "colorChange")

    def validate_dynamic_properties(self):
        self.open(self.URL)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.ENABLE_AFTER))
        wait.until(EC.presence_of_element_located(self.COLOR_CHANGE))
