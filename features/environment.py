from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.manage_your_money_page import ManageYourMoneyPage
from pages.login_page import LoginPage
from allure_behave.hooks import allure_report

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.manage_your_money_page = ManageYourMoneyPage()
    context.login_page = LoginPage()
    allure_report("path/to/result/dir")

def after_all(context):
    context.browser.quit()