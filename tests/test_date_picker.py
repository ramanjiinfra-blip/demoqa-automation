from pages.datepicker_page import DatePickerPage

def test_date_picker(driver):
    page = DatePickerPage(driver)
    page.set_date("09/04/2025")
    driver.save_screenshot("screenshots/test_result.png")
