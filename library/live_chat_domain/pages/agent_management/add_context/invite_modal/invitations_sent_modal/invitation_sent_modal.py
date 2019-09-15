from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text


class InvitationsSentModal:

    DONE = (By.XPATH, xpath_to_text("Done", exact_match=True, tag="button"))

    def __init__(self, driver):
        self.driver = driver

    def click_done(self):
        self.driver.click_with_timeout(self.DONE)