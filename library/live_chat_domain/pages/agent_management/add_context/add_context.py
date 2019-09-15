from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text
from .. import agent_management


class AddContext(agent_management.AgentManagement):

    INVITE_AGENTS_VIA_ADD = (By.XPATH, xpath_to_text("Invite Agents", exact_match=True))
    IMPORT_GSUITE = (By.XPATH, xpath_to_text("Import G Suite users", tag="button"))
    SHARE_INVITE = (By.XPATH, xpath_to_text("Share invite link", tag="button", exact_match=True))
    ADD_BOT = (By.XPATH, xpath_to_text("Add a bot", tag="a", exact_match=True))
    CREATE_GROUP = (By.XPATH, xpath_to_text("Create a group", tag="a", exact_match=True))

    def click_invite_agents_on_add_section(self):
        self.driver.click_with_timeout(self.INVITE_AGENTS_VIA_ADD)

    def click_import_gsuite_users(self):
        self.driver.click_with_timeout(self.IMPORT_GSUITE)

    def click_share_invite_link(self):
        self.driver.click_with_timeout(self.SHARE_INVITE)

    def click_add_bot(self):
        self.driver.click_with_timeout(self.ADD_BOT)

    def click_create_a_group(self):
        self.driver.click_with_timeout(self.CREATE_GROUP)