from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.configuration_reader import get_config_value

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = get_config_value("BASE_URL")

    def open(self):
        
        self.driver.get(self.base_url)
        return self

    def find_element(self, by, locator):
        try:
            return self.wait.until(
                EC.presence_of_element_located((by, locator))
            )
        except TimeoutException:
            raise NoSuchElementException(f"Element not found with {by}={locator}")

    def click_element(self, by, locator):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
        except TimeoutException:
            raise NoSuchElementException(f"Element not clickable with {by}={locator}")

    def is_element_present(self, by, locator):
        try:
            self.wait.until(EC.presence_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False