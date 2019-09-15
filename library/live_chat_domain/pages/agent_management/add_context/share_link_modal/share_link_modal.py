from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text
from time import sleep


class ShareLinkModal:

    JOIN_LINK_STARTS_WITH = "https://accounts.labs.livechatinc.com/join/"

    JOIN_LINK = (By.XPATH, "//input[@readonly and @type='text']")
    COPY_LINK = (By.XPATH, xpath_to_text("Copy link", tag="button"))
    GENERATE_NEW_LINK = (By.XPATH, xpath_to_text("Generate a new one"))
    CLOSE_MODAL = (By.XPATH, "//*[@class='modal-portal-container']//button[@title='Close modal']")

    def __init__(self, driver):
        self.driver = driver

    def get_join_link(self):
        for i in range(6):
            join_link_obj = self.driver.wait_for_visible(self.JOIN_LINK)
            join_link = join_link_obj.get_attribute("value")
            if self.JOIN_LINK_STARTS_WITH not in join_link:
                sleep(0.5)
                continue
            else:
                return join_link
        else:
            raise AssertionError("Join link not available")

    def click_generate_new_link(self):
        self.driver.click_with_timeout(self.GENERATE_NEW_LINK)

    def close_modal(self):
        self.driver.click_with_timeout(self.CLOSE_MODAL)