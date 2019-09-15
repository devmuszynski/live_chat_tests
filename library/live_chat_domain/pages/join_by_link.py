from selenium.webdriver.common.by import By


class JoinByLink:

    EMAIL = (By.ID, "email")
    NAME = (By.ID, "name")
    PASSWORD = (By.ID, "password")

    JOIN = (By.CSS_SELECTOR, "button.button.red")

    def __init__(self, driver):
        self.driver = driver

    def join(self, link, email, name, password):
        self.driver.get(link)
        self.fill_in_email(email)
        self.fill_in_name(name)
        self.fill_in_password(password)
        self.click_join()

    def fill_in_email(self, email):
        self.driver.write_to_element(self.EMAIL, email)

    def fill_in_name(self, name):
        self.driver.write_to_element(self.NAME, name)

    def fill_in_password(self, password):
        self.driver.write_to_element(self.PASSWORD, password)

    def click_join(self):
        self.driver.click_with_timeout(self.JOIN)

