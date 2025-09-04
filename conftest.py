import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Optional for headless environments (like EC2/VPS)
    chrome_options.add_argument("--headless=new")

    # Create service from ChromeDriverManager
    service = Service(ChromeDriverManager().install())

    # Pass both service and options to Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
