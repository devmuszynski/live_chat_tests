from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text


class DeleteModal:

    ACCEPT_DELETE = (By.XPATH, xpath_to_text("Delete", exact_match=True))

    def __init__(self, driver):
        self.driver = driver

    def accept_deletion(self):
        self.driver.click_with_timeout(self.ACCEPT_DELETE)