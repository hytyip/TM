from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginPageLocator(object):
    # Search Results Page Locators

    header_text = (By.XPATH, "//h1")
    username_textbox = (By.ID, "ThinkMoney_Theme_wt28_block_wtMainContent_OnlineBanking_CW_wt55_block_wtMainContent_OnlineBanking_CW_wt86_block_wtInputWidget_ThinkMoney_Patterns_wt52_block_wtInput_Label_wtUserNameInput")
    password_textbox = (By.ID, "ThinkMoney_Theme_wt28_block_wtMainContent_OnlineBanking_CW_wt55_block_wtMainContent_OnlineBanking_CW_wt68_block_wtInputWidget_ThinkMoney_Patterns_wt88_block_wtInput_Label_wtPasswordInput")

class LoginPage(Browser):
    # Login Page Actions

    def get_header(self):
        return self.get_element(*LoginPageLocator.header_text).text

    def username_textbox_displayed(self):
        return self.element_displayed(*LoginPageLocator.username_textbox)

    def password_textbox_displayed(self):
        return self.element_displayed(*LoginPageLocator.password_textbox)