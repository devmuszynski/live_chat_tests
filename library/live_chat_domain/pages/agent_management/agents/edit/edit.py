from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text


class Edit:

    DELETE_AGENT = (By.XPATH, xpath_to_text("Delete agent.", tag="button"))
    AGENT_PERMISSION = (By.XPATH, "//label[.//@type='radio' and .//@name='permission' and .//@value='normal']")
    ADMIN_PERMISSION = (By.XPATH, "//label[.//@type='radio' and .//@name='permission' and .//@value='viceowner']")

    ACCEPT_CHANGES = (By.XPATH, xpath_to_text("Save changes", exact_match=True, tag="button"))

    def __init__(self, driver):
        self.driver = driver

    def click_delete_agent(self):
        self.driver.click_with_timeout_and_scroll(self.DELETE_AGENT)

    def set_agent_permission(self):
        self.driver.click_with_timeout_and_scroll(self.AGENT_PERMISSION)

    def set_admin_permission(self):
        self.driver.click_with_timeout_and_scroll(self.ADMIN_PERMISSION)

    def accept_changes(self):
        self.driver.click_with_timeout(self.ACCEPT_CHANGES)

    @staticmethod
    def __get_formatted_xpath_locator(xpath, formatter):
        """
        Uses xpath tuple with placeholder to be filled in by formatter
        """
        return tuple((xpath[0], xpath[1].format(formatter)))