from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
import time


@step('I visit the thinkmoney website')
def step_impl(context):
    context.home_page.navigate("https://www.thinkmoney.co.uk")

@step('I click the login button')
def step_impl(context):
    context.home_page.click_login_button()

@step('I see the thinkmoney homepage')
def step_impl(context):
    assert_equal(context.home_page.get_page_title(), "Digital banking for everyone | thinkmoney")
    assert_equal(context.home_page.get_header(), "Digital banking for everyone")

@step('I see the "Manage your money" page')
def step_impl(context):
    context.browser.wait_for_ajax()
    context.manage_your_money_page.wait_for_element_login_button()
    assert_equal(context.manage_your_money_page.get_page_title(), "Online banking | Open a bank account online | thinkmoney")
    assert_equal(context.manage_your_money_page.get_header(), "Manage your money with online banking")

@step('I click the Continue To Login button')
def step_impl(context):
    context.manage_your_money_page.click_continue_to_login_button()

@step('I see the Login page')
def step_impl(context):
    context.browser.wait_for_ajax()
    window_after = context.browser.window_handles(1)
    context.browser.switch_to_window(window_after)
    assert_equal(context.login_page.get_page_title(), "Login")
    assert_equal(context.login_page.username_textbox_displayed(), True)
    assert_equal(context.login_page.password_textbox_displayed(), True)
