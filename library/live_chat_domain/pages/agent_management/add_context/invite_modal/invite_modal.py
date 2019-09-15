from selenium.webdriver.common.by import By
from library.selenium_utils import xpath_to_text

from selenium.common.exceptions import TimeoutException


class InviteModal:

    INVITE_ANOTHER = (By.XPATH, xpath_to_text("Invite another"))
    SEND_INVITATIONS = (By.XPATH, "//button[@type='submit']")

    INVALID_EMAIL = (By.XPATH, "//*[@class='field-error'][contains(text(), 'Please provide a valid email address')])")

    ROLE_INPUT_BOX = (By.XPATH, "//input[@name='select-box-input']")

    SELECT_ROLE_BOXES = (By.XPATH, "//div[@class='selected-item']")
    SELECT_ROLE_OPTIONS__FORMAT = (By.XPATH, "//li[./div/span[text()='{}']]")
    SELECT_GROUP_OPTIONS__FORMAT = (By.XPATH, "//li[./div/span[text()='{}']]")

    INPUT_GROUP = (By.XPATH, "//input[contains(@name, 'multiselectbox')]")

    EMAIL_BOX__FORMAT = (By.ID, "email-{}")

    def __init__(self, driver):
        self.driver = driver

    def assure_number_of_invite_fields(self, num):
        base_num_of_fields = 3
        if num > base_num_of_fields:
            for i in range(num-3):
                self.click_add_another_invite()
        elif num < base_num_of_fields:
            for i in range(3-num):
                pass

    def click_add_another_invite(self):
        self.driver.click_with_timeout(self.INVITE_ANOTHER)

    def click_send_invitations(self):
        self.driver.click_with_timeout(self.SEND_INVITATIONS)

    def fill_email_box(self, email_box_num, email):
        """
        :param email_box_num: starts with 0
        :param email: user email
        """
        self.driver.write_to_element(self.__get_email_box_locator(email_box_num), email)

    def click_roles_box(self, role_box_num):
        role_boxes = self.driver.wait_for_multiple_present(self.SELECT_ROLE_BOXES, timeout=5)
        role_boxes[role_box_num].click()

    def select_role(self, role, role_box_num):
        selectables_of_this_role = self.driver.wait_for_multiple_present(self.__get_select_role_locator(role))
        selectables_of_this_role[role_box_num].click()

    def click_groups_box(self, group_box_num):
        group_inputs = self.driver.wait_for_multiple_present(self.INPUT_GROUP)
        group_inputs[group_box_num].click()

    # its the same as select_role
    def select_group(self, group, group_box_num):
        selectables_of_this_group = self.driver.wait_for_multiple_present(self.__get_select_role_locator(group))
        selectables_of_this_group[group_box_num].click()

    def __get_select_role_locator(self, role):
        f"""
        Fills in {self.SELECT_ROLE_OPTIONS__FORMAT} with role so it returns locator
        :param role: string of a role to choose
        :return: locator of specific email box
        """

        return self.__get_formatted_xpath_locator(self.SELECT_ROLE_OPTIONS__FORMAT, role)

    def __get_email_box_locator(self, num):
        f"""
        Fills in {self.EMAIL_BOX__FORMAT} with number so it returns locator
        :param num: iterated from 0
        :return: locator of specific email box
        """

        return self.__get_formatted_xpath_locator(self.EMAIL_BOX__FORMAT, num)

    @staticmethod
    def __get_formatted_xpath_locator(xpath, formatter):
        """
        Uses xpath tuple with placeholder to be filled in by formatter
        """
        return tuple((xpath[0], xpath[1].format(formatter)))

    def wait_for_lagging_error_on_invalid_emails(self):
        """
        Invalid email error is lagging behind automated script, so here we wait until it appears and disappears
        :return:
        """
        try:
            self.driver.wait_for_visible(self.INVALID_EMAIL, timeout=2)
        except TimeoutException:
            self.driver.wait_for_invisible(self.INVALID_EMAIL, timeout=2)
