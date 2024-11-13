import pytest
import time
from selenium.webdriver.common.keys import Keys
from tests.ui.page_objects.cookie_page import CookiePage
from tests.ui.page_objects.home_page import HomePage

class TestWebsite:
    @pytest.mark.ui
    def test_search_feature(self, driver):
        """
           UI tests for the TestWebsite for the search feature    
        """
        cookie_page = CookiePage(driver)
        cookie_page.open()
        cookie_page.accept_all_cookies()
            
        home_page = HomePage(driver)
        search_term = "IFRS 17"
        home_page.perform_search(search_term)   
        link_text = home_page.get_interim_results_link_text()
        assert "Interim results for the six months ended 30 June 2022" in link_text
        home_page.click_interim_results_link()

            

                