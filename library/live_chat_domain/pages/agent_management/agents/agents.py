from selenium.webdriver.common.by import By
from .. import agent_management


class Agents(agent_management.AgentManagement):

    AGENTS_TABLE = (By.XPATH, "//tbody[.//text()='Invite Agents']")
    NAME_COLUMN = "td[2]"
    ROLE_COLUMN = "td[4]"

    SELECT_USER__FORMAT = (By.XPATH, "//tbody/tr[./td[2]//text()='{}']")
    EDIT_USER = (By.XPATH, "//a[contains(@href, 'agents/edit')]")

    def select_user(self, email):
        self.driver.click_with_timeout(self.__get_formatted_xpath_locator(self.SELECT_USER__FORMAT, email))

    def click_edit_user(self):
        self.driver.click_with_timeout(self.EDIT_USER)

    def get_agents_data(self):
        table = self.__get_agents_table()
        rows = self.__get_agents_rows(table)
        agents = []
        for row in rows:
            agent = {
                "name": self.__get_agent_name(row),
                "email": self.__get_agent_email(row),
                "role": self.__get_agent_role(row)
            }
            agents.append(agent)
        return agents

    def get_agents_emails(self):
        table = self.__get_agents_table()
        rows = self.__get_agents_rows(table)
        agents = []
        for row in rows:
            agents.append(self.__get_agent_email(row))
        return agents

    def __get_agents_table(self):
        return self.driver.wait_for_visible(self.AGENTS_TABLE)

    @staticmethod
    def __get_agents_rows(agents_table):
        """First row is to add agents, others are their data"""
        all_rows = agents_table.find_elements_by_xpath("tr")
        return all_rows[1:]

    def __get_agent_name(self, agent_row):
        return agent_row.find_element_by_xpath(f"{self.NAME_COLUMN}/div[1]").text

    def __get_agent_email(self, agent_row):
        return agent_row.find_element_by_xpath(f"{self.NAME_COLUMN}/div[2]").text

    def __get_agent_role(self, agent_row):
        return agent_row.find_element_by_xpath(f"{self.ROLE_COLUMN}/div[1]").text

    @staticmethod
    def __get_formatted_xpath_locator(xpath, formatter):
        """
        Uses xpath tuple with placeholder to be filled in by formatter
        """
        return tuple((xpath[0], xpath[1].format(formatter)))