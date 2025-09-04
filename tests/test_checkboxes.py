from pages.checkbox_page import CheckboxPage

def test_check_checkbox(driver):
    page = CheckboxPage(driver)
    page.click_home_checkbox()
    driver.save_screenshot("screenshots/test_result.png")
