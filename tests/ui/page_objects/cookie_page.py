from tests.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CookiePage(BasePage):
    
    ACCEPT_COOKIES_BUTTON = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")

    def accept_all_cookies(self):
        """
        Accept all cookies
        """
        self.click_element(*self.ACCEPT_COOKIES_BUTTON)
