from library.live_chat_domain.pages.login import LoginPage
from library.live_chat_domain.pages.install_code import InstallCodePage

from library.live_chat_domain.pages.join_by_link import JoinByLink

from library.live_chat_domain.interface.agent_management import AgentManagement


class selenium_live_chat(AgentManagement):

    def __init__(self, driver):
        super(selenium_live_chat, self).__init__(driver)

    def login(self, address, email, password):
        LoginPage(self.driver).login(address, email, password)

    def skip_livechat_instalation(self):
        InstallCodePage(self.driver).skip_instalation()

    def join_by_link(self, link, email, name, password):
        page = JoinByLink(self.driver)
        page.join(link, email, name, password)

    def close(self):
        self.driver.close()
