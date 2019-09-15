from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text


class InstallCodePage:

    SKIP = (By.XPATH, xpath_to_text("I'll do it later →", exact_match=True))

    def __init__(self, driver):
        self.driver = driver

    def skip_instalation(self):
        self.driver.click_with_timeout(self.SKIP)
