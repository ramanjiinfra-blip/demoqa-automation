from pages.upload_page import UploadPage
import os

def test_file_upload(driver):
    file_path = os.path.abspath("sample_file.txt")
    with open("sample_file.txt", "w") as f:
        f.write("This is a test file.")

    page = UploadPage(driver)
    page.upload_file(file_path)
    driver.save_screenshot("screenshots/test_result.png")
