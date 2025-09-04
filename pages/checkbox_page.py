# pages/checkbox_page.py

from pages.base_page import BasePage  # or correct import if structure differs

class CheckboxPage(BasePage):
    URL = "https://demoqa.com/checkbox"
    CLASSIFIED = ("css selector", "span.rct-title")

    def click_home_checkbox(self):
        self.open(self.URL)
        self.click(self.CLASSIFIED)
