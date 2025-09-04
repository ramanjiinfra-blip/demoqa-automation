from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class WebTablesPage(BasePage):
    ADD_NEW_RECORD_BUTTON = (By.ID, "addNewRecordButton")
    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    EMAIL_FIELD = (By.ID, "userEmail")
    AGE_FIELD = (By.ID, "age")
    SALARY_FIELD = (By.ID, "salary")
    DEPARTMENT_FIELD = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")

    URL = "https://demoqa.com/webtables"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def add_user(self, first_name, last_name, email, age, salary, department):
        # Wait for possible ad iframe overlay to disappear (adjust selector if needed)
        try:
            self.wait.until(EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "iframe[id^='google_ads_iframe']")))
        except TimeoutException:
            # If not gone after waiting, proceed anyway or handle differently
            pass

        # Wait until the Add New Record button is clickable
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_NEW_RECORD_BUTTON))
        # Scroll the button into view to avoid overlays
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        # Click the button
        add_button.click()

        # Fill out the form fields
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.AGE_FIELD).send_keys(age)
        self.driver.find_element(*self.SALARY_FIELD).send_keys(salary)
        self.driver.find_element(*self.DEPARTMENT_FIELD).send_keys(department)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
