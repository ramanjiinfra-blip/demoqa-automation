from pages.dynamic_props_page import DynamicPropsPage

def test_dynamic_buttons(driver):
    page = DynamicPropsPage(driver)
    page.validate_dynamic_properties()
    driver.save_screenshot("screenshots/test_result.png")
