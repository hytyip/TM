from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from browser import Browser

class ManageYourMoneyPageLocator(object):
    # Manage Your Money Page Locators

    header_text = (By.XPATH, "//h1")
    continue_to_login_button = (By.XPATH, "//*[contains(text(), 'continue to login')]")


class ManageYourMoneyPage(Browser):
    # Manage Your Money Page Actions
    def get_header(self):
        return self.get_element(*ManageYourMoneyPageLocator.header_text).text

    def click_continue_to_login_button(self):
        self.click_element(*ManageYourMoneyPageLocator.continue_to_login_button)

    def wait_for_element_login_button(self):
        try:
            element_visible = expected_conditions.visibility_of_element_located(*ManageYourMoneyPageLocator.continue_to_login_button)
            WebDriverWait(self.driver, 10).until(element_visible)
        except Exception:
            print("Timed out waiting for page to load")
