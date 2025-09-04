from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UploadPage(BasePage):
    URL = "https://demoqa.com/upload-download"
    UPLOAD_INPUT = (By.ID, "uploadFile")

    def upload_file(self, filepath):
        self.open(self.URL)
        self.driver.find_element(*self.UPLOAD_INPUT).send_keys(filepath)
