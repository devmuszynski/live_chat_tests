from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BaseDriver(webdriver.Remote):

    def __init__(self, default_element_timeout=10):
        self.elem_timeout = default_element_timeout
        super().__init__()

    def _until(self, method, timeout):
        return WebDriverWait(self, timeout).until(method)

    def wait_for_clickable(self, locator, timeout=10):
        return self._until(EC.element_to_be_clickable(locator), timeout)

    def wait_for_clickable_and_scroll(self, locator, timeout):
        elem = self.wait_for_present(locator, timeout)
        self.scroll_to_element(elem)
        return self.wait_for_clickable(locator, timeout=1)

    def wait_for_visible(self, locator, timeout=10):
        return self._until(EC.visibility_of_element_located(locator), timeout)

    def wait_for_present(self, locator, timeout=10):
        return self._until(EC.presence_of_element_located(locator), timeout)

    def wait_for_multiple_present(self, locator, timeout=10):
        """
        :return: list of elements found
        """
        return self._until(EC.presence_of_all_elements_located(locator), timeout)

    def wait_for_invisible(self, locator, timeout=10):
        return self._until(EC.invisibility_of_element(locator), timeout)

    def click_with_timeout(self, locator, timeout=10):
        elem = self.wait_for_clickable(locator, timeout)
        elem.click()

    def click_with_timeout_and_scroll(self, locator, timeout=10):
        elam = self.wait_for_clickable_and_scroll(locator, timeout)
        elam.click()

    def write_to_element(self, locator, text, timeout=10):
        elem = self.wait_for_clickable(locator, timeout)
        elem.clear()
        elem.send_keys(text)

    def scroll_to_element(self, elem):
        actions = ActionChains(self)
        actions.move_to_element(elem).perform()


class ChromeDriver(webdriver.Chrome, BaseDriver):

    def __init__(self):
        super().__init__()


class FirefoxDriver(webdriver.Firefox, BaseDriver):

    def __init__(self):
        super().__init__()

