from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from browser import Browser

class HomePageLocator(object):
    # Home Page Locators

    header_text = (By.XPATH, "//h1")
    login_button = (By.CSS_SELECTOR, '[data-e2e="login-d"]')
    continue_to_login_button = (By.XPATH, "//*[contains(text(), 'continue to login')]")


class HomePage(Browser):
    # Home Page Actions
    def get_header(self):
        return self.get_element(*HomePageLocator.header_text).text
    
    def click_login_button(self):
        self.click_element(*HomePageLocator.login_button)

    