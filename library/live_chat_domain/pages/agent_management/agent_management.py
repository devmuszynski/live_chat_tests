from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text


class AgentManagement:
    ADD = (By.XPATH, xpath_to_text("Add", tag="button", exact_match=True))
    INVITE_AGENTS_DIRECT = (By.XPATH, xpath_to_text("Invite Agents", tag="td/span", exact_match=True))
    INACTIVE_GROUPS_SECTION = (By.XPATH, "//*[@id='agents-new']//a[@href='/agents/groups']")
    ACTIVE_GROUPS_SECTION = (By.XPATH, "//*[@id='groups-new']//a[@href='/agents/groups']")

    def __init__(self, driver):
        self.driver = driver

    def click_add_button(self):
        self.driver.click_with_timeout(self.ADD)

    def click_invite_agents_direct(self):
        self.driver.click_with_timeout(self.INVITE_AGENTS_DIRECT)

    def go_to_groups_section(self):
        self.driver.click_with_timeout(self.INACTIVE_GROUPS_SECTION)
