from tests.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

class HomePage(BasePage):
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search button']")
    SEARCH_INPUT = (By.NAME, "k")
    NEWS_OVERLAY = (By.CLASS_NAME, "component--notifications__story")
    CLOSE_NEWS_BUTTON = (By.CLASS_NAME, "close-button")
    SEARCH_RESULT_WRAPPER = (By.CLASS_NAME, "wrapper.loaded")
    INTERIM_RESULTS_LINK = (By.PARTIAL_LINK_TEXT, "Interim results")

    def handle_news_overlay(self):

        try:
            if self.is_element_present(*self.CLOSE_NEWS_BUTTON):
                self.click_element(*self.CLOSE_NEWS_BUTTON)
                return
            
            search_button = self.find_element(*self.SEARCH_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
            
            time.sleep(0.5)
            
            if self.is_element_present(*self.NEWS_OVERLAY):
                self.driver.execute_script("""
                    var element = document.querySelector('.component--notifications__story');
                    if(element) element.parentNode.removeChild(element);
                """)
                
        except Exception as e:
            print(f"Warning: Error handling news overlay: {str(e)}")

    def click_pre_search_button(self):

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                self.handle_news_overlay()
                
                try:
                    self.click_element(*self.SEARCH_BUTTON)
                except ElementClickInterceptedException:
                    try:
               
                        search_button = self.find_element(*self.SEARCH_BUTTON)
                        self.driver.execute_script("arguments[0].click();", search_button)
                    except Exception:
               
                        search_button = self.find_element(*self.SEARCH_BUTTON)
                        ActionChains(self.driver).move_to_element(search_button).click().perform()
                
                return 
                
            except Exception as e:
                if attempt == max_attempts - 1: 
                    raise Exception(f"Failed to click search button after {max_attempts} attempts: {str(e)}")
                time.sleep(1) 

    def input_search_term(self, term):

        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(term)

    def perform_search(self, term):
  
        try:
            self.click_pre_search_button()
            
            self.wait.until(
                EC.element_to_be_clickable(self.SEARCH_INPUT)
            )
            
            time.sleep(1)
            
            self.input_search_term(term)
            
            search_input = self.find_element(*self.SEARCH_INPUT)
            actual_value = search_input.get_attribute('value')
            assert actual_value == term, f"Search term mismatch. Expected: {term}, Got: {actual_value}"
            
            time.sleep(2)
            
            self.wait.until(
                EC.visibility_of_element_located(self.SEARCH_RESULT_WRAPPER)
            )
            
            assert self.is_search_page_loaded(), "Search page did not load properly"
            
        except Exception as e:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            self.driver.save_screenshot(f"search_operation_failure_{timestamp}.png")
            raise Exception(f"Failed to perform search: {str(e)}")

        time.sleep(2)


        try:
            interim_link = self.wait.until(
                EC.visibility_of_element_located(self.INTERIM_RESULTS_LINK)
            )
            
            actual_href = interim_link.get_attribute('href')
                        
            return actual_href
            
        except Exception as e:            
            try:
                interim_link = self.find_element(*self.INTERIM_RESULTS_LINK)
            except:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                self.driver.save_screenshot(f"interim_results_verification_failure_{timestamp}.png")
                raise Exception(f"Failed to verify interim results link: {str(e)}")
        
    def click_interim_results_link(self):

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                self.handle_news_overlay()  # Overlay'i handle et
                
                interim_link = self.wait.until(
                    EC.element_to_be_clickable(self.INTERIM_RESULTS_LINK)
                )
                
                try:
                    interim_link.click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", interim_link)
                
                return True
                
            except Exception as e:
                if attempt == max_attempts - 1:
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    self.driver.save_screenshot(f"interim_results_click_failure_{timestamp}.png")
                    raise Exception(f"Failed to click interim results link after {max_attempts} attempts: {str(e)}")
                time.sleep(1)

    def get_interim_results_link_text(self):
        
        try:
            interim_link = self.wait.until(
                EC.visibility_of_element_located(self.INTERIM_RESULTS_LINK)
            )
            return interim_link.text
        except Exception as e:
            raise Exception(f"Failed to get interim results link text: {str(e)}")

    def is_search_page_loaded(self):
        return self.is_element_present(*self.SEARCH_RESULT_WRAPPER)