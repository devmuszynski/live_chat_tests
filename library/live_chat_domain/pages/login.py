from selenium.webdriver.common.by import By


class LoginPage:

    EMAIL_BOX = (By.ID, "email")
    PASSWORD_BOX = (By.ID, "password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button.button.red")

    def __init__(self, driver):
        self.driver = driver

    def login(self, address, email, password):
        self.driver.get(address)

        self.fill_email_box(email)
        self.fill_password_box(password)
        self.click_login_button()

    def fill_email_box(self, email):
        self.driver.write_to_element(self.EMAIL_BOX, email)

    def fill_password_box(self, password):
        self.driver.write_to_element(self.PASSWORD_BOX, password)

    def click_login_button(self):
        self.driver.click_with_timeout(self.SIGN_IN_BUTTON)
