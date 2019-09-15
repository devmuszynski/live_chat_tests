from ..pages import agent_management
from time import sleep


class AgentManagement:

    def __init__(self, driver):
        self.driver = driver

        self.__main = agent_management.agents.Agents(self.driver)
        self.__edit = agent_management.agents.edit.Edit(self.driver)
        self.__delete = agent_management.agents.edit.delete_modal.DeleteModal(self.driver)

        self.__add_context = agent_management.add_context.AddContext(self.driver)
        self.__invite_modal = agent_management.add_context.invite_modal.InviteModal(self.driver)
        self.__invitations_sent = agent_management.add_context.invite_modal.invitations_sent_modal\
            .InvitationsSentModal(self.driver)

        self.__share_link_modal = agent_management.add_context.share_link_modal.ShareLinkModal(self.driver)

    def delete_agent(self, email):
        self.__main.select_user(email)
        self.__main.click_edit_user()
        self.__edit.click_delete_agent()
        self.__delete.accept_deletion()

    def change_user_permission(self, email, permission):
        self.__main.select_user(email)
        self.__main.click_edit_user()
        if permission == "Agent":
            self.__edit.set_agent_permission()
        elif permission == "Admin":
            self.__edit.set_admin_permission()
        else:
            raise InvalidPermission
        self.__edit.accept_changes()

    def get_agents_data(self):
        return self.__main.get_agents_data()

    def get_agents_emails(self):
        return self.__main.get_agents_emails()

    def send_invitations_to_agents(self, email_role_dicts):
        self.__main.click_add_button()
        self.__add_context.click_invite_agents_on_add_section()
        self.__invite_modal.assure_number_of_invite_fields(len(email_role_dicts))
        for i, (email, role) in enumerate(email_role_dicts.items()):
            self.__invite_modal.fill_email_box(i, email)
            self.__invite_modal.click_roles_box(i)
            self.__invite_modal.select_role(role, i)
        sleep(2)    # please be sane
        self.__invite_modal.click_send_invitations()
        self.__invitations_sent.click_done()

    def get_join_link(self):
        self.__main.click_add_button()
        self.__add_context.click_share_invite_link()
        join_link = self.__share_link_modal.get_join_link()
        self.__share_link_modal.close_modal()
        return join_link


class InvalidPermission(Exception):
    pass
