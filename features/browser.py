from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Browser(object):

    driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
    
    def quit(context):
        context.driver.quit()

    def get_element(context, *locator):
        return context.driver.find_element(*locator)

    def click_element(context, *locator):
        context.driver.find_element(*locator).click()

    def navigate(context, address):
        context.driver.get(address)

    def get_page_title(context):
        return context.driver.title

    def element_displayed(self, *locator):
        return self.get_element(*locator).is_displayed()

    def window_handles(context, number):
        return context.driver.window_handles[number]
        
    def switch_to_window(context, name):
        context.driver.switch_to_window(name)

    def wait_for_ajax(context):
        wait = WebDriverWait(context.driver, 15)
        try:
            wait.until(lambda driver: context.driver.execute_script('return jQuery.active') == 0)
            wait.until(lambda driver: context.driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass

    