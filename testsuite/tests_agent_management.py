import unittest
from library.custom_webdrivers import ChromeDriver
from library.live_chat_domain.interface.interface import selenium_live_chat

my_mail = "devmuszynski@gmail.com"
my_pass = "dobrastronka"
login_addr = "https://my.labs.livechatinc.com/agents/devmuszynski%40gmail.com"


def go_to_agents_management_section(selenium):
    selenium.login(login_addr, my_mail, my_pass)
    try:
        selenium.skip_livechat_instalation()
    except TimeoutError:
        pass


class TestAddingAgentsTeardownDeletion(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium_live_chat(ChromeDriver())
        go_to_agents_management_section(self.selenium)
        self.new_agents = {
            "hej@elo.com": "Agent",
            "nope@nope.com": "Agent",
            "rodeo@hej.com": "Agent",
            "nope@very.com": "Admin"
        }
        self.selenium.send_invitations_to_agents(self.new_agents)

    def tearDown(self):
        self.selenium.close()

    def tearDownClass(self):
        """
        Deletes agents
        """
        for i in self.new_agents:
            self.selenium.delete_agent(i)

    def test_agents_added(self):
        """
        Checks if after adding agents they appear on list of agents
        """
        not_added = []

        added = self.selenium.get_agents_emails()
        for should_be_email in self.new_agents.keys():
            if should_be_email not in added:
                not_added.append(should_be_email)
        self.assertFalse(not_added, f"Users not added: {not_added}")

    def test_correct_roles(self):
        """
        Checks if after adding agents all that were added have expected roles
        """
        users_with_invalid_role = []

        agents = self.selenium.get_agents_data()
        for email, expected_role in self.new_agents.items():
            for agent in agents:
                if agent["email"] == email and agent["role"] != expected_role:
                    users_with_invalid_role.append({email: f"should be {expected_role}, but is {agent['role']}"})
        self.assertFalse(users_with_invalid_role, msg=users_with_invalid_role)


class TestJoinByLink(unittest.TestCase):

    def setUp(self):
        self.email = "new@urrrr.com"
        self.name = "Got here by link 2"
        self.password = "superstrongpass"

    def test_join_by_link(self):
        self.selenium = selenium_live_chat(ChromeDriver())
        go_to_agents_management_section(self.selenium)
        self.join_link = self.selenium.get_join_link()

        self.selenium.join_by_link(self.join_link, self.email, self.name, self.password)
        self.selenium.close()

        self.selenium = selenium_live_chat(ChromeDriver())
        go_to_agents_management_section(self.selenium)

        emails = self.selenium.get_agents_emails()
        self.assertIn(self.email, emails, "User not added")


class TestChangeUserPermission(unittest.TestCase):

    def setUp(self):
        self.email = "change@myperms.com"

        self.selenium = selenium_live_chat(ChromeDriver())
        go_to_agents_management_section(self.selenium)
        self.selenium.send_invitations_to_agents({self.email: "Agent"})

    def test_change_user_permissions(self):
        self.selenium.change_user_permission(self.email, "Admin")

    def tearDown(self):
        self.selenium.delete_agent(self.email)


if __name__ == "__main__":
    unittest.main()
