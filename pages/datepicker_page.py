from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DatePickerPage(BasePage):
    URL = "https://demoqa.com/date-picker"
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")

    def set_date(self, date_str):
        self.open(self.URL)
        date_input = self.driver.find_element(*self.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date_str)
        date_input.send_keys("\n")
